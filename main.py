import streamlit as st
import cv2
import time

st.title('Using Mobile Camera with Streamlit')
frame_window = st.image([])
take_picture_button = st.button('Take Picture')

# Add a 2-minute delay before attempting to open the video stream
st.write("Checking connection...")
#time.sleep(10)

# Initialize video capture
vid = cv2.VideoCapture('rtsp://192.168.141.166:8080/h264.sdp')

# Check if the camera is opened successfully
if not vid.isOpened():
    error_message = "Error: Unable to open camera stream."
    st.error(error_message)
    raise RuntimeError(error_message)

# Loop until user takes a picture
while not take_picture_button:
    # Read frame from video stream
    got_frame, frame = vid.read()
    
    if not got_frame:
        st.warning("Warning: Unable to read frame from camera stream.")
        break
    
    # Convert frame to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Update displayed frame
    frame_window.image(frame)
    
    # Introduce delay to control update rate
    time.sleep(0.1)

# Release video capture resources
vid.release()
