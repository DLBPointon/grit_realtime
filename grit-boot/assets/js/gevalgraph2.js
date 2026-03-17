TESTER = document.getElementById('gevalgraph2');

function gevalgraph2() {

    const { ADDRESS } = window.GRIT_STATIC;

    var three = document.getElementById('gevalgraph2gb');
    three = three.options[three.selectedIndex].value
    var one = 'sample_id';
    var two = 'scaff_n50_change';
    var four = 'length_after';

    var legendToggle = document.getElementById('GevalGraph2LegendToggle');
    var showLegend = legendToggle ? legendToggle.checked : true;

    var url = ADDRESS + 'select=' + one + ',' + two + ',' + three + ',' + four;

    d3.json(url, function (error, data) {
        if (error) return console.warn(error);
        var x = [];
        var y = [];
        var c = [];
        var label = [];

        data.forEach((item) => {
            x.push(item[four] / 1000000000);
            y.push(item[two]);
            c.push(item[three]);
            label.push('Org: ' + item[one] + ' | Percent change: ' + item[two])
        });

        var trace1 = {
            type: 'scatter',
            x: x,
            y: y,
            mode: 'markers',
            text: label,
            transforms: [{
                type: 'groupby',
                groups: c
            }]
        };

        var datas = [trace1];

        var elmntgg2 = document.getElementById("gevalgraph2").clientWidth - 30

        var layout = {
            title: 'Scaff N50 count change (%) by Assembly size (Gb)',
            xaxis: {
                title: 'Assembly Size (Gb)'
            },
            yaxis: {
                title: 'Scaff N50 count change (%)'
            },
            showlegend: showLegend,
            legend: {
                orientation: 'h',
                x: 0,
                xanchor: 'left',
                y: 1.02,
                yanchor: 'bottom'
            },
            margin: {
                t: 30
            },
            width: elmntgg2

        };

        var config = { responsive: true, displayModeBar: true }
        Plotly.react('gevalgraph2', datas, layout, config)

    })
}

gevalgraph2()
