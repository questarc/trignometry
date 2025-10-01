import streamlit as st
import matplotlib.pyplot as plt
import math
from matplotlib.patches import Arc

def show_trig_vr_environments():
    st.header("VR-Inspired Virtual Environments")
    st.markdown("""
    Solve trig challenges in a virtual world! Calculate the height of a tower by entering the angle of elevation and distance.
    """)
    
    distance = st.number_input("Distance to tower base (meters)", value=10.0)
    angle_deg = st.number_input("Angle of elevation (degrees)", value=30.0)
    if distance and angle_deg:
        angle_rad = math.radians(angle_deg)
        height = distance * math.tan(angle_rad)
        st.markdown(f"Tower height: {height:.2f} meters")
        
        fig_vr, ax_vr = plt.subplots()
        ax_vr.plot([0, distance], [0, 0], 'b-')
        ax_vr.plot([distance, distance], [0, height], 'g-')
        ax_vr.plot([0, distance], [0, height], 'r-')
        ax_vr.add_patch(Arc((0,0), 2, 2, theta1=0, theta2=angle_deg, color='purple'))
        ax_vr.text(0.5, 0.1, f'θ = {angle_deg}°', color='purple')
        ax_vr.text(distance/2, -0.2, 'Distance', color='b')
        ax_vr.text(distance + 0.1, height/2, 'Height', color='g')
        ax_vr.set_xlim(0, distance * 1.2)
        ax_vr.set_ylim(0, height * 1.2)
        ax_vr.axis('off')
        st.pyplot(fig_vr)
