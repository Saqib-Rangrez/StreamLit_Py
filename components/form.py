import streamlit as st
from datetime import datetime
import pandas as pd
from utils.date_utils import get_day_of_month
from utils.data_processing import load_uphc_data, filter_children_data

def display_form():
    st.header("Enter Details")

    # Display today's date and calculate day of the month
    today = datetime.today()
    day_info = get_day_of_month(today)
    st.write(f"Today's Date: {today.strftime('%d %b %Y')}")
    st.write(f"Today is the {day_info} of the month")

    # Step 1: Select UPHC
    uphc = st.selectbox("Select UPHC", options=["Shanti Nagar", "Eid Gah"])

    # Step 2: Filter UPHC data based on selected day
    uphc_data = load_uphc_data()
    filtered_uphc_data = uphc_data[uphc_data["Day_of_Month"] == day_info]
    
    area = st.selectbox("Select Area", options=filtered_uphc_data["Area"].unique())
    anm = st.selectbox("Select ANM", options=filtered_uphc_data["ANM"].unique())
    asha = st.selectbox("Select ASHA", options=filtered_uphc_data["ASHA"].unique())

    # Step 3: Enter Due number
    due = st.number_input("Enter Due Number", min_value=0, step=1)

    # Step 4: Filter children data based on selected UPHC and area
    children_data = filter_children_data(area)
    visited_child = st.multiselect("Visited Child", options=children_data["Child_ID"].tolist())
    
    # Step 5: Count conversions
    conversion = st.number_input("Enter Conversion Done", min_value=0, step=1)

    return day_info, uphc, area, anm, asha, due, visited_child, conversion
