
// Typing animation
const texts = [
    "Data Scientist",
    "Machine Learning Engineer", 
    "AI Enthusiast",
    "Python Developer",
    "Problem Solver"
];

let textIndex = 0;
let charIndex = 0;
let currentText = '';
let isDeleting = false;

function typeWriter() {
    const typedElement = document.querySelector('.typed-text');
    
    if (!typedElement) return;
    
    if (isDeleting) {
        currentText = texts[textIndex].substring(0, charIndex - 1);
        charIndex--;
    } else {
        currentText = texts[textIndex].substring(0, charIndex + 1);
        charIndex++;
    }
    
    typedElement.textContent = currentText;
    
    let typeSpeed = 100;
    
    if (isDeleting) {
        typeSpeed /= 2;
    }
    
    if (!isDeleting && charIndex === texts[textIndex].length) {
        typeSpeed = 2000;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        isDeleting = false;
        textIndex = (textIndex + 1) % texts.length;
        typeSpeed = 500;
    }
    
    setTimeout(typeWriter, typeSpeed);
}

// Mobile menu toggle
function toggleMobileMenu() {
    const navMenu = document.querySelector('.nav-menu');
    const hamburger = document.querySelector('.hamburger');
    
    navMenu.classList.toggle('active');
    hamburger.classList.toggle('active');
}

// Smooth scrolling for navigation links
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Close mobile menu if open
                const navMenu = document.querySelector('.nav-menu');
                navMenu.classList.remove('active');
            }
        });
    });
}

// Navbar scroll effect
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// Fade in animation on scroll
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);
    
    // Add fade-in class to elements
    const elementsToAnimate = document.querySelectorAll(
        '.section-title, .experience-card, .project-card, .skill-category, .certificate-card, .contact-item, .stat-item, .timeline-item'
    );
    
    elementsToAnimate.forEach(el => {
        el.classList.add('fade-in');
        observer.observe(el);
    });
}

// Skill bar animations
function animateSkillBars() {
    const skillBars = document.querySelectorAll('.skill-progress');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const width = progressBar.getAttribute('data-width');
                setTimeout(() => {
                    progressBar.style.width = width;
                }, 500);
            }
        });
    }, { threshold: 0.5 });
    
    skillBars.forEach(bar => observer.observe(bar));
}

// Particle effect for hero section
function createParticles() {
    const hero = document.querySelector('.hero');
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.cssText = `
            position: absolute;
            width: 2px;
            height: 2px;
            background: rgba(0, 255, 136, 0.5);
            border-radius: 50%;
            pointer-events: none;
            animation: float ${3 + Math.random() * 4}s linear infinite;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            animation-delay: ${Math.random() * 2}s;
        `;
        hero.appendChild(particle);
    }
    
    // Add particle animation keyframes
    if (!document.querySelector('#particle-style')) {
        const style = document.createElement('style');
        style.id = 'particle-style';
        style.textContent = `
            @keyframes float {
                0% { transform: translateY(0px) rotate(0deg); opacity: 0; }
                10% { opacity: 1; }
                90% { opacity: 1; }
                100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
            }
        `;
        document.head.appendChild(style);
    }
}

// Counter animation for stats
function animateCounters() {
    const counters = document.querySelectorAll('.stat-item h3');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = parseInt(counter.textContent);
                let current = 0;
                const increment = target / 50;
                const timer = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        current = target;
                        clearInterval(timer);
                    }
                    counter.textContent = Math.floor(current) + '+';
                }, 50);
            }
        });
    }, { threshold: 0.5 });
    
    counters.forEach(counter => observer.observe(counter));
}

// Project card hover effects
function initProjectHovers() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) rotateX(5deg)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) rotateX(0deg)';
        });
    });
}

// Dynamic background effect
function createDynamicBackground() {
    const hero = document.querySelector('.hero');
    
    hero.addEventListener('mousemove', (e) => {
        const rect = hero.getBoundingClientRect();
        const x = ((e.clientX - rect.left) / rect.width) * 100;
        const y = ((e.clientY - rect.top) / rect.height) * 100;
        
        hero.style.background = `
            radial-gradient(circle at ${x}% ${y}%, rgba(0, 255, 136, 0.1) 0%, transparent 50%),
            radial-gradient(circle at ${100-x}% ${100-y}%, rgba(0, 136, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 20% 80%, #120458 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, #421e7a 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, #8b5a3c 0%, transparent 50%),
            #000
        `;
    });
}

// Loading screen
function initLoadingScreen() {
    const loadingScreen = document.createElement('div');
    loadingScreen.innerHTML = `
        <div style="
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #000;
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        ">
            <div style="
                width: 50px;
                height: 50px;
                border: 3px solid rgba(0, 255, 136, 0.3);
                border-top: 3px solid #00ff88;
                border-radius: 50%;
                animation: spin 1s linear infinite;
            "></div>
            <p style="color: #00ff88; margin-top: 1rem; font-family: 'Poppins', sans-serif;">Loading Portfolio...</p>
        </div>
        <style>
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    `;
    
    document.body.appendChild(loadingScreen);
    
    window.addEventListener('load', () => {
        setTimeout(() => {
            loadingScreen.style.opacity = '0';
            loadingScreen.style.transition = 'opacity 0.5s ease';
            setTimeout(() => {
                loadingScreen.remove();
            }, 500);
        }, 1000);
    });
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize loading screen
    initLoadingScreen();
    
    // Start typing animation
    setTimeout(typeWriter, 2000);
    
    // Initialize smooth scrolling
    initSmoothScrolling();
    
    // Initialize navbar scroll effect
    initNavbarScroll();
    
    // Initialize scroll animations
    initScrollAnimations();
    
    // Initialize skill bar animations
    animateSkillBars();
    
    // Create particles
    createParticles();
    
    // Initialize counter animations
    animateCounters();
    
    // Initialize project hovers
    initProjectHovers();
    
    // Create dynamic background
    createDynamicBackground();
    
    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    if (hamburger) {
        hamburger.addEventListener('click', toggleMobileMenu);
    }
    
    // Close mobile menu when clicking on a link
    document.querySelectorAll('.nav-menu a').forEach(link => {
        link.addEventListener('click', () => {
            const navMenu = document.querySelector('.nav-menu');
            navMenu.classList.remove('active');
        });
    });
});

// Contact form functionality (if you add a contact form later)
function initContactForm() {
    const contactForm = document.querySelector('#contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Add your form submission logic here
            // This could be EmailJS, Netlify Forms, or your own backend
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;
            
            // Simulate form submission
            setTimeout(() => {
                submitBtn.textContent = 'Message Sent!';
                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    contactForm.reset();
                }, 2000);
            }, 1000);
        });
    }
}

// Performance optimization: Lazy loading for images
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Add resize handler for responsive behavior
window.addEventListener('resize', () => {
    // Close mobile menu on resize
    const navMenu = document.querySelector('.nav-menu');
    navMenu.classList.remove('active');
});

// Add keyboard navigation support
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const navMenu = document.querySelector('.nav-menu');
        navMenu.classList.remove('active');
    }
});
