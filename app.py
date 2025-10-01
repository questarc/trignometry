import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Polygon
import plotly.graph_objects as go
import io
from PIL import Image, ImageDraw
import base64
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = "Encyclopedia"

# App Title
st.title("Innovative Trig App: Trigonometry Visualizer for High Schoolers")
st.markdown("""
Welcome to the Innovative Trig App! This app is designed to make trigonometry fun and easy to understand through colorful visualizations, clear explanations, and interactive tools. 
Explore concepts like a trigonometry encyclopedia, use the calculator to verify your homework, test your knowledge with quizzes, discover real-world applications, and engage with creative visualizations.
""")

# Sidebar Navigation with Icons
st.sidebar.header("Navigation")
pages = {
    "📚 Encyclopedia": "Encyclopedia",
    "🧮 Trig Calculator": "Trig Calculator",
    "❓ Quiz": "Quiz",
    "🌍 Real-World Applications": "Real-World Applications",
    "🔄 AR Unit Circle": "AR Unit Circle",
    "🌐 VR Environments": "VR Environments",
    "📖 Story Creator": "Story Creator",
    "📏 Clinometer Simulator": "Clinometer Simulator",
    "🧩 Puzzles & Games": "Puzzles & Games",
    "🎡 Spinner & Sketcher": "Spinner & Sketcher",
    "🎨 Radian Crafts": "Radian Crafts",
    "🚀 Motion & Waves": "Motion & Waves"
}

for icon_label, page_name in pages.items():
    if st.sidebar.button(icon_label, key=page_name):
        st.session_state.page = page_name

# Page Rendering
if st.session_state.page == "Encyclopedia":
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

elif st.session_state.page == "Trig Calculator":
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

elif st.session_state.page == "Quiz":
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
        answer = st.radio("Choose:", q["options"], key=f"quiz_{i}")
        if st.button(f"Submit Q{i+1}", key=f"submit_q{i}"):
            if answer == q["answer"]:
                st.success("Correct!")
                score += 1
            else:
                st.error(f"Wrong! Correct answer: {q['answer']}")

    if st.button("Show Score"):
        st.markdown(f"Your score: {score}/{len(questions)}")

elif st.session_state.page == "Real-World Applications":
    st.header("Real-World Applications of Trigonometry")
    st.markdown("""
    Trigonometry isn't just for math class—it's used everywhere in the real world! This section explores how trig helps in various fields. 
    Expand each section to learn more and see why understanding trig is so useful.
    """)

    with st.expander("1. Architecture and Construction"):
        st.markdown("""
        ### How Trig is Used:
        Architects and builders use trigonometry to calculate heights, angles, and distances. For example:
        - Determining the slope of a roof using tangent.
        - Calculating the height of a building by measuring angles from the ground (using sine or tangent).
        - Designing bridges or towers to ensure stability with force angles.
        
        **Example:** If you know the distance from a building and the angle of elevation to its top, tan(θ) = height / distance helps find the height.
        
        ### Visualization:
        Imagine a right triangle where the opposite side is the building height, adjacent is the ground distance, and θ is the angle.
        """)
        fig_arch, ax_arch = plt.subplots()
        ax_arch.plot([0, 5], [0, 0], 'b-')
        ax_arch.plot([5, 5], [0, 4], 'g-')
        ax_arch.plot([0, 5], [0, 4], 'r-')
        ax_arch.add_patch(Arc((0,0), 1, 1, theta1=0, theta2=math.degrees(math.atan(4/5)), color='purple'))
        ax_arch.text(0.5, 0.1, 'θ', color='purple')
        ax_arch.text(2.5, -0.2, 'Distance', color='b')
        ax_arch.text(5.1, 2, 'Height', color='g')
        ax_arch.set_xlim(0, 6)
        ax_arch.set_ylim(0, 5)
        ax_arch.axis('off')
        st.pyplot(fig_arch)

    with st.expander("2. Physics and Engineering"):
        st.markdown("""
        ### How Trig is Used:
        In physics, trig models projectile motion, waves, and forces. Engineers use it in mechanical, electrical, and civil fields.
        - Projectile paths: Horizontal (cos) and vertical (sin) components of velocity.
        - Electrical engineering: AC circuits with sine waves for voltage and current.
        - Mechanics: Resolving forces into components using sin and cos.
        
        **Example:** A ball thrown at an angle θ has initial velocity split as v_x = v * cos(θ), v_y = v * sin(θ).
        """)
        t = np.linspace(0, 2, 100)
        vx = 5 * np.cos(np.pi/4)
        vy = 5 * np.sin(np.pi/4) - 9.8 * t
        x = vx * t
        y = 5 * np.sin(np.pi/4) * t - 0.5 * 9.8 * t**2
        fig_phys, ax_phys = plt.subplots()
        ax_phys.plot(x, y, 'r-')
        ax_phys.set_title('Projectile Motion')
        ax_phys.set_xlabel('Horizontal Distance')
        ax_phys.set_ylabel('Vertical Height')
        ax_phys.grid(True)
        st.pyplot(fig_phys)

    with st.expander("3. Astronomy and Navigation"):
        st.markdown("""
        ### How Trig is Used:
        Astronomers calculate distances to stars using parallax (trig in triangles). Navigation uses trig for GPS and sailing.
        - Celestial navigation: Using angles to stars or sun to find position.
        - GPS: Triangulation with satellites involves spherical trig.
        
        **Example:** In sailing, the law of cosines helps calculate distances between points on Earth's surface.
        """)

    with st.expander("4. Medicine and Biology"):
        st.markdown("""
        ### How Trig is Used:
        In medical imaging like MRI or ultrasound, trig models waves and angles.
        - Ultrasound: Calculating reflection angles for imaging.
        - Optics in eyes: Trig in lens design and vision correction.
        
        **Example:** In ECG, heart rhythms are analyzed using sinusoidal waves.
        """)

    with st.expander("5. Computer Graphics and Gaming"):
        st.markdown("""
        ### How Trig is Used:
        3D modeling, animations, and games rely on trig for rotations, projections, and movements.
        - Rotating objects: Using sin and cos for transformations.
        - Lighting and shadows: Calculating angles of incidence.
        
        **Example:** In a game, a character's jump follows a parabolic path modeled by trig functions.
        """)

    with st.expander("6. Music and Sound Engineering"):
        st.markdown("""
        ### How Trig is Used:
        Sound waves are sinusoidal. Trig helps in synthesizing music and audio effects.
        - Fourier analysis: Breaking sounds into sine waves.
        - Tuning instruments: Harmonics based on wave frequencies.
        
        **Example:** A musical note's waveform is y = A * sin(2πft), where f is frequency.
        """)
        t_sound = np.linspace(0, 0.01, 1000)
        y_sound = np.sin(2 * np.pi * 440 * t_sound)
        fig_sound, ax_sound = plt.subplots()
        ax_sound.plot(t_sound, y_sound, 'b-')
        ax_sound.set_title('Sine Wave for Sound')
        ax_sound.set_xlabel('Time')
        ax_sound.set_ylabel('Amplitude')
        ax_sound.grid(True)
        st.pyplot(fig_sound)

    with st.expander("7. Surveying and Geography"):
        st.markdown("""
        ### How Trig is Used:
        Surveyors measure land using trig to find distances and heights.
        - Mapping: Triangulation for accurate maps.
        - Earthquakes: Seismology uses trig to locate epicenters.
        
        **Example:** Using theodolites to measure angles and calculate areas.
        """)

elif st.session_state.page == "AR Unit Circle":
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

elif st.session_state.page == "VR Environments":
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

elif st.session_state.page == "Story Creator":
    st.header("Digital Storytelling Project Builder")
    st.markdown("""
    Upload a photo of a real-life scenario (e.g., a slide or shadow), draw a triangle, and calculate trig values. Download your story as a PDF.
    """)
    
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Scenario")
        
        angle_deg = st.number_input("Angle of triangle (degrees)", value=30.0, key="story_angle")
        side_adj = st.number_input("Adjacent side length", value=5.0)
        angle_rad = math.radians(angle_deg)
        opposite = side_adj * math.tan(angle_rad)
        
        draw = ImageDraw.Draw(image)
        width, height = image.size
        x1, y1 = width * 0.2, height * 0.8
        x2, y2 = x1 + side_adj * 20, y1
        x3, y3 = x2, y1 - opposite * 20
        draw.line([(x1, y1), (x2, y2)], fill='blue', width=2)
        draw.line([(x2, y2), (x3, y3)], fill='green', width=2)
        draw.line([(x1, y1), (x3, y3)], fill='red', width=2)
        draw.text((x1 + 10, y1 - 20), f'θ = {angle_deg}°', fill='purple')
        
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        st.image(buf, caption="Triangle Overlay")
        
        st.markdown(f"""
        - Opposite: {opposite:.2f}
        - Adjacent: {side_adj:.2f}
        - Hypotenuse: {math.sqrt(opposite**2 + side_adj**2):.2f}
        """)
        
        if st.button("Generate Story PDF"):
            pdf_buffer = io.BytesIO()
            c = canvas.Canvas(pdf_buffer, pagesize=letter)
            c.drawString(100, 750, "Trigonometry Story")
            c.drawString(100, 730, f"Scenario: Analyzed a real-life triangle with angle {angle_deg}°")
            c.drawString(100, 710, f"Opposite: {opposite:.2f}, Adjacent: {side_adj:.2f}")
            img_buf = io.BytesIO()
            image.save(img_buf, format="PNG")
            c.drawImage(reportlab.lib.utils.ImageReader(img_buf), 100, 400, width=200, height=200)
            c.showPage()
            c.save()
            pdf_buffer.seek(0)
            st.download_button("Download Story PDF", pdf_buffer, "story.pdf", "application/pdf")

elif st.session_state.page == "Clinometer Simulator":
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

elif st.session_state.page == "Puzzles & Games":
    st.header("Puzzles & Games")
    st.markdown("Match ratios to triangles or identify quadrants in these fun challenges!")
    
    st.subheader("Ratio Matching Game")
    ratios = ["sin(θ) = 0.5", "cos(θ) = 0.5", "tan(θ) = 1"]
    triangles = ["Triangle A: Opp=3, Hyp=6", "Triangle B: Adj=3, Hyp=6", "Triangle C: Opp=4, Adj=4"]
    answers = {0: 0, 1: 1, 2: 2}
    
    selections = {}
    for i, ratio in enumerate(ratios):
        selections[ratio] = st.selectbox(f"Match {ratio}", triangles, key=f"ratio_{i}")
    
    if st.button("Check Matches"):
        correct = sum(1 for i, ratio in enumerate(ratios) if selections[ratio] == triangles[answers[i]])
        st.markdown(f"You got {correct}/{len(ratios)} correct!")

elif st.session_state.page == "Spinner & Sketcher":
    st.header("Paper Plate Spinner & Angle Sketcher")
    st.markdown("Spin the wheel to get a random angle, then sketch it in standard position.")
    
    if 'random_angle' not in st.session_state:
        st.session_state.random_angle = 0
    
    if st.button("Spin Wheel"):
        st.session_state.random_angle = np.random.randint(0, 360)
    
    angle_deg = st.session_state.random_angle
    angle_rad = math.radians(angle_deg)
    
    fig_spin, ax_spin = plt.subplots()
    ax_spin.add_patch(plt.Circle((0, 0), 1, color='lightblue', fill=False))
    ax_spin.plot([0, math.cos(angle_rad)], [0, math.sin(angle_rad)], 'r-')
    ax_spin.set_xlim(-1.2, 1.2)
    ax_spin.set_ylim(-1.2, 1.2)
    ax_spin.set_aspect('equal')
    ax_spin.axis('off')
    st.pyplot(fig_spin)
    
    st.markdown(f"Angle: {angle_deg}°")
    coterminal = st.number_input("Enter a coterminal angle (degrees)", key="coterm")
    if st.button("Check Coterminal"):
        if (coterminal % 360) == (angle_deg % 360):
            st.success("Correct coterminal angle!")
        else:
            st.error("Try again!")

elif st.session_state.page == "Radian Crafts":
    st.header("Radian Exploration with Arts and Crafts")
    st.markdown("Arrange sectors to form a circle and visualize radians.")
    
    num_sectors = st.slider("Number of sectors (each π/3 radians)", 1, 12, 6)
    sector_angle = np.pi / 3
    
    fig_craft, ax_craft = plt.subplots()
    for i in range(num_sectors):
        theta = np.linspace(i * sector_angle, (i + 1) * sector_angle, 100)
        x = np.cos(theta)
        y = np.sin(theta)
        ax_craft.fill_betweenx(y, 0, x, alpha=0.3, color=plt.cm.rainbow(i/num_sectors))
    ax_craft.set_xlim(-1.2, 1.2)
    ax_craft.set_ylim(-1.2, 1.2)
    ax_craft.set_aspect('equal')
    ax_craft.axis('off')
    st.pyplot(fig_craft)
    
    if st.button("Generate Printable PDF"):
        pdf_buffer = io.BytesIO()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        c.drawString(100, 750, "Radian Craft Template")
        c.drawString(100, 730, f"Cut out {num_sectors} sectors, each π/3 radians")
        c.showPage()
        c.save()
        pdf_buffer.seek(0)
        st.download_button("Download Craft PDF", pdf_buffer, "radian_craft.pdf", "application/pdf")

elif st.session_state.page == "Motion & Waves":
    st.header("Projectile Motion & Wave Animations")
    st.markdown("Adjust parameters to see how trig models motion and waves.")
    
    angle_deg = st.slider("Launch angle (degrees)", 0, 90, 45, key="motion_angle")
    velocity = st.number_input("Initial velocity (m/s)", value=10.0)
    
    angle_rad = math.radians(angle_deg)
    t = np.linspace(0, 2 * velocity * np.sin(angle_rad) / 9.8, 100)
    x = velocity * np.cos(angle_rad) * t
    y = velocity * np.sin(angle_rad) * t - 0.5 * 9.8 * t**2
    y = np.maximum(y, 0)
    
    fig_motion, ax_motion = plt.subplots()
    ax_motion.plot(x, y, 'r-')
    ax_motion.set_title('Projectile Motion')
    ax_motion.set_xlabel('Horizontal Distance (m)')
    ax_motion.set_ylabel('Height (m)')
    ax_motion.grid(True)
    st.pyplot(fig_motion)
    
    st.subheader("Sound Wave")
    freq = st.slider("Frequency (Hz)", 100, 1000, 440)
    t_wave = np.linspace(0, 0.01, 1000)
    y_wave = np.sin(2 * np.pi * freq * t_wave)
    fig_wave, ax_wave = plt.subplots()
    ax_wave.plot(t_wave, y_wave, 'b-')
    ax_wave.set_title('Sound Wave')
    ax_wave.set_xlabel('Time (s)')
    ax_wave.set_ylabel('Amplitude')
    ax_wave.grid(True)
    st.pyplot(fig_wave)
