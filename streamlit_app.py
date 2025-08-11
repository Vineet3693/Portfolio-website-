
import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Portfolio Website Preview",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the complete file contents
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Scientist Portfolio</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Embedded CSS will go here */
        {CSS_CONTENT}
    </style>
</head>
<body>
    <!-- Navigation -->
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
                <li><a href="#certificates">Certificates</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Welcome Animation Section -->
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
                <p class="hero-description">Passionate about turning data into insights and building intelligent solutions for the future</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn-primary">Get In Touch</a>
                    <a href="#resume" class="btn-secondary">Download CV</a>
                </div>
            </div>
        </div>
        
        <div class="scroll-indicator">
            <div class="scroll-arrow"></div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>I am a dedicated Data Scientist with a passion for extracting meaningful insights from complex datasets. With expertise in machine learning, statistical analysis, and data visualization, I strive to solve real-world problems through data-driven solutions.</p>
                    <div class="career-goals">
                        <h3>Career Goals</h3>
                        <p>Looking forward to advancing my career in AI and Machine Learning, focusing on developing innovative solutions that make a positive impact on society.</p>
                    </div>
                </div>
                <div class="about-stats">
                    <div class="stat-item">
                        <h3>2+</h3>
                        <p>Years Experience</p>
                    </div>
                    <div class="stat-item">
                        <h3>15+</h3>
                        <p>Projects Completed</p>
                    </div>
                    <div class="stat-item">
                        <h3>5+</h3>
                        <p>Technologies</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="section">
        <div class="container">
            <h2 class="section-title">Education</h2>
            <div class="education-timeline">
                <div class="timeline-item">
                    <div class="timeline-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <div class="timeline-content">
                        <h3>Bachelor's Degree in Computer Science</h3>
                        <h4>University Name</h4>
                        <span class="timeline-date">2020 - 2024</span>
                        <p>Specialized in Data Science and Machine Learning with focus on statistical analysis and predictive modeling.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="section">
        <div class="container">
            <h2 class="section-title">Experience & Internships</h2>
            <div class="experience-grid">
                <div class="experience-card">
                    <div class="card-header">
                        <h3>Data Scientist Intern</h3>
                        <span class="duration">3 months</span>
                    </div>
                    <h4>Agni AI</h4>
                    <p>Worked on machine learning projects, developed predictive models, and gained hands-on experience with data analysis.</p>
                    <ul class="experience-list">
                        <li>Implemented machine learning algorithms using Python and TensorFlow</li>
                        <li>Performed data preprocessing and feature engineering</li>
                        <li>Conducted model evaluation and optimization</li>
                    </ul>
                    <div class="tech-stack">
                        <span class="tech-tag">Python</span>
                        <span class="tech-tag">TensorFlow</span>
                        <span class="tech-tag">Pandas</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
        <div class="container">
            <h2 class="section-title">Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-brain"></i>
                    </div>
                    <div class="project-content">
                        <h3>Machine Learning Prediction Model</h3>
                        <p>Developed a comprehensive ML model for predictive analytics using ensemble methods.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Scikit-learn</span>
                            <span class="tech-tag">Pandas</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section">
        <div class="container">
            <h2 class="section-title">Technical Skills</h2>
            <div class="skills-container">
                <div class="skill-category">
                    <h3><i class="fas fa-code"></i> Programming Languages</h3>
                    <div class="skills-list">
                        <div class="skill-item">
                            <span class="skill-name">Python</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="90%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">SQL</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="85%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <h2 class="section-title">Contact Me</h2>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <h3>Email</h3>
                        <p>your.email@example.com</p>
                    </div>
                    <div class="contact-item">
                        <h3>LinkedIn</h3>
                        <p>linkedin.com/in/yourprofile</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script>
        {JS_CONTENT}
    </script>
</body>
</html>"""

CSS_CONTENT = """
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Poppins', sans-serif;
    background-color: #000;
    color: #fff;
    overflow-x: hidden;
    line-height: 1.6;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

/* Navigation Styles */
.navbar {
    position: fixed;
    top: 0;
    width: 100%;
    background: rgba(0, 0, 0, 0.95);
    backdrop-filter: blur(20px);
    z-index: 1000;
    padding: 1rem 0;
    transition: all 0.3s ease;
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
    gap: 2.5rem;
}

.nav-menu a {
    color: #fff;
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s ease;
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
    position: relative;
    padding: 2rem;
}

.welcome-animation {
    text-align: center;
    margin-bottom: 4rem;
    animation: fadeInDown 1.5s ease-out;
}

.welcome-text {
    font-size: clamp(3rem, 8vw, 6rem);
    font-weight: 900;
    background: linear-gradient(45deg, #00ff88, #0088ff, #ff0088, #ffff00);
    background-size: 400% 400%;
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientShift 4s ease-in-out infinite;
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

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-content {
    display: flex;
    align-items: center;
    gap: 4rem;
    max-width: 1200px;
    width: 100%;
}

.profile-image-3d {
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: float 6s ease-in-out infinite;
    box-shadow: 0 20px 40px rgba(0, 255, 136, 0.3);
}

.profile-placeholder {
    font-size: 8rem;
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
    font-size: clamp(2.5rem, 5vw, 4rem);
    margin-bottom: 1rem;
    background: linear-gradient(45deg, #fff, #00ff88);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.typing-animation {
    font-size: 1.8rem;
    color: #00ff88;
    margin-bottom: 2rem;
    height: 2.5rem;
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
    line-height: 1.8;
    margin-bottom: 2.5rem;
}

.hero-buttons {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
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
    transform: translateY(-3px);
}

.scroll-indicator {
    position: absolute;
    bottom: 2rem;
    left: 50%;
    transform: translateX(-50%);
    animation: bounce 2s infinite;
}

.scroll-arrow {
    width: 2px;
    height: 40px;
    background: linear-gradient(to bottom, #00ff88, transparent);
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}

/* Section Styles */
.section {
    padding: 6rem 0;
    position: relative;
}

.section:nth-child(even) {
    background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
}

.section-title {
    font-size: 3rem;
    text-align: center;
    margin-bottom: 4rem;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* About Section */
.about-content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 4rem;
    align-items: center;
}

.about-text p {
    font-size: 1.1rem;
    color: #ccc;
    margin-bottom: 2rem;
    line-height: 1.8;
}

.career-goals h3 {
    color: #00ff88;
    margin-bottom: 1rem;
    font-size: 1.5rem;
}

.about-stats {
    display: grid;
    gap: 2rem;
}

.stat-item {
    text-align: center;
    padding: 2rem;
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    border-radius: 15px;
    border: 1px solid rgba(0, 255, 136, 0.1);
    transition: all 0.3s ease;
}

.stat-item:hover {
    transform: translateY(-5px);
    border-color: rgba(0, 255, 136, 0.3);
}

.stat-item h3 {
    font-size: 2.5rem;
    color: #00ff88;
    margin-bottom: 0.5rem;
}

/* Timeline */
.education-timeline {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
}

.timeline-item {
    display: flex;
    align-items: flex-start;
    gap: 2rem;
    margin-bottom: 3rem;
}

.timeline-icon {
    width: 60px;
    height: 60px;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: #000;
    flex-shrink: 0;
}

.timeline-content {
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    padding: 2rem;
    border-radius: 15px;
    border: 1px solid rgba(0, 255, 136, 0.1);
    flex: 1;
}

.timeline-content h3 {
    color: #00ff88;
    margin-bottom: 0.5rem;
}

.timeline-date {
    background: rgba(0, 255, 136, 0.1);
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
    color: #00ff88;
    display: inline-block;
    margin-bottom: 1rem;
}

/* Experience */
.experience-grid {
    display: grid;
    gap: 3rem;
}

.experience-card {
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    border-radius: 20px;
    padding: 2.5rem;
    border: 1px solid rgba(0, 255, 136, 0.1);
    transition: all 0.3s ease;
}

.experience-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 20px 40px rgba(0, 255, 136, 0.2);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.experience-card h3 {
    color: #00ff88;
    font-size: 1.4rem;
}

.duration {
    background: rgba(0, 136, 255, 0.1);
    color: #0088ff;
    padding: 0.3rem 1rem;
    border-radius: 20px;
    font-size: 0.9rem;
}

.experience-list {
    list-style: none;
    margin: 1.5rem 0;
}

.experience-list li {
    position: relative;
    padding-left: 2rem;
    margin-bottom: 1rem;
    color: #ccc;
}

.experience-list li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: #00ff88;
}

.tech-stack {
    display: flex;
    flex-wrap: wrap;
    gap: 0.8rem;
    margin-top: 1.5rem;
}

.tech-tag {
    background: rgba(0, 255, 136, 0.1);
    color: #00ff88;
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    border: 1px solid rgba(0, 255, 136, 0.2);
}

/* Projects */
.projects-grid {
    display: grid;
    gap: 2.5rem;
}

.project-card {
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    border-radius: 20px;
    overflow: hidden;
    border: 1px solid rgba(0, 255, 136, 0.1);
    transition: all 0.3s ease;
}

.project-card:hover {
    transform: translateY(-10px);
}

.project-image {
    height: 200px;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    color: #000;
}

.project-content {
    padding: 2rem;
}

.project-content h3 {
    color: #00ff88;
    margin-bottom: 1rem;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1.5rem;
}

/* Skills */
.skills-container {
    display: grid;
    gap: 3rem;
}

.skill-category {
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    padding: 2.5rem;
    border-radius: 20px;
    border: 1px solid rgba(0, 255, 136, 0.1);
}

.skill-category h3 {
    color: #00ff88;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.skills-list {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.skill-item {
    display: flex;
    flex-direction: column;
    gap: 0.8rem;
}

.skill-name {
    color: #fff;
    font-weight: 500;
}

.skill-bar {
    height: 8px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 4px;
    overflow: hidden;
}

.skill-progress {
    height: 100%;
    background: linear-gradient(45deg, #00ff88, #0088ff);
    border-radius: 4px;
    width: 0;
    transition: width 2s ease-in-out;
}

/* Contact */
.contact-content {
    max-width: 800px;
    margin: 0 auto;
}

.contact-info {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}

.contact-item {
    background: linear-gradient(135deg, #1a1a1a, #2a2a2a);
    padding: 2rem;
    border-radius: 15px;
    border: 1px solid rgba(0, 255, 136, 0.1);
    text-align: center;
    transition: all 0.3s ease;
}

.contact-item:hover {
    transform: translateY(-5px);
    border-color: rgba(0, 255, 136, 0.3);
}

.contact-item h3 {
    color: #00ff88;
    margin-bottom: 1rem;
}

/* Responsive */
@media (max-width: 768px) {
    .hero-content {
        flex-direction: column;
        text-align: center;
        gap: 2rem;
    }
    
    .about-content {
        grid-template-columns: 1fr;
    }
    
    .profile-image-3d {
        width: 200px;
        height: 200px;
    }
    
    .nav-menu {
        display: none;
    }
}
"""

JS_CONTENT = """
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

// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Skill bar animations
function animateSkillBars() {
    const skillBars = document.querySelectorAll('.skill-progress');
    skillBars.forEach(bar => {
        const width = bar.getAttribute('data-width');
        setTimeout(() => {
            bar.style.width = width;
        }, 1000);
    });
}

// Initialize everything
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(typeWriter, 1000);
    setTimeout(animateSkillBars, 2000);
});
"""

def create_download_link(content, filename, mime_type):
    """Create a download link for file content"""
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:{mime_type};base64,{b64}" download="{filename}" style="text-decoration: none; background: linear-gradient(45deg, #00ff88, #0088ff); color: black; padding: 0.5rem 1rem; border-radius: 25px; font-weight: 600;">📥 Download {filename}</a>'

def main():
    st.title("🌟 Data Scientist Portfolio Website")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.title("📁 Portfolio Files")
    
    # Main tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🌐 Live Preview", "📄 HTML File", "🎨 CSS File", "⚡ JavaScript File"])
    
    with tab1:
        st.subheader("🚀 Live Website Preview")
        st.info("👆 This is how your portfolio website will look when deployed!")
        
        # Create the complete HTML with embedded CSS and JS
        complete_html = HTML_CONTENT.format(
            CSS_CONTENT=CSS_CONTENT,
            JS_CONTENT=JS_CONTENT
        )
        
        # Display the website using Streamlit components
        components.html(complete_html, height=800, scrolling=True)
        
        # Download all files section
        st.markdown("---")
        st.subheader("📦 Download Complete Website")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            # HTML file (separate files version)
            html_separate = '''<!DOCTYPE html>
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
    <!-- Navigation -->
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
                <li><a href="#certificates">Certificates</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <!-- Welcome Animation Section -->
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
                <p class="hero-description">Passionate about turning data into insights and building intelligent solutions for the future</p>
                <div class="hero-buttons">
                    <a href="#contact" class="btn-primary">Get In Touch</a>
                    <a href="#resume" class="btn-secondary">Download CV</a>
                </div>
            </div>
        </div>
        
        <div class="scroll-indicator">
            <div class="scroll-arrow"></div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>I am a dedicated Data Scientist with a passion for extracting meaningful insights from complex datasets. With expertise in machine learning, statistical analysis, and data visualization, I strive to solve real-world problems through data-driven solutions.</p>
                    <div class="career-goals">
                        <h3>Career Goals</h3>
                        <p>Looking forward to advancing my career in AI and Machine Learning, focusing on developing innovative solutions that make a positive impact on society. I aim to become a leading expert in deep learning and computer vision technologies.</p>
                    </div>
                </div>
                <div class="about-stats">
                    <div class="stat-item">
                        <h3>2+</h3>
                        <p>Years Experience</p>
                    </div>
                    <div class="stat-item">
                        <h3>15+</h3>
                        <p>Projects Completed</p>
                    </div>
                    <div class="stat-item">
                        <h3>5+</h3>
                        <p>Technologies</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education" class="section">
        <div class="container">
            <h2 class="section-title">Education</h2>
            <div class="education-timeline">
                <div class="timeline-item">
                    <div class="timeline-icon">
                        <i class="fas fa-graduation-cap"></i>
                    </div>
                    <div class="timeline-content">
                        <h3>Bachelor's Degree in Computer Science</h3>
                        <h4>University Name</h4>
                        <span class="timeline-date">2020 - 2024</span>
                        <p>Specialized in Data Science and Machine Learning with a focus on statistical analysis and predictive modeling. Maintained a strong academic record with relevant coursework in algorithms, databases, and artificial intelligence.</p>
                    </div>
                </div>
                <div class="timeline-item">
                    <div class="timeline-icon">
                        <i class="fas fa-certificate"></i>
                    </div>
                    <div class="timeline-content">
                        <h3>Data Science Certification</h3>
                        <h4>Online Platform</h4>
                        <span class="timeline-date">2023</span>
                        <p>Completed comprehensive certification in data science covering machine learning, statistics, and data visualization techniques.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience Section -->
    <section id="experience" class="section">
        <div class="container">
            <h2 class="section-title">Experience & Internships</h2>
            <div class="experience-grid">
                <div class="experience-card">
                    <div class="card-header">
                        <h3>Data Scientist Intern</h3>
                        <span class="duration">3 months</span>
                    </div>
                    <h4>Agni AI</h4>
                    <p>Worked on cutting-edge machine learning projects, developed predictive models, and gained hands-on experience with advanced data analysis and visualization tools.</p>
                    <ul class="experience-list">
                        <li>Implemented machine learning algorithms using Python and TensorFlow</li>
                        <li>Performed data preprocessing and feature engineering on large datasets</li>
                        <li>Conducted model evaluation and optimization for improved accuracy</li>
                        <li>Collaborated with cross-functional teams on AI-driven solutions</li>
                    </ul>
                    <div class="tech-stack">
                        <span class="tech-tag">Python</span>
                        <span class="tech-tag">TensorFlow</span>
                        <span class="tech-tag">Pandas</span>
                        <span class="tech-tag">NumPy</span>
                    </div>
                </div>
                
                <div class="experience-card">
                    <div class="card-header">
                        <h3>Data Analyst & Developer Intern</h3>
                        <span class="duration">2 months</span>
                    </div>
                    <h4>Tech Innovation Company</h4>
                    <p>Focused on web development and data analysis, creating interactive dashboards and data-driven applications for business intelligence.</p>
                    <ul class="experience-list">
                        <li>Developed responsive web applications using modern frameworks</li>
                        <li>Created interactive dashboards for data visualization</li>
                        <li>Optimized database queries and improved system performance</li>
                        <li>Implemented automated reporting systems</li>
                    </ul>
                    <div class="tech-stack">
                        <span class="tech-tag">JavaScript</span>
                        <span class="tech-tag">React</span>
                        <span class="tech-tag">SQL</span>
                        <span class="tech-tag">Tableau</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
        <div class="container">
            <h2 class="section-title">Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-brain"></i>
                    </div>
                    <div class="project-content">
                        <h3>Machine Learning Prediction Model</h3>
                        <p>Developed a comprehensive machine learning model for predictive analytics using ensemble methods. Achieved 95% accuracy in classification tasks with real-world datasets.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Scikit-learn</span>
                            <span class="tech-tag">Pandas</span>
                            <span class="tech-tag">Matplotlib</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="project-link">
                                <i class="fab fa-github"></i> GitHub
                            </a>
                            <a href="#" class="project-link">
                                <i class="fas fa-external-link-alt"></i> Live Demo
                            </a>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div class="project-content">
                        <h3>Data Analytics Dashboard</h3>
                        <p>Created an interactive web-based dashboard for business intelligence with real-time data visualization and automated reporting capabilities.</p>
                        <div class="project-tech">
                            <span class="tech-tag">Python</span>
                            <span class="tech-tag">Streamlit</span>
                            <span class="tech-tag">Plotly</span>
                            <span class="tech-tag">SQL</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="project-link">
                                <i class="fab fa-github"></i> GitHub
                            </a>
                            <a href="#" class="project-link">
                                <i class="fas fa-external-link-alt"></i> Live Demo
                            </a>
                        </div>
                    </div>
                </div>
                
                <div class="project-card">
                    <div class="project-image">
                        <i class="fas fa-robot"></i>
                    </div>
                    <div class="project-content">
                        <h3>AI-Powered Web Application</h3>
                        <p>Full-stack web application integrating machine learning models with modern web technologies for automated decision-making processes.</p>
                        <div class="project-tech">
                            <span class="tech-tag">React</span>
                            <span class="tech-tag">Node.js</span>
                            <span class="tech-tag">TensorFlow.js</span>
                            <span class="tech-tag">MongoDB</span>
                        </div>
                        <div class="project-links">
                            <a href="#" class="project-link">
                                <i class="fab fa-github"></i> GitHub
                            </a>
                            <a href="#" class="project-link">
                                <i class="fas fa-external-link-alt"></i> Live Demo
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Technical Skills Section -->
    <section id="skills" class="section">
        <div class="container">
            <h2 class="section-title">Technical Skills</h2>
            <div class="skills-container">
                <div class="skill-category">
                    <h3><i class="fas fa-code"></i> Programming Languages</h3>
                    <div class="skills-list">
                        <div class="skill-item">
                            <span class="skill-name">Python</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="90%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">R</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="85%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">SQL</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="88%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">JavaScript</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="82%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3><i class="fas fa-brain"></i> Machine Learning</h3>
                    <div class="skills-list">
                        <div class="skill-item">
                            <span class="skill-name">TensorFlow</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="87%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">PyTorch</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="80%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Scikit-learn</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="92%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Keras</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="85%"></div>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="skill-category">
                    <h3><i class="fas fa-chart-bar"></i> Data Visualization</h3>
                    <div class="skills-list">
                        <div class="skill-item">
                            <span class="skill-name">Tableau</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="88%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Power BI</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="83%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Matplotlib</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="90%"></div>
                            </div>
                        </div>
                        <div class="skill-item">
                            <span class="skill-name">Plotly</span>
                            <div class="skill-bar">
                                <div class="skill-progress" data-width="85%"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Certificates Section -->
    <section id="certificates" class="section">
        <div class="container">
            <h2 class="section-title">Certificates</h2>
            <div class="certificates-grid">
                <div class="certificate-card">
                
            <h3>Data Science Professional Certificate</h3>
                    <p>IBM - Coursera</p>
                    <span class="cert-date">2024</span>
                </div>
                
                <div class="certificate-card">
                    <h3>Machine Learning Specialization</h3>
                    <p>Stanford University - Coursera</p>
                    <span class="cert-date">2023</span>
                </div>
                
                <div class="certificate-card">
                    <h3>Python for Data Science</h3>
                    <p>University of Michigan</p>
                    <span class="cert-date">2023</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Resume Download Section -->
    <section id="resume" class="section">
        <div class="container">
            <h2 class="section-title">Resume</h2>
            <div class="resume-download">
                <p>Download my complete resume for more details</p>
                <a href="resume.pdf" class="download-btn" download>
                    <span>Download Resume</span>
                </a>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <div class="container">
            <h2 class="section-title">Contact Me</h2>
            <div class="contact-content">
                <div class="contact-info">
                    <div class="contact-item">
                        <h3>Email</h3>
                        <p>your.email@example.com</p>
                    </div>
                    <div class="contact-item">
                        <h3>Phone</h3>
                        <p>+1 (555) 123-4567</p>
                    </div>
                    <div class="contact-item">
                        <h3>LinkedIn</h3>
                        <p>linkedin.com/in/yourprofile</p>
                    </div>
                    <div class="contact-item">
                        <h3>GitHub</h3>
                        <p>github.com/yourusername</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <script src="script.js"></script>
</body>
</html>'''
            
        
   


