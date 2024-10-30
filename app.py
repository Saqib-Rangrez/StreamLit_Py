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

    # Initialize variables
    selected_day = None
    session_place = None
    selected_anm = None
    selected_asha = None
    due = None
    children_for_session = None

    # Tab 1: Enter Details
    with tabs[0]:
        result = form.display_form()
        if result is None:
            st.error("Form submission failed. Please check your inputs.")
        else:
            selected_day, session_place, selected_anm, selected_asha, due, children_for_session = result

    # Tab 2: Show Report
    with tabs[1]:
        if selected_day is not None:
            report.display_report(selected_day, session_place, selected_anm, selected_asha, due, children_for_session)
        else:
            st.warning("Please enter details in the first tab to see the report.")

if __name__ == "__main__":
    main()
