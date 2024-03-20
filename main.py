
import streamlit as st
import cv2

vid = cv2.VideoCapture( 'rtsp://192.168.141.166:8080/h264.sdp' )

st.title( 'Using Mobile Camera with Streamlit' )
frame_window = st.image( [] )
take_picture_button = st.button( 'Take Picture' )

while True:
    got_frame , frame = vid.read()
    frame = cv2.cvtColor( frame , cv2.COLOR_BGR2RGB )
    if got_frame:
        frame_window.image(frame)

    if take_picture_button:
        # Pass the frame to a model
        # And show the output here...
        break

vid.release()
