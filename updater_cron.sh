while getopts r flag
do
    case "${flag}" in
        r) run=false;;
    esac
done


if [ "$run" == false ]; then
    echo "FULL JIRA_DUMP IN PROGRESS";
    rm /home/grit/grt-v5/grit-boot/output/jira_dump.tsv;
    touch /home/grit/grt-v5/grit-boot/output/jira_dump.tsv;
    /home/grit/miniconda3/envs/grt-env/bin/python3 /home/grit/grt-v5/scripts/jira_connect.py -o ./grit-boot/output/jira_dump.tsv &&
    sleep 10
fi

cd /home/grit/grt-v5/ &&
/usr/local/bin/docker-compose down --volumes &&
sleep 10 &&
git pull origin production-sos &&
sleep 5 &&
/usr/local/bin/docker-compose up -d &
