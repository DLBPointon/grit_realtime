(function () {
    function assertStaticValues() {
        if (!window.GRIT_STATIC || !window.GRIT_STATIC.ADDRESS) {
            throw new Error("GRIT_STATIC is not loaded. Ensure assets/js/static_values.js is included before page_helpers.js.");
        }
    }

    function getAddress() {
        assertStaticValues();
        return window.GRIT_STATIC.ADDRESS;
    }

    window.assertStaticValues = assertStaticValues;

    window.rowcountDashboard = function () {
        var url = getAddress();
        d3.json(url, function (error, data) {
            if (error) return console.warn(error);
            var number = Object.keys(data).length;
            document.getElementById("rowscounted").innerHTML = JSON.stringify(number);
        });
    };

    window.latestDateDashboard = function () {
        var url = getAddress() + "limit=1&order=date_updated.desc&select=date_updated";
        d3.json(url, function (error, data) {
            if (error) return console.warn(error);
            var date_item = JSON.stringify(data).split(":")[1].split('"');
            document.getElementById("updated_when").innerHTML = date_item[1];
        });
    };

    window.connectionStatusDashboard = function () {
        var url = getAddress() + "limit=1";
        fetch(url)
            .then(function (data) {
                if (data.ok) {
                    document.getElementById("db_con").innerHTML = "Online";
                    document.getElementById("db_con").style.color = "green";
                } else {
                    document.getElementById("db_con").innerHTML = "Offline";
                    document.getElementById("db_con").style.color = "red";
                }
            })
            .catch(function (e) {
                console.error("EXCEPTION: ", e);
            });
    };

    window.rowcountClade = function () {
        var one = document.getElementById("CladeSelector");
        if (!one) return;
        var prefix = one.options[one.selectedIndex].value;
        var url = getAddress() + "order=family_name.asc&prefix_sl=in.(" + prefix + ")";
        d3.json(url, function (error, data) {
            if (error) return console.warn(error);
            var number = Object.keys(data).length;
            document.getElementById("rowscounted3").innerHTML = JSON.stringify(number);
        });
    };

    window.rowcountProject = function () {
        var one = document.getElementById("CladeSelectorP");
        if (!one) return;
        var proj = one.options[one.selectedIndex].value;
        var tickets = ["GRIT", "RC"];
        var url = tickets.includes(proj)
            ? getAddress() + "order=family_name.asc&project_code=in.(" + proj + ")"
            : getAddress() + "order=family_name.asc&project_type=in.(" + proj + ")";
        d3.json(url, function (error, data) {
            if (error) return console.warn(error);
            var number = Object.keys(data).length;
            document.getElementById("rowscounted2").innerHTML = JSON.stringify(number);
        });
    };
})();
