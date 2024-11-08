from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import io

app = Flask(__name__)

# Font and image configuration
font_path = r"C:\Users\hp\Desktop\Teaching Assistant\ABC\Python\text_to_handwritting\ShantellSans-Italic-VariableFont_BNCE,INFM,SPAC,wght.ttf"
font_size = 20
text_color = (0, 0, 138)  # RGB color for the text (blue)
image_width = 800
line_spacing = 10  # Space between lines

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get text from form
        text = request.form.get('text', '')

        # Check if text is provided
        if not text.strip():
            return "Please enter some text to generate handwriting."

        # Load the handwriting font
        try:
            font = ImageFont.truetype(font_path, font_size)
        except OSError:
            return "Error: Font not found. Please ensure the font file path is correct."

        # Split text into lines and calculate image height
        lines = text.splitlines()
        line_height = font.getbbox("A")[3] + line_spacing  # Calculate line height
        image_height = line_height * len(lines) + 20  # Total image height with padding

        # Create a blank white image
        image = Image.new("RGB", (image_width, image_height), color="white")
        draw = ImageDraw.Draw(image)

        # Draw the text line by line
        y_text = 10
        for line in lines:
            draw.text((10, y_text), line, font=font, fill=text_color)
            y_text += line_height

        # Save the image to a BytesIO object
        img_io = io.BytesIO()
        image.save(img_io, 'PNG')
        img_io.seek(0)

        # Return image as a response
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name="handwritten_text.png")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
