TESTER = document.getElementById('test');

function makegraph() {

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


    var one = document.getElementById('MainGraphSelector1X');
    one = one.options[one.selectedIndex].value
    var two = document.getElementById('MainGraphSelector1Y');
    two = two.options[two.selectedIndex].value
    var three = document.getElementById('MainGraphSelector1C');
    three = three.options[three.selectedIndex].value

    var legendToggle = document.getElementById('MainGraph1LegendToggle');
    var showLegend = legendToggle ? legendToggle.checked : true;

    if (two === 'mipergb') {
        var url = 'http://0.0.0.0:8001/gritdata?select=' + one + ',manual_interventions,' + three + ',length_after'
    } else {
        var url = 'http://0.0.0.0:8001/gritdata?select=' + one + ',' + two + ',' + three
    }

    d3.json(url, function (error, data) {
        if (error) return console.warn(error);
        var x = [];
        var y = [];
        var c = [];

        data.forEach((item) => {
            x.push(item[one]);

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
            type: 'scatter',
            x: x,
            y: y,
            mode: 'markers',
            transforms: [{
                type: 'groupby',
                groups: c
            }],
            name: 'maingraph1',
            marker: {
                line: { width: 1, },
                symbol: 'circle',
                size: 5
            }
        };

        var datas = [trace1];

        var elmnt = document.getElementById("test").clientWidth - 30

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
                r: 50,
                b: 100
            },
            showlegend: showLegend,
            legend: {
                font: { size: 8, },
                yanchor: 'middle',
                xanchor: 'right'
            },
            autosize: true,
            width: elmnt
        };
        var config = { responsive: true, displayModeBar: true }
        Plotly.newPlot('test', datas, layout, config);

        document.getElementById('test').on('plotly_doubleclick', function (datas) {
            console.log("This far")
            Plotly.toImage('test', { format: 'jpeg', height: 500, width: 800 }).then(function (dataUrl) {
                var iframe = "<iframe width='100%' height='100%' src='" +
                    dataUrl + "'></iframe>"
                var x = window.open();
                x.document.open();
                x.document.write(iframe);
                x.document.close();
            });

        })
    }
    )
}

makegraph()
