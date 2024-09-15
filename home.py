import streamlit as st

# Function to render the sticky header
def render_header():
    st.markdown("""
        <style>
        body {background-color: #121212;}
        h1 {color: #ffffff; font-family: 'Helvetica'; text-align: center;}
        
        /* Header Styling */
        .header {
            background-color: #1c1c1c;
            padding: 10px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 1000;
        }
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

        /* Button Styling */
        .stButton>button {
            background-color: #02ab21;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 10em;
            margin: 30px auto;
            display: block;
        }
        .stButton>button:hover {
            background-color: #55C667;
            color: white;
        }
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Sticky Header content
    st.markdown("""
        <div class="header">
            <a href="#">About Us</a>
            <a href="#">Our Accomplishments</a>
            <a href="#">People</a>
        </div>
    """, unsafe_allow_html=True)

# Home page function
def home_page():
    render_header()  # Add the sticky header to the home page

    # Display the logo with reduced size using st.image
    st.image(r"D:\Rakathon\dashboard-ecommerce\dashboard\nangara.png", 
             caption="Welcome to Nangara! Your Postal System Optimizer", 
             use_column_width=True)  # Reduced the image size

    # Button for 'Validate Pincode'
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Validate Pincode"):
        return "validate"  # Signal to switch to the main page functionality
    st.markdown('</div>', unsafe_allow_html=True)

    return None
