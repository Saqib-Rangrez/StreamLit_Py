import streamlit as st
from datetime import datetime
from components import form, report
from utils.date_utils import get_day_of_month

# Set up page configuration
st.set_page_config(page_title="UPHC Child Visit Application", layout="wide")

# Main app structure
def main():
    st.title("UPHC Child Visit Application")

    # Set up tabs
    tabs = st.tabs(["Enter Details", "Show Report"])

    # Tab 1: Enter Details
    with tabs[0]:
        selected_day, uphc, area, anm, asha, due, visited_child, conversion = form.display_form()

    # Tab 2: Show Report
    with tabs[1]:
        if selected_day and uphc:
            report.display_report(selected_day, uphc, area, anm, asha, due, visited_child, conversion)

if __name__ == "__main__":
    main()
