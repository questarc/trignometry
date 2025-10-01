import streamlit as st
import math
import plotly.graph_objects as go
import numpy as np

def show_trig_ar_unit_circle():
    st.header("AR-Style Unit Circle Simulator")
    st.markdown("""
    Drag the angle arm to explore the unit circle interactively. Watch sine, cosine, and tangent update in real-time, along with the corresponding wave graphs.
    """)
    
    angle_deg = st.slider("Angle (degrees)", 0, 360, 45, key="ar_angle")
    angle_rad = math.radians(angle_deg)
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[0, math.cos(angle_rad)], y=[0, math.sin(angle_rad)], mode='lines+markers', name='Angle Arm', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=[math.cos(angle_rad)], y=[math.sin(angle_rad)], mode='markers', marker=dict(size=10, color='red'), name='Point'))
    fig.add_trace(go.Scatter(x=[0, math.cos(angle_rad)], y=[0, 0], mode='lines', line=dict(color='blue', dash='dash'), name='cos(θ)'))
    fig.add_trace(go.Scatter(x=[math.cos(angle_rad), math.cos(angle_rad)], y=[0, math.sin(angle_rad)], mode='lines', line=dict(color='green', dash='dash'), name='sin(θ)'))
    fig.add_shape(type="circle", xref="x", yref="y", x0=-1, y0=-1, x1=1, y1=1, line_color="lightblue")
    fig.update_layout(xaxis=dict(range=[-1.5, 1.5]), yaxis=dict(range=[-1.5, 1.5]), showlegend=True, title="Interactive Unit Circle")
    st.plotly_chart(fig)
    
    st.markdown(f"""
    - Cos(θ) = {math.cos(angle_rad):.2f}
    - Sin(θ) = {math.sin(angle_rad):.2f}
    - Tan(θ) = {math.tan(angle_rad):.2f}
    """)
    
    x_wave = np.linspace(0, 2*np.pi, 1000)
    y_wave = np.sin(x_wave)
    fig_wave = go.Figure()
    fig_wave.add_trace(go.Scatter(x=x_wave, y=y_wave, mode='lines', name='Sine Wave', line=dict(color='red')))
    fig_wave.add_trace(go.Scatter(x=[angle_rad], y=[math.sin(angle_rad)], mode='markers', marker=dict(size=10), name='Current Point'))
    fig_wave.update_layout(title="Sine Wave", xaxis_title="Angle (radians)", yaxis_title="Value")
    st.plotly_chart(fig_wave)
