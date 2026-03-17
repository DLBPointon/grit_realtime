function telo_pie() {

    const { ADDRESS } = window.GRIT_STATIC;

    var one = document.getElementById('telo_selector1');
    one = one.options[one.selectedIndex].value

    var legendToggle = document.getElementById('TeloPieLegendToggle');
    var showLegend = legendToggle ? legendToggle.checked : true;

    var url = ADDRESS + 'select=' + one

    d3.json(url, function (error, data) {
        if (error) return console.warn(error);
        var c = [];
        var count = {};

        data.forEach((item) => {
            var value = item[one];
            if (value === null || value === undefined || value === '') {
                return;
            }
            c.push(value);
        });

        for (var i = 0; i < c.length; ++i) {
            if (!count[c[i]])
                count[c[i]] = 0;
            ++count[c[i]];
        }

        var datas = [{
            values: Object.values(count),
            labels: Object.keys(count),
            type: 'pie'
        }];

        var elmntr2 = document.getElementById("telo_right1").clientWidth - 30

        var layout = {
            width: elmntr2,
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
        Plotly.react('telo_right1', datas, layout, config);

    })
}
