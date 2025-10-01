import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def show_trig_clinometer():
    st.header("Clinometer and Measurement Simulator")
    st.markdown("""
    Simulate using a clinometer to measure heights. Enter an angle and distance to calculate the height of an object.
    """)
    
    angle_deg = st.number_input("Angle of elevation (degrees)", value=30.0, key="clino_angle")
    distance = st.number_input("Distance to object (meters)", value=10.0)
    angle_rad = math.radians(angle_deg)
    height = distance * math.tan(angle_rad)
    
    st.markdown(f"Object height: {height:.2f} meters")
    
    fig_clino, ax_clino = plt.subplots()
    ax_clino.plot([0, distance], [0, 0], 'b-')
    ax_clino.plot([distance, distance], [0, height], 'g-')
    ax_clino.plot([0, distance], [0, height], 'r-')
    ax_clino.add_patch(Arc((0,0), 2, 2, theta1=0, theta2=angle_deg, color='purple'))
    ax_clino.text(0.5, 0.1, f'θ = {angle_deg}°', color='purple')
    ax_clino.set_xlim(0, distance * 1.2)
    ax_clino.set_ylim(0, height * 1.2)
    ax_clino.axis('off')
    st.pyplot(fig_clino)
