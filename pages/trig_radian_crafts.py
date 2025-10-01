import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

def show_trig_radian_crafts():
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
