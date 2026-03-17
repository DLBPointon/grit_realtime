function loadPartial(targetId, url) {
    return fetch(url)
        .then((res) => {
            if (!res.ok) {
                throw new Error(`Failed to load ${url}: ${res.status}`);
            }
            return res.text();
        })
        .then((html) => {
            var target = document.getElementById(targetId);
            if (target) {
                target.innerHTML = html;
            }
        })
        .catch((err) => {
            console.error(err);
        });
}

function setActiveNav() {
    var current = window.location.pathname.split('/').pop();
    if (!current) {
        current = 'index.html';
    }

    var links = document.querySelectorAll('#accordionSidebar a.nav-link');
    links.forEach(function (link) {
        var href = link.getAttribute('href');
        if (href === current) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    Promise.all([
        loadPartial('site-header', 'partials/header.html'),
        loadPartial('site-footer', 'partials/footer.html')
    ]).then(function () {
        setActiveNav();
    });
});
