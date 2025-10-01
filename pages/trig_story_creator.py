import streamlit as st
import math
from PIL import Image, ImageDraw
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def show_trig_story_creator():
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
