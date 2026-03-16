TESTER = document.getElementById('rightgraph1');

function makegraph_box() {

    const SINGLE_LETTER_MAP = {
        a: "Amphibians",
        b: "Birds",
        c: "Non-Vascular plants",
        d: "Dicotyledons",
        e: "Echinoderm",
        f: "Fishes",
        g: "Fungi",
        h: "Platyhelminths",
        i: "Insects",
        j: "Jellyfish and other Cnidaria",
        k: "Other chordates",
        l: "Monocotyledons(lilies etc.)",
        m: "Mammals",
        n: "Nematodes",
        o: "Sponges",
        p: "Protists",
        q: "Other arthropods",
        r: "Reptiles",
        s: "Sharks and relatives",
        t: "Other animal phyla",
        u: "Algae",
        v: "Other vascular plants",
        w: "Annelids(worms)",
        x: "Molluscs",
        y: "Bacteria",
        z: "Archea",
        "-": "Viruses"
    }


    var two = document.getElementById('RightGraphSelector1Y');
    two = two.options[two.selectedIndex].value
    var three = document.getElementById('RightGraphSelector1C');
    three = three.options[three.selectedIndex].value

    var legendToggle = document.getElementById('RightGraph1LegendToggle');
    var showLegend = legendToggle ? legendToggle.checked : true;

    if (two === 'mipergb') {
        var url = 'http://0.0.0.0:8001/gritdata?select=manual_interventions,' + three + ',length_after'
    } else {
        var url = 'http://0.0.0.0:8001/gritdata?select=' + two + ',' + three
    }

    d3.json(url, function (error, data) {
        if (error) return console.warn(error);
        var y = [];
        var c = [];


        data.forEach((item) => {
            if (two === 'mipergb') {
                y.push((item['manual_interventions'] / item['length_after']) * 1000000000)
            } else {
                y.push(item[two]);
            }

            if (three === 'prefix_sl') {
                c.push(SINGLE_LETTER_MAP[item[three]]);
            } else {
                c.push(item[three]);
            }
        });

        var trace1 = {
            type: 'box',
            x: c,
            y: y,
            transforms: [{
                type: 'groupby',
                groups: c
            }]
        };

        var datas = [trace1];

        var elmntr1 = document.getElementById("rightgraph1").clientWidth - 30


        var layout = {
            width: elmntr1,
            autosize: true,
            showlegend: showLegend,
            margin: {
                l: 50,
                r: 50,
                t: 0
            },
        };

        var config = { responsive: true, displayModeBar: true }
        Plotly.react('rightgraph1', datas, layout, config)
    })
}

makegraph_box()
