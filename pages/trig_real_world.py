import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

def show_trig_real_world():
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
        ax_arch.add_patch(Arc((0,0), 1, 1, theta1=0, theta2=np.degrees(np.atan(4/5)), color='purple'))
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
