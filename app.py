import streamlit as st
import pandas as pd
from datetime import datetime
import time

# Initialize an empty list to store the candy interactions
candy_events = []

# Simulate a toddler picking up and eating candies
def candy_simulation():
    candies = ['Candy 1', 'Candy 2', 'Candy 3', 'Candy 4', 'Candy 5']
    for candy in candies:
        pick_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        candy_events.append({'Candy': candy, 'Event': 'Picked Up', 'Timestamp': pick_time})
        time.sleep(2)  # Simulate delay between actions
        eat_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        candy_events.append({'Candy': candy, 'Event': 'Eaten', 'Timestamp': eat_time})
        time.sleep(2)

# Main Streamlit app
def main():
    st.title("Hungry Toddler Candy Tracker")
    
    # Button to start the candy simulation
    if st.button('Run Candy Simulation'):
        st.write("Starting simulation...")
        candy_simulation()
        st.write("Simulation complete!")
    
    # Display the candy event log
    if candy_events:
        df = pd.DataFrame(candy_events)
        st.write("Candy Event Log:")
        st.dataframe(df)

        # Button to download the event log as CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name='candy_event_log.csv', mime='text/csv')

if __name__ == "__main__":
    main()
