// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // Логика бургер-меню
    const hamburger = document.querySelector('.hamburger-menu');
    const navList = document.querySelector('.nav-list');

    if (hamburger && navList) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('open');
            navList.classList.toggle('open');
        });
    }

    // Простая анимация появления при прокрутке (добавляет класс 'visible')
    const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Прекратить наблюдение после анимации
            }
        });
    }, { threshold: 0.1 }); // Срабатывает, когда 10% элемента видно

    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });
});
