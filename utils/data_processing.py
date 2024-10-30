import pandas as pd

def load_uphc_data(file_path):
    """
    Load SMAP data from a CSV file.
    Arguments:
        file_path (str): The path to the CSV file.
    Returns:
        pd.DataFrame: The loaded SMAP data.
    """
    try:
        df = pd.read_csv(file_path)
        # print(df)
        if df.empty:
            print(f"Warning: The DataFrame is empty after loading from {file_path}.")
        return df
    except Exception as e:
        print(f"Error loading data from {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error


def filter_events_by_day(smap_data, day_info):
    """
    Filter events based on the day of the session.
    Arguments:
        smap_data (pd.DataFrame): The loaded SMAP data.
        day_info (str): The day of the month (e.g., "First Monday").
    Returns:
        pd.DataFrame: Filtered events that match the day of the session.
    """
    # Strip whitespace and clean the DAY OF SESSION column
    smap_data['DAY_OF_SESSION'] = smap_data['DAY_OF_SESSION'].str.replace(r'\s+', ' ', regex=True).str.strip()
    
    # Filter the DataFrame
    filtered_events = smap_data[smap_data['DAY_OF_SESSION'].str.lower() == day_info.lower()]
    
    return filtered_events



def get_session_details(events_today, session_place):
    """
    Get available ANM and ASHA options for a specific session place.
    Arguments:
        events_today (pd.DataFrame): Filtered events data for today.
        session_place (str): The selected session place.
    Returns:
        tuple: Two lists containing ANM and ASHA names respectively.
    """
    # Filter for the selected session place
    session_data = events_today[events_today['SESSION_PLACE'] == session_place]

    # Get unique ANM and ASHA options
    anm_options = session_data['NAME_OF_ANM'].unique().tolist()
    asha_options = session_data['NAME_OF_ASHA'].unique().tolist()

    return anm_options, asha_options

def load_child_data(file_path):
    # Load child data from a CSV file.
    return pd.read_csv(file_path)

def filter_child_data(child_data, session_place):
    # Filter child data based on the session place.
    filtered_children = child_data[child_data['SESSION_PLACE'] == session_place]
    return filtered_children