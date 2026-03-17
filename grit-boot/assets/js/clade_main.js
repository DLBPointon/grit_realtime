
function cladegrapher() {
    const { SINGLE_LETTER_MAP, ADDRESS } = window.GRIT_STATIC;

    var one = document.getElementById('CladeSelector');
    prefix = one.options[one.selectedIndex].value

    var two = document.getElementById('CladeGraphSelector1X');
    two = two.options[two.selectedIndex].value

    var three = document.getElementById('CladeGraphSelector1Y');
    three = three.options[three.selectedIndex].value

    var four = document.getElementById('CladeGraphSelector1C');
    four = four.options[four.selectedIndex].value

    var legendToggle = document.getElementById('CladeGraphLegendToggle');
    var showLegend = legendToggle ? legendToggle.checked : true;

    var url = ADDRESS + 'order=family_name.asc&prefix_sl=in.('
        + prefix + ')&select=' + two + ',family_name,prefix_dl,prefix_fn,project_type,' + three

    d3.json(url, function (error, data) {
        if (error) return console.warn(error);
        var x = [];
        var y = [];
        var c = [];

        data.forEach((item) => {
            x.push(item[two]);

            if (three.includes('length_after')) {
                y.push((item['manual_interventions'] / item['length_after']) * 1000000000)
            } else {
                y.push(item[three]);
            }

            c.push(item[four]);
        });

        var elmnt = document.getElementById("cladetest").clientWidth - 60

        var trace1 = {
            type: 'scatter',
            x: x,
            y: y,
            mode: 'markers',
            transforms: [{
                type: 'groupby',
                groups: c
            }],
            name: 'cladegraph',
            marker: {
                line: { width: 1, },
                symbol: 'circle',
                size: 5
            }
        }

        var datas = [trace1];


        var layout = {
            xaxis: {
                showgrid: false,
                showline: true,
                linecolor: 'rgb(102, 102, 102)',
                titlefont: { font: { color: 'rgb(204, 204, 204)' } },
                tickfont: { font: { color: 'rgb(102, 102, 102)' } },
                autotick: true,
                dtick: 10,
                ticks: 'outside',
                tickcolor: 'rgb(102, 102, 102)'
            },
            margin: {
                l: 50,
                r: 0,
                t: 30,
            },
            showlegend: showLegend,
            legend: {
                font: { size: 8, },
                orientation: 'h',
                x: 0,
                xanchor: 'left',
                y: 1.02,
                yanchor: 'bottom'
            },
            width: elmnt
        };
        var config = { responsive: true, displayModeBar: true }
        Plotly.react('cladetest', datas, layout, config);
    }
    )

}

cladegrapher()
