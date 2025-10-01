import streamlit as st
import math

def show_trig_calculator():
    st.header("Trig Calculator")
    st.markdown("Use this tool to calculate trig values or solve triangles. Verify your homework here!")

    calc_type = st.selectbox("Choose Calculation Type", ["Basic Trig Functions", "Inverse Trig Functions", "Triangle Solver"])

    if calc_type == "Basic Trig Functions":
        angle = st.number_input("Enter angle in degrees", value=0.0)
        angle_rad = math.radians(angle)
        st.markdown(f"""
        - Sin: {math.sin(angle_rad):.4f}
        - Cos: {math.cos(angle_rad):.4f}
        - Tan: {math.tan(angle_rad):.4f}
        """)

    elif calc_type == "Inverse Trig Functions":
        value = st.number_input("Enter value (-1 to 1 for sin/cos, any for tan)", value=0.0)
        try:
            st.markdown(f"""
            - Arcsin (degrees): {math.degrees(math.asin(value)):.4f}°
            - Arccos (degrees): {math.degrees(math.acos(value)):.4f}°
            - Arctan (degrees): {math.degrees(math.atan(value)):.4f}°
            """)
        except ValueError:
            st.error("Value must be between -1 and 1 for arcsin and arccos.")

    elif calc_type == "Triangle Solver":
        st.subheader("Right Triangle Solver")
        side_a = st.number_input("Side A (opposite to angle A)", value=0.0)
        side_b = st.number_input("Side B (adjacent to angle A)", value=0.0)
        if side_a and side_b:
            hypotenuse = math.sqrt(side_a**2 + side_b**2)
            angle_a = math.degrees(math.atan(side_a / side_b))
            st.markdown(f"""
            - Hypotenuse: {hypotenuse:.4f}
            - Angle A: {angle_a:.4f}°
            """)
