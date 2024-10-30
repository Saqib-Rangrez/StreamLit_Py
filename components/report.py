import streamlit as st
from datetime import datetime

def display_report(selected_day, uphc, area, anm, asha, due, visited_child, conversion):
    st.header("Generated Report")

    # Display the report in card format
    st.write(f"**Date:** {datetime.today().strftime('%d %b %Y')}")
    st.write(f"**UPHC:** {uphc}")
    st.write(f"**AREA:** {area}")
    st.write(f"**ANM:** {anm}")
    st.write(f"**ASHA:** {asha}")
    st.write(f"**DUE:** {due}")
    st.write(f"**VISITED CHILD:** {len(visited_child)}")
    st.write(f"**CONVERSION DONE:** {conversion}")
