import streamlit as st
from streamlit_option_menu import option_menu
import pin_code_correction
import handwritten_recognition
import voice_address_recognition
import address_parsing
import wrong_pincode_storage
import route_optimization
import dashboard
import home
import home1

# Set page configuration
st.set_page_config(page_title="Postal System Optimizer", page_icon=":mailbox:", layout="wide")

# CSS for dark theme
def render_dark_theme():
    st.markdown("""
        <style>
        /* Set the background color for the whole page */
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }

        /* Set the background color and style for the header */
        .header {
            background-color: #444444;
            padding: 10px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        /* Style for the navigation links in the header */
        .header a {
            color: white;
            text-decoration: none;
            font-size: 18px;
            padding: 8px 16px;
            transition: background-color 0.3s, color 0.3s;
            border-radius: 5px;
        }

        .header a:hover {
            background-color: #55C667;
            color: white;
        }

        /* Sidebar and option menu background styling */
        .css-1d391kg {  /* Sidebar */
            background-color: #1e1e1e !important;
        }

        /* Button styling */
        .stButton>button {
            background-color: #00aaff;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 12em;
            margin: 30px auto;
            display: block;
        }

        .stButton>button:hover {
            background-color: #55C667;
            color: white;
        }

        /* Main page link text styling */
        h1, h2, h3, h4, h5, h6, p, div, span {
            color: white !important;  /* Ensures text is white */
        }
        
        /* Custom styling for any other divs or containers */
        .block-container {
            background-color: #1e1e1e;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# Function to render the header and sidebar
def render_header():
    st.markdown("""
        <div class="header">
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact Us</a>
        </div>
    """, unsafe_allow_html=True)

# Function to render the main application with sidebar
def run_main_app():
    render_header()

    with st.sidebar:
        selected_page = option_menu(
            menu_title='Postal System Optimization',  # Title for the sidebar
            options=[
                'Home', 'Validate Pincode', 'Handwritten Address Recognition', 'Voice-Based Address Recognition', 
                'Address Parsing', 'Wrong Pincode Storage', 'Route Optimization', 'Dashboard'
            ],  # Menu options
            icons=['house', 'check-circle', 'pencil', 'mic', 'folder', 'file-earmark-excel', 'map', 'graph-up'],  # Corresponding icons
            menu_icon='box',  # Sidebar icon
            default_index=0,  # Default selected menu
            styles={
                "container": {"padding": "5px", "background-color": '#1e1e1e'},
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {
                    "color": "white", 
                    "font-size": "18px", 
                    "text-align": "left", 
                    "margin": "0px", 
                    "--hover-color": "#444444"
                },
                "nav-link-selected": {"background-color": "#00aaff"},
            }
        )

    # Linking pages based on selection
    if selected_page == 'Home':
        home1.app()  # Calls the different home function
    elif selected_page == 'Validate Pincode':
        pin_code_correction.app()  # Call the function from pin_code_correction.py
    elif selected_page == 'Handwritten Address Recognition':
        handwritten_recognition.app()  # Call the function from handwritten_recognition.py
    elif selected_page == 'Voice-Based Address Recognition':
        voice_address_recognition.app()  # Call the function from voice_address_recognition.py
    elif selected_page == 'Address Parsing':
        address_parsing.app()  # Call the function from address_parsing.py
    elif selected_page == 'Wrong Pincode Storage':
        wrong_pincode_storage.app()  # Call the function from wrong_pincode_storage.py
    elif selected_page == 'Route Optimization':
        route_optimization.app()  # Call the function from route_optimization.py
    elif selected_page == 'Dashboard':
        dashboard.app()  # Call the function from dashboard.py

# Main flow control
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Check if the session is still on the home page or if the user clicked on a button
if st.session_state["page"] == "home":
    next_action = home.home_page()
    if next_action == "validate":
        st.session_state["page"] = "main"  # Change session state to the main app
elif st.session_state["page"] == "main":
    render_dark_theme()  # Call the dark theme function
    run_main_app()
