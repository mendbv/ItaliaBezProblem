document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger-menu');
    const navList = document.querySelector('.nav-list');

    if (hamburger && navList) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('open');
            navList.classList.toggle('open');
        });
    }

    const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });
});
