function playIntroFadeinOnce() {
    const key = 'introFadeinShown';
    const isHome = window.location.pathname === '/';
    const elements = document.querySelectorAll('.intro_fadein');

    if (isHome || !sessionStorage.getItem(key)) {
        elements.forEach((element) => {
            element.classList.add('play_fadein');
        });

        sessionStorage.setItem(key, 'true');
    }
}

function playPageFadein() {
    const elements = document.querySelectorAll('.page_fadein');

    elements.forEach((element) => {
        element.classList.add('play_fadein');
    });
}