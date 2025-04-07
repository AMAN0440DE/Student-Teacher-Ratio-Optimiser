import streamlit as st
from pages.home import render_home
from pages.teacher_allocation import render_teacher_allocation
from pages.student_groups import render_student_groups
from pages.analytics import render_analytics
from pages.chatbot import render_chatbot

st.set_page_config(
    page_title="Student-Teacher Ratio Optimizer",
    page_icon="📚",
    layout="wide"
)

# Define the navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Teacher Allocation", "Student Groups", "Analytics", "Chatbot"]
)

# Display the appropriate page based on selection
if page == "Home":
    render_home()
elif page == "Teacher Allocation":
    render_teacher_allocation()
elif page == "Student Groups":
    render_student_groups()
elif page == "Analytics":
    render_analytics()
elif page == "Chatbot":
    render_chatbot()

# Footer
st.markdown("---")
st.markdown("Built with ❤️ DR teams")