# import streamlit as st
# from datetime import datetime
# from utils.data_processing import load_uphc_data, filter_events_by_day, get_session_details
# from utils.date_utils import get_day_of_month

# def display_form():
#     st.header("Enter Details")

#     # Display today's date and calculate day of the month
#     today = datetime.today()
#     day_info = get_day_of_month(today)
#     st.write(f"Today's Date: {today.strftime('%d %b %Y')}")
#     st.write(f"Today is the {day_info} of the month")

#     # Step 1: Select UPHC
#     uphc = st.selectbox("Select UPHC", options=["Shanti Nagar", "Other"])

#     # Load the appropriate CSV file based on UPHC selection
#     if uphc == "Shanti Nagar":
#         smap_data = load_uphc_data("scamps.csv")  # Load "scamps.csv" for Shanti Nagar
#     else:
#         smap_data = load_uphc_data("icamps.csv")  # Load "icamps.csv" for other UPHC

#     # Step 2: Filter events based on the day of the session
#     events_today = filter_events_by_day(smap_data, day_info)
#     if not events_today.empty:
#         st.write("Available Events for Today:")

#         # Display event details
#         st.dataframe(events_today[['NAME_OF_AREA', 'SESSION_PLACE', 'NAME_OF_ANM', 'NAME_OF_ASHA']])

#         # Step 3: Select a session place from the filtered events
#         session_place = st.selectbox("Select Session Place", options=events_today['SESSION_PLACE'].unique())

#         # Get available ANM and ASHA options based on session place
#         anm_options, asha_options = get_session_details(events_today, session_place)
#         selected_anm = st.selectbox("Select ANM", options=anm_options)
#         selected_asha = st.selectbox("Select ASHA", options=asha_options)

#         # Additional form fields as needed
#         due = st.number_input("Enter Due Number", min_value=0, step=1)

#         return day_info, session_place, selected_anm, selected_asha, due

#     else:
#         st.write("No events available for today.")
#         return day_info, None, None, None, None


import streamlit as st
from datetime import datetime
from utils.data_processing import load_uphc_data, filter_events_by_day, get_session_details, load_child_data, filter_child_data
from utils.date_utils import get_day_of_month
import os

def display_form():
    st.header("Enter Details")

    # Display today's date and calculate day of the month
    today = datetime.today()
    day_info = get_day_of_month(today)
    st.write(f"Today's Date: {today.strftime('%d %b %Y')}")
    st.write(f"Today is the {day_info} of the month")

    # Load smap data (ICamps or SCamps based on location)
    uphc_type = st.selectbox("Select UPHC", options=["Select UPHC", "Shanti Nagar", "Eid Gah"])
    print(uphc_type)
    if uphc_type != "Select UPHC":
        
        file_path = "./data/scamps.csv" if uphc_type == "Shanti Nagar" else "./data/icamps.csv"
        print("File exists:", os.path.isfile(file_path))
        smap_data = load_uphc_data(file_path)

        # Step 1: Filter events based on the day of the session
        events_today = filter_events_by_day(smap_data, day_info)
        print(day_info)
        print(events_today)
        if not events_today.empty:
            st.write("Available Events for Today:")

            # Display event details
            st.dataframe(events_today[['NAME_OF_AREA', 'SESSION_PLACE', 'NAME_OF_ANM', 'NAME_OF_ASHA']])

            # Step 2: Select a session place from the filtered events
            session_place = st.selectbox("Select Session Place", options=events_today['SESSION_PLACE'].unique())

            # Get available ANM and ASHA options based on session place
            anm_options, asha_options = get_session_details(events_today, session_place)
            selected_anm = st.selectbox("Select ANM", options=anm_options)
            selected_asha = st.selectbox("Select ASHA", options=asha_options)

            # Step 3: Load and filter child data based on the session place
            child_data_file_path = "child_data.csv"  # Assuming this is the path to the child data CSV
            child_data = load_child_data(child_data_file_path)
            children_for_session = filter_child_data(child_data, session_place)

            # Display child details with checkboxes for visitation and conversion status
            if not children_for_session.empty:
                st.write("Children for the selected session place:")
                for index, child in children_for_session.iterrows():
                    st.write(f"Child ID: {child['CHILD_ID']}, Name: {child['CHILD_NAME']}, Age: {child['AGE']}")

                    # Checkbox for visitation status
                    visited = st.checkbox("Visited", key=f"visited_{index}")

                    # Checkbox for conversion status
                    conversion_done = st.checkbox("Conversion Done", key=f"conversion_{index}")

                    # Store the selection
                    children_for_session.loc[index, 'Visited'] = visited
                    children_for_session.loc[index, 'Conversion_Done'] = conversion_done

            # Additional form fields as needed
            due = st.number_input("Enter Due Number", min_value=0, step=1)
            return day_info, session_place, selected_anm, selected_asha, due, children_for_session

    else:
        st.warning("Please select a valid UPHC.")
    



