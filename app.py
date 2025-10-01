import streamlit as st

# Initialize session state for navigation
if 'category' not in st.session_state:
    st.session_state.category = "Home"

# App Title
st.title("MathBook App: Trigonometry & Geometry for High Schoolers")
st.markdown("""
Welcome to the MathBook App! Explore Trigonometry and Geometry through interactive visualizations, calculators, quizzes, and more. 
Select a category below to begin learning.
""")

# Sidebar Navigation with Icons
st.sidebar.header("Select Category")
categories = {
    "🏠 Home": "Home",
    "📐 Trigonometry": "Trigonometry",
    "🔲 Geometry": "Geometry"
}

for icon_label, category in categories.items():
    if st.sidebar.button(icon_label, key=category):
        st.session_state.category = category

# Home Page
if st.session_state.category == "Home":
    st.header("Welcome to MathBook")
    st.markdown("""
    Choose a category from the sidebar to explore:
    - **Trigonometry**: Dive into angles, triangles, and waves with visualizations, calculators, and real-world applications.
    - **Geometry**: Learn about shapes, areas, volumes, and transformations with interactive tools.
    """)

# Trigonometry Navigation
elif st.session_state.category == "Trigonometry":
    st.header("Trigonometry")
    st.markdown("Select a trigonometry tool from the sidebar to continue.")
    # Import and call trig pages (handled in respective page files)

# Geometry Page
elif st.session_state.category == "Geometry":
    from pages.geometry import show_geometry_page
    show_geometry_page()
