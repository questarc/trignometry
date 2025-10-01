import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon, Circle

def show_geometry_page():
    st.header("Geometry Explorer")
    st.markdown("""
    Welcome to the Geometry section! Learn about shapes, areas, volumes, and transformations with interactive visualizations and tools.
    Use the expanders below to explore key concepts or try the calculator and quiz.
    """)

    with st.expander("1. Basic Shapes and Properties"):
        st.markdown("""
        ### Explanation
        Geometry studies shapes, their properties, and relationships. Key shapes include:
        - **Triangles**: Three sides, angles sum to 180°.
        - **Circles**: Defined by radius, with circumference and area formulas.
        - **Quadrilaterals**: Four-sided shapes like rectangles and parallelograms.
        
        ### Formulas
        - Triangle Area: \\(A = \\frac{1}{2} \\times base \\times height\\)
        - Circle Area: \\(A = \\pi r^2\\)
        - Rectangle Area: \\(A = length \\times width\\)
        """)
        
        shape = st.selectbox("Choose a shape to visualize", ["Triangle", "Circle", "Rectangle"])
        if shape == "Triangle":
            base = st.slider("Base length", 1.0, 10.0, 5.0)
            height = st.slider("Height", 1.0, 10.0, 3.0)
            area = 0.5 * base * height
            
            fig, ax = plt.subplots()
            triangle = Polygon([[0, 0], [base, 0], [base/2, height]], color='lightgreen')
            ax.add_patch(triangle)
            ax.set_xlim(-1, base + 1)
            ax.set_ylim(-1, height + 1)
            ax.axis('equal')
            st.pyplot(fig)
            st.markdown(f"Area: {area:.2f} square units")
        
        elif shape == "Circle":
            radius = st.slider("Radius", 1.0, 5.0, 2.0)
            area = np.pi * radius**2
            
            fig, ax = plt.subplots()
            circle = Circle((0, 0), radius, color='lightblue', fill=False)
            ax.add_patch(circle)
            ax.set_xlim(-radius-1, radius+1)
            ax.set_ylim(-radius-1, radius+1)
            ax.axis('equal')
            st.pyplot(fig)
            st.markdown(f"Area: {area:.2f} square units")
        
        elif shape == "Rectangle":
            length = st.slider("Length", 1.0, 10.0, 5.0)
            width = st.slider("Width", 1.0, 10.0, 3.0)
            area = length * width
            
            fig, ax = plt.subplots()
            rectangle = Polygon([[0, 0], [length, 0], [length, width], [0, width]], color='lightcoral')
            ax.add_patch(rectangle)
            ax.set_xlim(-1, length + 1)
            ax.set_ylim(-1, width + 1)
            ax.axis('equal')
            st.pyplot(fig)
            st.markdown(f"Area: {area:.2f} square units")

    with st.expander("2. Angles and Polygons"):
        st.markdown("""
        ### Explanation
        Angles in polygons are key to understanding shapes.
        - Sum of interior angles in a polygon: \\((n-2) \\times 180^\\circ\\), where n is the number of sides.
        - Regular polygons have equal sides and angles.
        
        ### Visualization
        """)
        sides = st.slider("Number of polygon sides", 3, 8, 4)
        angle_sum = (sides - 2) * 180
        st.markdown(f"Sum of interior angles: {angle_sum}°")
        
        fig, ax = plt.subplots()
        theta = np.linspace(0, 2*np.pi, sides+1)
        x = np.cos(theta)
        y = np.sin(theta)
        ax.plot(x, y, 'b-')
        ax.set_aspect('equal')
        ax.axis('off')
        st.pyplot(fig)

    with st.expander("3. Geometry Calculator"):
        st.markdown("Calculate areas, perimeters, or volumes of shapes.")
        calc_type = st.selectbox("Choose calculation", ["Triangle Area", "Circle Circumference", "Cube Volume"])
        
        if calc_type == "Triangle Area":
            base = st.number_input("Base", value=5.0)
            height = st.number_input("Height", value=3.0)
            area = 0.5 * base * height
            st.markdown(f"Area: {area:.2f} square units")
        
        elif calc_type == "Circle Circumference":
            radius = st.number_input("Radius", value=2.0)
            circumference = 2 * np.pi * radius
            st.markdown(f"Circumference: {circumference:.2f} units")
        
        elif calc_type == "Cube Volume":
            side = st.number_input("Side length", value=4.0)
            volume = side**3
            st.markdown(f"Volume: {volume:.2f} cubic units")

    with st.expander("4. Geometry Quiz"):
        st.markdown("Test your geometry knowledge!")
        questions = [
            {
                "question": "What is the sum of angles in a triangle?",
                "options": ["180°", "360°", "90°", "270°"],
                "answer": "180°"
            },
            {
                "question": "The formula for the area of a circle is:",
                "options": ["πr²", "2πr", "r²", "πr"],
                "answer": "πr²"
            }
        ]
        
        score = 0
        for i, q in enumerate(questions):
            st.subheader(f"Question {i+1}: {q['question']}")
            answer = st.radio("Choose:", q["options"], key=f"geo_quiz_{i}")
            if st.button(f"Submit Q{i+1}", key=f"geo_submit_q{i}"):
                if answer == q["answer"]:
                    st.success("Correct!")
                    score += 1
                else:
                    st.error(f"Wrong! Correct answer: {q['answer']}")
        
        if st.button("Show Score"):
            st.markdown(f"Your score: {score}/{len(questions)}")
