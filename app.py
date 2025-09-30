import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon

# App Title
st.title("Innovative Trig App: Trigonometry Visualizer for High Schoolers")
st.markdown("""
Welcome to the Innovative Trig App! This app is designed to make trigonometry fun and easy to understand through colorful visualizations, clear explanations, and interactive tools. 
Explore concepts like a trigonometry encyclopedia, use the calculator to verify your homework, and test your knowledge with quizzes.
""")

# Sidebar Navigation
page = st.sidebar.selectbox("Navigate", ["Encyclopedia", "Trig Calculator", "Quiz"])

if page == "Encyclopedia":
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
        
        # Interactive Slider for Angle
        angle_deg = st.slider("Adjust the angle (θ in degrees)", 1, 89, 30)
        angle_rad = math.radians(angle_deg)
        
        # Calculate sides
        hypotenuse = 1
        opposite = math.sin(angle_rad) * hypotenuse
        adjacent = math.cos(angle_rad) * hypotenuse
        
        # Plot Right Triangle
        fig, ax = plt.subplots()
        ax.plot([0, adjacent], [0, 0], 'b-', linewidth=2)  # Adjacent
        ax.plot([adjacent, adjacent], [0, opposite], 'g-', linewidth=2)  # Opposite
        ax.plot([0, adjacent], [0, opposite], 'r-', linewidth=2)  # Hypotenuse
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
        
        angle_deg_unit = st.slider("Adjust the angle (θ in degrees)", 0, 360, 45)
        angle_rad_unit = math.radians(angle_deg_unit)
        
        # Plot Unit Circle
        fig_unit, ax_unit = plt.subplots()
        circle = plt.Circle((0, 0), 1, color='lightblue', fill=False)
        ax_unit.add_patch(circle)
        ax_unit.plot([0, math.cos(angle_rad_unit)], [0, math.sin(angle_rad_unit)], 'r-')
        ax_unit.plot([math.cos(angle_rad_unit), math.cos(angle_rad_unit)], [0, math.sin(angle_rad_unit)], 'g--')  # Vertical
        ax_unit.plot([0, math.cos(angle_rad_unit)], [0, 0], 'b--')  # Horizontal
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

elif page == "Trig Calculator":
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
        st.markdown(f"""
        - Arcsin (degrees): {math.degrees(math.asin(value)):.4f}°
        - Arccos (degrees): {math.degrees(math.acos(value)):.4f}°
        - Arctan (degrees): {math.degrees(math.atan(value)):.4f}°
        """)

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

elif page == "Quiz":
    st.header("Trigonometry Quiz")
    st.markdown("Test your knowledge with these multiple-choice questions!")

    questions = [
        {
            "question": "What is sin(90°)?",
            "options": ["0", "1", "-1", "Undefined"],
            "answer": "1"
        },
        {
            "question": "What does SOH stand for?",
            "options": ["Sine = Opposite/Hypotenuse", "Cosine = Adjacent/Hypotenuse", "Tangent = Opposite/Adjacent", "None"],
            "answer": "Sine = Opposite/Hypotenuse"
        },
        {
            "question": "The period of tan(x) is:",
            "options": ["360°", "180°", "90°", "270°"],
            "answer": "180°"
        },
        {
            "question": "Pythagorean identity:",
            "options": ["sin² + cos² = 1", "sin + cos = 1", "tan = sin/cos", "All of the above"],
            "answer": "sin² + cos² = 1"
        }
    ]

    score = 0
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}: {q['question']}")
        answer = st.radio("Choose:", q["options"])
        if st.button(f"Submit Q{i+1}"):
            if answer == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong! Correct answer: {q['answer']}")

    if st.button("Show Score"):
        st.markdown(f"Your score: {score}/{len(questions)}")
