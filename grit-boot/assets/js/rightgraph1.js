TESTER = document.getElementById('rightgraph1');

function makegraph_box() {

    const { ADDRESS, SINGLE_LETTER_MAP } = window.GRIT_STATIC;
    var two = document.getElementById('RightGraphSelector1Y');
    two = two.options[two.selectedIndex].value
    var three = document.getElementById('RightGraphSelector1C');
    three = three.options[three.selectedIndex].value

    var legendToggle = document.getElementById('RightGraph1LegendToggle');
    var showLegend = legendToggle ? legendToggle.checked : true;

    if (two === 'mipergb') {
        var url = ADDRESS + 'select=manual_interventions,' + three + ',length_after'
    } else {
        var url = ADDRESS + 'select=' + two + ',' + three
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
            legend: {
                orientation: 'h',
                x: 0,
                xanchor: 'left',
                y: 1.02,
                yanchor: 'bottom'
            },
            margin: {
                l: 50,
                r: 50,
                t: 30
            },
        };

        var config = { responsive: true, displayModeBar: true }
        Plotly.react('rightgraph1', datas, layout, config)
    })
}

makegraph_box()
