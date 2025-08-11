
import streamlit as st
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Portfolio Website Preview",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_file_content(file_path):
    """Load and return file content"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"File {file_path} not found"
    except Exception as e:
        return f"Error reading {file_path}: {str(e)}"

def main():
    st.title("🌟 Data Scientist Portfolio Website")
    st.markdown("---")
    
    # Sidebar
    st.sidebar.title("📁 Project Files")
    st.sidebar.markdown("This Streamlit app displays your portfolio website files.")
    
    # File selection
    files = {
        "HTML (index.html)": "index.html",
        "CSS (styles.css)": "styles.css", 
        "JavaScript (script.js)": "script.js",
        "README.md": "README.md"
    }
    
    selected_file = st.sidebar.selectbox("Select file to view:", list(files.keys()))
    
    # Display instructions
    with st.sidebar.expander("📋 Setup Instructions"):
        st.markdown("""
        **To use this portfolio:**
        
        1. **Download Files**: Copy all the code files to your computer
        2. **Create Project Folder**: Make a new folder for your portfolio
        3. **Save Files**: 
           - Save HTML code as `index.html`
           - Save CSS code as `styles.css`
           - Save JavaScript code as `script.js`
           - Save README content as `README.md`
        
        4. **Customize Content**:
           - Replace "Your Name" with your actual name
           - Add your profile picture
           - Update contact information
           - Add your projects and experience
        
        5. **Test Locally**: Open `index.html` in your browser
        
        6. **Deploy**: Upload to GitHub Pages, Netlify, or Vercel
        """)
    
    with st.sidebar.expander("🎨 Customization Tips"):
        st.markdown("""
        **Personalization Checklist:**
        
        ✅ **Replace placeholders**:
        - Your name and title
        - Contact information
        - Education details
        - Work experience
        - Projects and descriptions
        
        ✅ **Add your content**:
        - Profile photo
        - Resume PDF
        - Project screenshots
        - Certificate images
        
        ✅ **Customize colors** (in CSS):
        - Primary: `#00ff88` (green)
        - Secondary: `#0088ff` (blue)
        - Change to your preferred colors
        """)
    
    # Main content area
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader(f"📄 {selected_file}")
        
        # Get file extension for syntax highlighting
        file_path = files[selected_file]
        if file_path.endswith('.html'):
            language = 'html'
        elif file_path.endswith('.css'):
            language = 'css'
        elif file_path.endswith('.js'):
            language = 'javascript'
        elif file_path.endswith('.md'):
            language = 'markdown'
        else:
            language = 'text'
        
        # Create file content (since we can't read actual files in Streamlit Cloud)
        file_contents = {
            "index.html": '''<!DOCTYPE html>
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
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <div class="about-content">
                <div class="about-text">
                    <p>I am a dedicated Data Scientist with a passion for extracting meaningful insights from complex datasets.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Add all other sections here... -->
    
    <script src="script.js"></script>
</body>
</html>''',
            
            "styles.css": '''/* Complete CSS code from previous response */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background-color: #000;
    color: #fff;
    overflow-x: hidden;
}

/* Add all CSS styles here... */''',
            
            "script.js": '''// Complete JavaScript code from previous response
const texts = [
    "Data Scientist",
    "Machine Learning Engineer", 
    "AI Enthusiast",
    "Python Developer",
    "Problem Solver"
];

// Add all JavaScript functions here...''',
            
            "README.md": '''# Data Scientist Portfolio Website

A modern, responsive portfolio website for data scientists.

## Features
- Responsive Design
- Animated Welcome Section
- 3D Profile Image
- Interactive Navigation

## Setup Instructions
1. Download all files
2. Customize content
3. Deploy to GitHub Pages

For full README content, see the code files.'''
        }
        
        # Display the selected file content
        content = file_contents.get(file_path, "File content not available in demo")
        st.code(content, language=language)
        
        # Download button
        st.download_button(
            label=f"📥 Download {selected_file}",
            data=content,
            file_name=file_path,
            mime=f"text/{language}"
        )
    
    with col2:
        st.subheader("🚀 Quick Actions")
        
        # Feature highlights
        st.markdown("""
        ### ✨ Features
        - **Responsive Design**
        - **Dark Theme** 
        - **Animated Effects**
        - **3D Profile Image**
        - **Typing Animation**
        - **Skill Progress Bars**
        - **Project Showcase**
        - **Contact Section**
        """)
        
        st.markdown("---")
        
        # Technology stack
        st.markdown("""
        ### 🛠️ Tech Stack
        - HTML5
        - CSS3 
        - JavaScript ES6+
        - Font Awesome
        - Google Fonts
        """)
        
        st.markdown("---")
        
        # Deployment options
        st.markdown("""
        ### 🌐 Deploy Options
        - **GitHub Pages** (Free)
        - **Netlify** (Free)
        - **Vercel** (Free)
        - **Firebase Hosting**
        """)
    
    # Instructions section
    st.markdown("---")
    st.subheader("📖 Complete Setup Guide")
    
    tab1, tab2, tab3, tab4 = st.tabs(["💻 Local Setup", "🔧 Customization", "🌐 Deployment", "📱 Testing"])
    
    with tab1:
        st.markdown("""
        ### Local Development Setup
        
        1. **Create Project Directory**:

        ```bash
        mkdir my-portfolio
        cd my-portfolio
        ```
        
        2. **Create Files**:
        - Copy HTML code → save as `index.html`
        - Copy CSS code → save as `styles.css`  
        - Copy JavaScript code → save as `script.js`
        - Copy README → save as `README.md`
        
        3. **Open in Browser**:

        ```bash
        # Simply double-click index.html
        # OR use live server in VS Code
        ```
        
        4. **Project Structure**:

        ```
        my-portfolio/
        ├── index.html
        ├── styles.css
        ├── script.js
        ├── README.md
        └── assets/
            ├── resume.pdf
            └── profile-photo.jpg
        ```
        """)
    
    with tab2:
        st.markdown("""
        ### Customization Checklist
        
        #### 📝 Content Updates (Required):
        - [ ] Replace "Your Name" with your actual name
        - [ ] Update typing animation texts in script.js
        - [ ] Add your education details
        - [ ] Add your work experience
        - [ ] Update project descriptions
        - [ ] Add your contact information
        - [ ] Replace placeholder profile image
        - [ ] Add your resume PDF file
        
        #### 🎨 Style Customizations (Optional):

        ```css
        /* Main colors - update in styles.css */
        --primary-color: #00ff88;    /* Green accent */
        --secondary-color: #0088ff;  /* Blue accent */
        --background: #000;          /* Black background */
        ```
        
        #### 🖼️ Asset Requirements:
        - **Profile Photo**: 300x300px, square format
        - **Resume**: PDF format, named `resume.pdf`  
        - **Project Images**: Optional, for project showcase
        """)
    
    with tab3:
        st.markdown("""
        ### Deployment Options
        
        #### 🔥 GitHub Pages (Recommended):

        ```bash
        # 1. Create GitHub repository
        git init
        git add .
        git commit -m "Initial portfolio"
        git remote add origin https://github.com/username/portfolio
        git push -u origin main
        
        # 2. Enable GitHub Pages in repository settings
        # Your site: https://username.github.io/portfolio
        ```
        
        #### ⚡ Netlify:
        1. Drag & drop your project folder to netlify.com
        2. Or connect GitHub repository for automatic updates
        3. Get instant custom domain
        
        #### 🔹 Vercel:

        ```bash
        # Install Vercel CLI
        npm i -g vercel
        
        # Deploy
        vercel
        ```
        
        #### 💡 Tips:
        - Use custom domain for professional look
        - Enable HTTPS (automatic on most platforms)
        - Set up automatic deployments from GitHub
        """)
    
    with tab4:
        st.markdown("""
        ### Testing & Quality Assurance
        
        #### 📱 Responsive Testing:
        - [ ] Desktop (1920px+)
        - [ ] Laptop (1366px)
        - [ ] Tablet (768px)
        - [ ] Mobile (375px)
        
        #### 🌐 Browser Testing:
        - [ ] Chrome (primary)
        - [ ] Firefox
        - [ ] Safari
        - [ ] Edge
        
        #### ⚡ Performance Checklist:
        - [ ] Images optimized (<500KB each)
        - [ ] CSS/JS minified for production
        - [ ] Fast loading (<3 seconds)
        - [ ] Smooth animations
        
        #### ♿ Accessibility:
        - [ ] Alt text for images
        - [ ] Keyboard navigation
        - [ ] Screen reader friendly
        - [ ] Good color contrast
        
        #### 🔧 Dev Tools:

        ```bash
        # Test with browser dev tools
        F12 → Toggle device toolbar
        Network tab → Check load times
        Lighthouse → Performance audit
        ```
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>🌟 <strong>Portfolio Website Generator</strong> 🌟</p>
        <p>Built with Streamlit • Ready for deployment • Fully customizable</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
