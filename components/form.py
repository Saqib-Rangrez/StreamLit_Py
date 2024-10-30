import streamlit as st
from datetime import datetime
from utils.data_processing import load_uphc_data, filter_events_by_day, get_session_details, load_child_data, filter_child_data
from utils.date_utils import get_day_of_month
import os

def display_form():
    # Date selection with a highlighted heading
    selected_date = st.date_input("Select Date", value=datetime.today())
    day_info = get_day_of_month(selected_date)
    st.markdown(f"<span style='font-weight: bold;'>Selected Date: </span> {selected_date.strftime('%d %b %Y')}", unsafe_allow_html=True)
    st.markdown(f"<span style='font-weight: bold;'>Day of the month: </span> {day_info}", unsafe_allow_html=True)

    # UPHC selection
    st.markdown("<h3 style='color: #4A90E2;'>Select UPHC</h3>", unsafe_allow_html=True)
    uphc_type = st.selectbox("", options=["Select UPHC", "Shanti Nagar", "Eid Gah"])

    if uphc_type != "Select UPHC":
        
        file_path = "./data/scamps.csv" if uphc_type == "Shanti Nagar" else "./data/icamps.csv"
        smap_data = load_uphc_data(file_path)

        # Filter events based on the day of the session
        events_today = filter_events_by_day(smap_data, day_info)
        if not events_today.empty:
            st.markdown("<h3 style='color: #4A90E2;'>Available Events for Selected Date</h3>", unsafe_allow_html=True)

            # Add a serial number column for display
            events_today = events_today.reset_index(drop=True)
            events_today.index += 1
            events_today.reset_index(inplace=True)
            events_today.rename(columns={'index': 'Sr. No.'}, inplace=True)

            # Display event details with serial numbers in a styled table
            st.table(events_today[['Sr. No.', 'NAME_OF_AREA', 'SESSION_PLACE', 'NAME_OF_ANM', 'NAME_OF_ASHA']])

            # Session place selection with clearer heading
            session_place = st.selectbox("Select Session Place", options=events_today['SESSION_PLACE'].unique())

            # Display selected ANM and ASHA as text with styling for readability
            anm_options, asha_options = get_session_details(events_today, session_place)
            selected_anm = anm_options[0] if anm_options else "N/A"
            selected_asha = asha_options[0] if asha_options else "N/A"
            st.markdown(f"<span style='font-weight: bold;'>Selected ANM: </span>{selected_anm}", unsafe_allow_html=True)
            st.markdown(f"<span style='font-weight: bold;'>Selected ASHA: </span> {selected_asha}", unsafe_allow_html=True)

            # Load and filter child data based on session place
            child_data_file_path = "child_data.csv"  # Assuming this is the path to the child data CSV
            child_data = load_child_data(child_data_file_path)
            children_for_session = filter_child_data(child_data, session_place)

            # Display child details with checkboxes for visitation and conversion status
            if not children_for_session.empty:
                st.markdown("<h3 style='color: #4A90E2;'>Children for the Selected Session Place</h3>", unsafe_allow_html=True)
                for index, child in children_for_session.iterrows():
                    st.markdown(f"<p style='font-weight: bold;'>Child ID: {child['CHILD_ID']}, Name: {child['CHILD_NAME']}, Age: {child['AGE']}</p>", unsafe_allow_html=True)
                    
                    # Checkbox for visitation status
                    visited = st.checkbox("Visited", key=f"visited_{index}")

                    # Checkbox for conversion status
                    conversion_done = st.checkbox("Conversion Done", key=f"conversion_{index}")

                    # Store the selection
                    children_for_session.loc[index, 'Visited'] = visited
                    children_for_session.loc[index, 'Conversion_Done'] = conversion_done

            # Additional form fields as needed with highlighting
            st.markdown("<h3 style='color: #4A90E2;'>Additional Details</h3>", unsafe_allow_html=True)
            due = st.number_input("Enter Due Number", min_value=0, step=1)
            return day_info, session_place, selected_anm, selected_asha, due, children_for_session

    else:
        st.warning("Please select a valid UPHC.")
