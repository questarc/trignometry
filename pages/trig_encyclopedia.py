import streamlit as st
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def show_trig_encyclopedia():
    st.header("Trigonometry Encyclopedia")
    st.markdown("""
    This section covers key trigonometry concepts with explanations, formulas, and colorful visualizations. Use the expander sections below to dive in!
    """)

    with st.expander("1. Basic Trigonometric Functions (Sin, Cos, Tan)"):
        st.markdown("""
        ### Explanation
        Trigonometric functions describe relationships between angles and sides in triangles. The three basic ones are:
        - **Sine (sin)**: Opposite / Hypotenuse
        - **Cosine (cos)**: Adjacent / Hypotenuse
        - **Tangent (tan)**: Opposite / Adjacent
        
        These are often remembered with **SOH-CAH-TOA**.
        
        ### Formulas
        - \\(\\sin(\\theta) = \\frac{opposite}{hypotenuse}\\)
        - \\(\\cos(\\theta) = \\frac{adjacent}{hypotenuse}\\)
        - \\(\\tan(\\theta) = \\frac{opposite}{adjacent}\\)
        
        ### Visualization: Right Triangle
        """)
        
        angle_deg = st.slider("Adjust the angle (θ in degrees)", 1, 89, 30, key="rt_angle")
        angle_rad = math.radians(angle_deg)
        
        hypotenuse = 1
        opposite = math.sin(angle_rad) * hypotenuse
        adjacent = math.cos(angle_rad) * hypotenuse
        
        fig, ax = plt.subplots()
        ax.plot([0, adjacent], [0, 0], 'b-', linewidth=2)
        ax.plot([adjacent, adjacent], [0, opposite], 'g-', linewidth=2)
        ax.plot([0, adjacent], [0, opposite], 'r-', linewidth=2)
        ax.text(adjacent/2, -0.05, 'Adjacent', color='b')
        ax.text(adjacent + 0.01, opposite/2, 'Opposite', color='g')
        ax.text(adjacent/2, opposite/2, 'Hypotenuse', color='r')
        ax.add_patch(Arc((0,0), 0.2, 0.2, theta1=0, theta2=angle_deg, color='purple'))
        ax.text(0.1, 0.05, f'θ = {angle_deg}°', color='purple')
        ax.set_xlim(0, 1.1)
        ax.set_ylim(0, 1.1)
        ax.axis('off')
        st.pyplot(fig)
        
        st.markdown(f"""
        - Sin(θ) = {opposite:.2f}
        - Cos(θ) = {adjacent:.2f}
        - Tan(θ) = {opposite/adjacent:.2f}
        """)

    with st.expander("2. The Unit Circle"):
        st.markdown("""
        ### Explanation
        The unit circle is a circle with radius 1 centered at the origin. It helps visualize trig functions for any angle.
        - Coordinates: (cos(θ), sin(θ))
        - Tan(θ) = sin(θ)/cos(θ)
        
        ### Formulas
        - \\(x = \\cos(\\theta)\\)
        - \\(y = \\sin(\\theta)\\)
        
        ### Visualization: Unit Circle
        """)
        
        angle_deg_unit = st.slider("Adjust the angle (θ in degrees)", 0, 360, 45, key="uc_angle")
        angle_rad_unit = math.radians(angle_deg_unit)
        
        fig_unit, ax_unit = plt.subplots()
        circle = plt.Circle((0, 0), 1, color='lightblue', fill=False)
        ax_unit.add_patch(circle)
        ax_unit.plot([0, math.cos(angle_rad_unit)], [0, math.sin(angle_rad_unit)], 'r-')
        ax_unit.plot([math.cos(angle_rad_unit), math.cos(angle_rad_unit)], [0, math.sin(angle_rad_unit)], 'g--')
        ax_unit.plot([0, math.cos(angle_rad_unit)], [0, 0], 'b--')
        ax_unit.text(0.5, -0.1, 'cos(θ)', color='b')
        ax_unit.text(math.cos(angle_rad_unit) + 0.01, math.sin(angle_rad_unit)/2, 'sin(θ)', color='g')
        ax_unit.add_patch(Arc((0,0), 0.5, 0.5, theta1=0, theta2=angle_deg_unit if angle_deg_unit <= 180 else angle_deg_unit - 360, color='purple'))
        ax_unit.text(0.2, 0.1, f'θ = {angle_deg_unit}°', color='purple')
        ax_unit.set_xlim(-1.2, 1.2)
        ax_unit.set_ylim(-1.2, 1.2)
        ax_unit.set_aspect('equal')
        ax_unit.axis('off')
        st.pyplot(fig_unit)
        
        st.markdown(f"""
        - Cos(θ) = {math.cos(angle_rad_unit):.2f}
        - Sin(θ) = {math.sin(angle_rad_unit):.2f}
        - Tan(θ) = {math.tan(angle_rad_unit):.2f}
        """)

    with st.expander("3. Graphs of Trigonometric Functions"):
        st.markdown("""
        ### Explanation
        Trig functions are periodic and can be graphed as waves.
        - Sine and Cosine have amplitude 1, period 360°.
        - Tangent has asymptotes and period 180°.
        
        ### Formulas
        - \\(y = \\sin(x)\\)
        - \\(y = \\cos(x)\\)
        - \\(y = \\tan(x)\\)
        
        ### Visualization: Graphs
        """)
        
        import numpy as np
        x = np.linspace(0, 2*np.pi, 1000)
        fig_graph, ax_graph = plt.subplots(3, 1, figsize=(8, 12))
        
        ax_graph[0].plot(x, np.sin(x), color='red')
        ax_graph[0].set_title('Sine Function', color='red')
        ax_graph[0].grid(True)
        
        ax_graph[1].plot(x, np.cos(x), color='blue')
        ax_graph[1].set_title('Cosine Function', color='blue')
        ax_graph[1].grid(True)
        
        ax_graph[2].plot(x, np.tan(x), color='green')
        ax_graph[2].set_title('Tangent Function', color='green')
        ax_graph[2].set_ylim(-10, 10)
        ax_graph[2].grid(True)
        
        plt.tight_layout()
        st.pyplot(fig_graph)

    with st.expander("4. Trigonometric Identities"):
        st.markdown("""
        ### Explanation
        Identities are equations true for all angles. They help simplify expressions.
        
        ### Key Formulas
        - Pythagorean: \\(\\sin^2(\\theta) + \\cos^2(\\theta) = 1\\)
        - \\(\\tan(\\theta) = \\frac{\\sin(\\theta)}{\\cos(\\theta)}\\)
        - Angle Sum: \\(\\sin(a + b) = \\sin(a)\\cos(b) + \\cos(a)\\sin(b)\\)
        - And many more...
        
        ### Visualization: Pythagorean Identity
        The unit circle shows this identity since x² + y² = 1.
        """)

    with st.expander("5. Inverse Trigonometric Functions"):
        st.markdown("""
        ### Explanation
        Inverse functions find angles from ratios.
        - \\(\\theta = \\sin^{-1}(opposite/hypotenuse)\\)
        
        ### Formulas
        - \\(\\arcsin(x), \\arccos(x), \\arctan(x)\\)
        
        ### Visualization
        Use the calculator section to compute inverses!
        """)

    with st.expander("6. Law of Sines and Cosines"):
        st.markdown("""
        ### Explanation
        For any triangle:
        - Law of Sines: \\(\\frac{a}{\\sin(A)} = \\frac{b}{\\sin(B)} = \\frac{c}{\\sin(C)}\\)
        - Law of Cosines: \\(c^2 = a^2 + b^2 - 2ab\\cos(C)\\)
        
        ### Visualization: Triangle Solver in Calculator
        """)
