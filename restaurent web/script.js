document.addEventListener('DOMContentLoaded', () => {
    // Form Submission
    const contactForm = document.querySelector('.contact-form-card form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Thank you! Your message has been successfully sent. 🍽️');
            contactForm.reset();
        });
    }

    // Simple Slider Logic for Gallery
    const slider = document.querySelector('.gallery-slider');
    const nextBtn = document.querySelector('.next');
    const prevBtn = document.querySelector('.prev');

    if (slider && nextBtn && prevBtn) {
        nextBtn.addEventListener('click', () => {
            slider.scrollBy({ left: 370, behavior: 'smooth' });
        });

        prevBtn.addEventListener('click', () => {
            slider.scrollBy({ left: -370, behavior: 'smooth' });
        });
    }

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'white';
            navbar.style.boxShadow = '0 10px 30px rgba(0,0,0,0.1)';
            navbar.style.padding = '10px 80px';
        } else {
            navbar.style.background = 'transparent';
            navbar.style.boxShadow = 'none';
            navbar.style.padding = '20px 80px';
        }
    });
});
