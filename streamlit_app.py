import time
import streamlit as st

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds  # Convert total time to seconds
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        st.write(timeformat)  # Display the time in Streamlit
        time.sleep(1)
        total_seconds -= 1

    st.write("Time's up!")

# Streamlit App
st.title("Countdown Timer")

# User input for minutes and seconds
minutes = st.number_input("Enter minutes:", min_value=0, step=1)
seconds = st.number_input("Enter seconds:", min_value=0, step=1)

# Button to start the timer
if st.button("Start Timer"):
    if minutes > 0 or seconds > 0:
        countdown_timer(minutes, seconds)
    else:
        st.write("Please enter a valid time.")
