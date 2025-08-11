import streamlit as st
import streamlit.components.v1 as components
import base64

# Set page config
st.set_page_config(
    page_title="Portfolio Website Generator",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define file contents as separate variables
HTML_FILE_CONTENT = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Scientist Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">Portfolio</div>
            <ul class="nav-menu">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <section id="home" class="hero">
        <div class="welcome-animation">
            <h1 class="welcome-text">WELCOME</h1>
            <p class="sub-welcome">to my profile</p>
        </div>
        
        <div class="hero-content">
            <div class="profile-image-container">
                <div class="profile-image-3d">
                    <div class="profile-placeholder">
                        <i class="fas fa-user"></i>
                    </div>
                </div>
            </div>
            
            <div class="hero-text">
                <h2 class="name">Your Name</h2>
                <div class="typing-animation">
                    <span class="typed-text"></span>
                    <span class="cursor">&nbsp;</span>
                </div>
                <p class="hero-description">Passionate Data Scientist turning data into insights</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn-primary">Get In Touch</a>
                    <a href="#resume" class="btn-secondary">Download CV</a>
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <p>I am a dedicated Data Scientist with expertise in machine learning and data visualization.</p>
            </div>
        </div>
    </section>

    <section id="experience" class="section">
        <div class="container">
            <h2 class="section-title">Experience</h2>
            <div class="experience-card">
                <h3>Data Scientist Intern</h3>
                <h4>Agni AI - 3 months</h4>
                <p>Worked on machine learning projects and data analysis.</p>
            </div>
        </div>
    </section>

    <section id="projects" class="section">
        <div class="container">
            <h2 class="section-title">Projects</h2>
            <div class="project-card">
                <h3>ML Prediction Model</h3>
                <p>Developed predictive models with 95% accuracy.</p>
            </div>
        </div>
    </section>

    <section id="contact" class="section">
        <div class="container">
            <h2 class="section-title">Contact</h2>
            <p>Email: your.email@example.com</p>
            <p>LinkedIn: linkedin.com/in/yourprofile</p>
        </div>
    </section>

    <script src="script.js"></script>
</body>
</html>'''

CSS_FILE_CONTENT = '''/* Portfolio Website Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background-color: #000;
    color: #fff;
    line-height: 1.6;
}

/* Navigation */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.95);
    backdrop-filter: blur(20px);
    z-index: 1000;
    padding: 1rem 0;
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
}

.nav-logo {
    font-size: 1.8rem;
    font-weight: bold;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-menu a:hover {
    color: #00ff88;
}

/* Hero Section */
.hero {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: radial-gradient(circle at 20% 80%, #120458 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, #421e7a 0%, transparent 50%),
                #000;
    padding: 2rem;
}

.welcome-animation {
    text-align: center;
    margin-bottom: 4rem;
}

.welcome-text {
    font-size: 4rem;
    font-weight: 900;
    background: linear-gradient(45deg, #00ff88, #0088ff, #ff0088);
    background-size: 300% 300%;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 3s ease-in-out infinite;
}

.sub-welcome {
    font-size: 1.5rem;
    color: #ccc;
    margin-top: 1rem;
}

@keyframes gradientShift {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
}

.hero-content {
    display: flex;
    align-items: center;
    gap: 4rem;
    max-width: 1200px;
    width: 100%;
}

.profile-image-3d {
    width: 250px;
    height: 250px;
    border-radius: 50%;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: float 6s ease-in-out infinite;
    box-shadow: 0 20px 40px rgba(0, 255, 136, 0.3);
}

.profile-placeholder {
    font-size: 6rem;
    color: #000;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

.hero-text {
    flex: 1;
}

.name {
    font-size: 3rem;
    margin-bottom: 1rem;
    background: linear-gradient(45deg, #fff, #00ff88);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.typing-animation {
    font-size: 1.5rem;
    color: #00ff88;
    margin-bottom: 2rem;
    height: 2rem;
    font-weight: 600;
}

.cursor {
    animation: blink 1s infinite;
}

@keyframes blink {
    0%, 50% { opacity: 1; }
    51%, 100% { opacity: 0; }
}

.hero-description {
    font-size: 1.2rem;
    color: #ccc;
    margin-bottom: 2rem;
}

.hero-buttons {
    display: flex;
    gap: 1rem;
}

.btn-primary, .btn-secondary {
    padding: 1rem 2rem;
    border: none;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    cursor: pointer;
}

.btn-primary {
    background: linear-gradient(45deg, #00ff88, #0088ff);
    color: #000;
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 255, 136, 0.4);
}

.btn-secondary {
    background: transparent;
    color: #00ff88;
    border: 2px solid #00ff88;
}

.btn-secondary:hover {
    background: #00ff88;
    color: #000;
}

/* Sections */
.section {
    padding: 4rem 0;
}

.section:nth-child(even) {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.section-title {
    font-size: 2.5rem;
    text-align: center;
    margin-bottom: 3rem;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.about-content {
    text-align: center;
    font-size: 1.2rem;
    color: #ccc;
    max-width: 800px;
    margin: 0 auto;
}

.experience-card, .project-card {
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    padding: 2rem;
    border-radius: 15px;
    border: 1px solid rgba(0, 255, 136, 0.1);
    margin-bottom: 2rem;
    transition: transform 0.3s ease;
}

.experience-card:hover, .project-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0, 255, 136, 0.1);
}

.experience-card h3, .project-card h3 {
    color: #00ff88;
    margin-bottom: 0.5rem;
}

.experience-card h4 {
    color: #0088ff;
    margin-bottom: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-content {
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }
    
    .profile-image-3d {
        width: 200px;
        height: 200px;
    }
    
    .welcome-text {
        font-size: 3rem;
    }
    
    .name {
        font-size: 2rem;
    }
    
    .nav-menu {
        display: none;
    }
}'''

JS_FILE_CONTENT = '''// Portfolio JavaScript
console.log("Portfolio loaded!");

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

// Smooth scrolling for navigation
document.addEventListener('DOMContentLoaded', function() {
    // Start typing animation
    setTimeout(typeWriter, 1000);
    
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add scroll animation for cards
    const cards = document.querySelectorAll('.experience-card, .project-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
});'''

