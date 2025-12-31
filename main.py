import streamlit as st
from streamlit_oauth import OAuth2Component
import requests
import time
from datetime import datetime

# ========== PAGE CONFIGURATION ==========
st.set_page_config(
    page_title="AgriSmart Login",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ========== CUSTOM CSS ==========
st.markdown("""
<style>
    /* Hide sidebar completely */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Hide the default Streamlit header and footer */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    footer {
        display: none !important;
    }
    
    /* Import fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Montserrat:wght@700&family=Playfair+Display:wght@700&display=swap');
    
    /* Color variables */
    :root {
        --primary: #2E8B57;
        --primary-light: #3CB371;
        --secondary: #FFD700;
        --dark-green: #1A5D1A;
        --light-bg: #F8F9FA;
        --gradient: linear-gradient(135deg, var(--primary), var(--primary-light));
        --leaf-pattern: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><path fill="%232E8B57" fill-opacity="0.1" d="M50 0 Q75 25 50 50 Q25 75 0 50 Q25 25 50 0"/></svg>');
    }
    
    /* Base styles */
    * {
        font-family: 'Poppins', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* App container with nature-inspired background */
    .stApp {
        background: var(--light-bg) var(--leaf-pattern);
        background-size: 200px 200px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        overflow: hidden;
    }
    
    /* Decorative elements */
    .stApp::before, .stApp::after {
        content: "";
        position: absolute;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(46,139,87,0.1) 0%, rgba(255,255,255,0) 70%);
        z-index: 0;
    }
    
    .stApp::before {
        top: -150px;
        right: -150px;
    }
    
    .stApp::after {
        bottom: -150px;
        left: -150px;
    }
    
    /* Main container */
    .main-container {
        width: 100%;
        max-width: 500px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2rem;
    }
    
    /* Login container with glass morphism effect */
    .login-container {
        width: 100%;
        padding: 3rem;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 24px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.15);
        text-align: center;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,0.3);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        z-index: 1;
        overflow: hidden;
        margin-top: 1.5rem;
    }
    
    .login-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(31, 38, 135, 0.2);
    }
    
    /* Decorative border */
    .login-container::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 6px;
        background: var(--gradient);
    }
    
    /* Title styles */
    .app-title {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        background: linear-gradient(90deg, var(--dark-green), var(--primary));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
        position: relative;
        display: inline-block;
    }
    
    .app-title::after {
        content: "🌱";
        position: absolute;
        right: -40px;
        top: -10px;
        font-size: 2rem;
        animation: float 3s ease-in-out infinite;
    }
    
    /* Tagline */
    .tagline {
        font-size: 1.1rem;
        color: var(--dark-green);
        margin-bottom: 0.5rem;
        position: relative;
        font-weight: 500;
    }
    
    /* Login form header */
    .login-header {
        font-size: 1.8rem;
        color: var(--dark-green);
        margin: 1.5rem 0;
        font-weight: 600;
    }
    
    /* Login description */
    .login-desc {
        margin: 0 auto 2rem;
        color: #5a6a72;
        font-size: 1rem;
        line-height: 1.6;
        max-width: 350px;
    }
    
    /* Google button container */
    .google-btn-container {
        width: 100%;
        max-width: 300px;
        margin: 0 auto 1.5rem;
    }
    
    /* Floating animation */
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    
    /* Celebration animation */
    @keyframes celebrate {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.1); opacity: 0.9; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    .celebrate {
        animation: celebrate 1.5s ease-in-out;
    }
    
    /* Progress bar animation */
    @keyframes progress {
        0% { width: 0%; }
        100% { width: 100%; }
    }
    
    /* Footer text */
    .footer-text {
        margin-top: 2rem;
        font-size: 0.85rem;
        color: #7a8a92;
        position: relative;
        padding-top: 1rem;
    }
    
    .footer-text::before {
        content: "";
        display: block;
        width: 60px;
        height: 1px;
        background: linear-gradient(90deg, var(--primary), transparent);
        margin: 0 auto 1rem;
        opacity: 0.5;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .login-container {
            padding: 2.5rem 1.5rem;
            margin: 1rem;
        }
        
        .app-title {
            font-size: 2.8rem;
        }
        
        .app-title::after {
            right: -35px;
            top: -8px;
            font-size: 1.8rem;
        }
        
        .login-header {
            font-size: 1.5rem;
        }
        
        .login-desc {
            font-size: 0.95rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ========== OAUTH CONFIGURATION ==========
GOOGLE_CLIENT_ID = "1085314539243-s9nda1ed9saae9d2pkllngu0vo4hpkhg.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
REDIRECT_URI = "http://localhost:8501/"

# Initialize OAuth component
oauth2 = OAuth2Component(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    authorize_endpoint="https://accounts.google.com/o/oauth2/v2/auth",
    token_endpoint="https://oauth2.googleapis.com/token"
)

# ========== FUNCTIONS ==========
def show_celebration():
    """Show celebration animation and redirect to home"""
    st.balloons()
    
    # Create a container for the celebration message
    celebration = st.empty()
    with celebration.container():
        st.markdown("""
        <div class="celebrate" style="text-align: center; padding: 2rem;">
            <h1 style="color: #2E8B57; font-family: 'Playfair Display', serif; font-size: 2.5rem; margin-bottom: 1.5rem;">
                🌻 Welcome to AgriSmart!
            </h1>
            <p style="font-size: 1.2rem; margin-bottom: 2.5rem; color: #5a6a72;">
                Your farming journey begins now...
            </p>
            <div style="width: 100%; max-width: 300px; margin: 0 auto;">
                <div style="height: 6px; background: #e0e0e0; border-radius: 4px; overflow: hidden;">
                    <div style="width: 100%; height: 100%; background: linear-gradient(90deg, #2E8B57, #3CB371); 
                        border-radius: 4px; animation: progress 2.5s ease-out;">
                    </div>
                </div>
            </div>
            <div style="margin-top: 3rem;">
                <svg width="80" height="80" viewBox="0 0 100 100" style="animation: float 3s ease-in-out infinite;">
                    <path fill="#FFD700" d="M50 0 L62 38 L100 38 L69 59 L82 100 L50 75 L18 100 L31 59 L0 38 L38 38 Z"/>
                </svg>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Wait for 3 seconds before redirecting
    time.sleep(3)
    
    # Update session state and redirect
    st.session_state.logged_in = True
    st.switch_page("pages/home.py")

def show_login_page():
    """Display the login page with Google OAuth"""
    # Main container
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # App title and description
    st.markdown("""
        <h1 class="app-title">AgriSmart</h1>
        <p class="tagline">Your Intelligent Farming Companion</p>
    """, unsafe_allow_html=True)
    
    # Login container
    st.markdown("""
    <div class="login-container">
        <h2 class="login-header">Welcome Back</h2>
        <p class="login-desc">
            Access your personalized farming dashboard for crop recommendations 
            and plant disease detection
        </p>
    """, unsafe_allow_html=True)
    
    # Google OAuth button container
    st.markdown('<div class="google-btn-container">', unsafe_allow_html=True)
    
    # Google OAuth button
    result = oauth2.authorize_button(
        name="Continue with Google",
        redirect_uri=REDIRECT_URI,
        scope="openid email profile",
        key="google_login",
        use_container_width=True,
        extras_params={
            "access_type": "offline",
            "prompt": "select_account"
        }
    )
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close google-btn-container
    
    st.markdown("""
        <p class="footer-text">
            By continuing, you agree to our Terms and Privacy Policy
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container
    
    # Handle OAuth result
    if result:
        if "error" in result:
            st.error(f"Login failed: {result.get('error_description', 'Unknown error')}")
        elif "token" in result:
            st.session_state.token = result.get("token")
            st.session_state.last_auth = datetime.now().isoformat()
            show_celebration()

# ========== MAIN APP LOGIC ==========
def main():
    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    # Check if user is already logged in
    if st.session_state.logged_in and 'token' in st.session_state:
        try:
            # Verify the token is still valid
            response = requests.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {st.session_state.token['access_token']}"}
            )
            response.raise_for_status()
            st.switch_page("pages/home.py")
            return
        except requests.RequestException:
            st.session_state.clear()
            st.rerun()
    
    # Show login page if not logged in
    show_login_page()

if __name__ == "__main__":
    main()