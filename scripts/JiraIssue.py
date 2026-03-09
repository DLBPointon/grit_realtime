import io
import re
import maya
from datetime import date
import requests
import logging
from prefix_assignments import master_dict, dl_dict

logger = logging.getLogger(__name__)

class JiraIssue:
    _ids = 0

    def __init__(self, raw_issue):
        JiraIssue._ids += 1
        fields = raw_issue.fields

        self.instance_no = JiraIssue._ids
        self.issue = raw_issue.key
        self.ticket_type = str(self.issue).split("-")[0]
        self.project_type = fields.issuetype.name
        self.scientific_name, self.family_data = self.get_taxonomy(
            raw_issue.get_field("customfield_11676")
        )
        self.curator = (
            raw_issue.get_field("customfield_11657")#["value"]
            if raw_issue.get_field("customfield_11657")
            else "EXTERNAL"
        )
        self.summary = fields.summary
        self.name_and_accession = self.parse_db_name(
            raw_issue.get_field("customfield_11643"),  # Geval DB ID
            raw_issue.get_field("customfield_11627"),  # Sample ID - ToLID Minus accession
            raw_issue.get_field("customfield_11609"),  # supposed to be the accession
        )
        self.prefix, self.prefix_verbose, self.prefix_label = self.get_prefixes(
            raw_issue.get_field("customfield_11627")  # Sample ID - ToLID Minus accession
        )
        self.length_before, self.length_after, self.length_change_per = (
            self.get_length_info(raw_issue.get_field("customfield_11608"))
        )
        self.date_updated = date.today()
        self.date_created = self.get_date(fields.created)
        self.telo_motif = (
            "N/A"
            if raw_issue.get_field("customfield_11650") is None
            else raw_issue.get_field("customfield_11650")
        )

        self.telo_len = (
            0
            if raw_issue.get_field("customfield_11651") is None
                else int(raw_issue.get_field("customfield_11651"))
        )
        self.chr_naming = (
            raw_issue.get_field("customfield_11607") #get the value
            if raw_issue.get_field("customfield_11607") is not None
            else "N/A"
        )
        self.expected_sex = self.get_sex(raw_issue.get_field("customfield_11641"))
        self.observed_sex = self.get_sex(raw_issue.get_field("customfield_11601"))
        self.curated_auto = (
            int(raw_issue.get_field("customfield_11659"))
            if raw_issue.get_field("customfield_11659") is not None
            else 0
        )
        self.curated_allo = (
            self.fix_odd_data(raw_issue.get_field("customfield_11617"))
            if raw_issue.get_field("customfield_11617") is not None
            else "N/A"
        )

        self.n50_before, self.n50_after, self.n50_change_percentage = self.get_n50_info(
            raw_issue.get_field("customfield_11608")
        )

        self.scaff_count_before, self.scaff_count_after, self.scaff_count_percentage = (
            self.get_scaff_count(raw_issue.get_field("customfield_11608"))
        )

        self.chr_assignment, self.assignment_percent = self.get_chr_data(
            raw_issue.get_field("customfield_11645")
        )

        self.interventions = self.calc_interventions(raw_issue)

        self.collection = self.__iter__()

    def __iter__(self):
        yield from self.__dict__.items()

    def __str__(self):
        txt = io.StringIO()
        txt.write(f"{self.__class__.__name__}:\n")
        [
            txt.write(f"- {a}: {b} \n")
            for a, b in self.collection
            if a not in ["block", "collection", "contents"]
        ]
        return txt.getvalue()

    def parse_db_name(self, db_name, name, accession):
        """
        Function to return the internal TolID + accession
        :param db_name:
        :return:
        """
        if name == "aBomBom1":
            name_and_accession = str(name) + "_" + str(accession)
        else:
            name_and_accession = str(name) + "_" + str(accession)

        return name_and_accession

    def get_prefixes(self, sample_name):
        """
        Function to pull prefix, prefix_verbose and prefix_full from name_ass.
        from ilAliOxi1:
        prefix = i
        prefix_verbose = il
        prefix_full = insect, would hope to pull lepidoptera for more specificity
        :param sample_name:
        :return:
        """
        if sample_name.startswith("CAM"):
            prefix = "i"
            prefix_verbose = "il"
            logging.info(f"|> Non-standard ticket: {sample_name}")
        elif sample_name.startswith("PS"):
            prefix = "n"
            prefix_verbose = "nx"
            logging.info(f"|> Non-standard ticket: {sample_name}")
        elif sample_name.startswith("HG"):
            prefix = "m"
            prefix_verbose = "m"
            logging.info(f"|> Non-standard ticket: {sample_name}")
        else:
            prefix_search = re.search(r"([a-z])", sample_name)
            prefix = prefix_search.group(1) if prefix_search is not None else None

            prefix_verbose_search = re.search(r"([a-z]*)", sample_name)
            prefix_verbose = prefix_verbose_search.group(1) if prefix_verbose_search is not None else None

        prefix_full = ""

        if len(str(prefix_verbose)) == 2:
            prefix_full = dl_dict.get(prefix_verbose)
        else:
            prefix_full = master_dict.get(prefix)

        return prefix, prefix_verbose, prefix_full

    def get_date(self, date_string):
        """
        A function to return a parsable date/time object for use in graphing by date
        :param date_obj:
        :return:
        """
        obj = maya.parse(date_string).datetime()
        ymd_date = obj.date().strftime("%Y-%m-%d")

        return ymd_date

    def get_taxonomy(self, latin_name):
        """
        A function to parse just the latin name from the returned value
        :param latin_name:
        :return:
        """
        scientific_name_search = re.search(r"([A-Z]\S*.\w*)", latin_name)
        scientific_name_result = scientific_name_search.group(1) if scientific_name_search is not None else None

        # For the occasional "genus_species" result rather than "genus species"
        if "_" in str(scientific_name_result):
            split_here = str(scientific_name_result).split("_")
            scientific_name_result = " ".join(split_here)

        scientific_name = str(scientific_name_result).split(" ")

        response = requests.get(
            f"https://www.ebi.ac.uk/ena/taxonomy/rest/scientific-name/{scientific_name[0]}%20{scientific_name[1]}"
        )

        if response.text == "No results.":
            family_data = "UNKNOWN"
        elif response.text == "[ ]":
            data_lineage, family_data = "NCBI ERROR", "NCBI ERROR"
        else:
            data = response.json()
            data_lineage = data[0]["lineage"]
            family = data_lineage.split("; ")
            family_data = family[-3]

        return scientific_name_result, family_data

    def fix_odd_data(self, allosome_data):
        if "," in allosome_data:
            splitres = allosome_data.split(",")
            curated_allo = str("".join(splitres))
        else:
            curated_allo = str(allosome_data)

        return curated_allo

    def get_length_info(self, data):
        """
        Function to return the length information hidden in assembly stats
        :param scaff_data:
        :return:
        """
        if data:
            length_search = re.search(r"total\s*([0-9]\w+)\s*([0-9]\w+)", data)
            length_before = int(length_search.group(1)) if length_search is not None else None
            length_after = int(length_search.group(2)) if length_search is not None else None
            if length_after is not None and length_before is not None:
                length_change_per = (length_after - length_before) / length_before * 100
            else:
                length_change_per = None
        else:
            length_before, length_after, length_change_per = None, None, None
        return length_before, length_after, length_change_per

    def get_n50_info(self, scaff_data):
        """
        Function to return the length information hidden in assembly stats
        :param scaff_data:
        :return:
        """
        if scaff_data:
            n50_search = re.search(r"N50\s*([0-9]*)\s*([0-9]*)", scaff_data)
            if n50_search is not None:
                n50_before = int(n50_search.group(1))
                n50_after = int(n50_search.group(2))
                n50_ab = n50_after - n50_before
                if n50_ab == 0:
                    n50_change_per = 0
                else:
                    n50_change_per = (n50_after - n50_before) / n50_before * 100
        else:
            n50_before, n50_after, n50_change_per = None, None, None

        return n50_before, n50_after, n50_change_per

    def get_scaff_count(self, scaff_data):
        """

        :param scaff_data:
        :return:
        """
        if scaff_data:
            scaff_count_search = re.search(r"count\s*([0-9]*)\s*([0-9]*)", scaff_data)
            if scaff_count_search is not None:
                scaff_count_before = int(scaff_count_search.group(1))
                scaff_count_after = int(scaff_count_search.group(2))
                if scaff_count_before + scaff_count_after == 0:
                    scaff_count_per = 0
                else:
                    scaff_count_per = (
                        (scaff_count_after - scaff_count_before) / scaff_count_before * 100
                    )
        else:
            scaff_count_before, scaff_count_after, scaff_count_per = None, None, None

        return scaff_count_before, scaff_count_after, scaff_count_per

    def get_chr_data(self, chromo_res):
        """
        Function to parse and return the chromosome assignment and assignment %
        :param chromo_res:
        :return:
        """
        if chromo_res:
            chr_ass_search = re.search(r"(found.[0-9].*somes.*\(.*\))", chromo_res)
            if chr_ass_search:
                chr_ass = chr_ass_search.group(1)
            elif chr_ass_search is None:
                chr_ass_search = re.search(r"(found.[0-9].*somes)", chromo_res)
                if chr_ass_search:
                    chr_ass = chr_ass_search.group(1)
                else:
                    chr_ass = None
            else:
                chr_ass = None

            ass_percent_search = re.search(r"Chr.length.(\d*.\d*).%", chromo_res)
            ass_percent = ass_percent_search.group(1) if ass_percent_search else None
        else:
            chr_ass, ass_percent = None, None

        return chr_ass, ass_percent

    def calc_interventions(self, issue):
        interventions = 0
        interaction_list = {
            "manual_breaks": issue.get_field("customfield_11615"),
            "manual_joins": issue.get_field("customfield_11681"),
            "manual_inversions": issue.get_field("customfield_10610"),
            "manual_haplotig_removals": issue.get_field("customfield_11632"),
        }

        for x, y in interaction_list.items():
            if y is not None:
                interventions += int(y)

        return interventions

    def get_sex(self, data):
        return data if data else None

    def output_list(self):
        return [
            self.name_and_accession,
            self.scientific_name,
            self.prefix,
            self.prefix_verbose,
            self.prefix_label,
            self.family_data,
            self.issue,
            self.project_type,
            self.length_before,
            self.length_after,
            self.length_change_per,
            self.n50_before,
            self.n50_after,
            self.n50_change_percentage,
            self.scaff_count_before,
            self.scaff_count_after,
            self.scaff_count_percentage,
            self.chr_assignment,
            self.assignment_percent,
            self.date_created,
            self.date_updated,
            self.interventions,
            self.chr_naming,
            (None if self.expected_sex == "N/A" else self.expected_sex),
            (None if self.observed_sex == "N/A" else self.observed_sex),
            (0 if self.curated_auto == 0 else self.curated_auto),
            (None if self.curated_allo == "N/A" else self.curated_allo),
            (None if self.ticket_type == "N/A" else self.ticket_type),
            (None if self.telo_motif == "N/A" else self.telo_motif),
            (None if self.telo_len == 0 else self.telo_len),
        ]
