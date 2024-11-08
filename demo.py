from PIL import Image, ImageDraw, ImageFont

# Text to convert to handwriting-style image
text = """
Diabetic retinopathy (DR) is a condition of the eye that threatens the sight of millions of individuals with diabetes,
leading to irreversible blindness if not addressed early. The classical method of screening involves extended examination
time of humans, which in turn is error-prone, and delayed diagnoses and poor patient management are the results. 
Advancements in the machine learning (ML) field constitute the automating of DR detection system, which can enhance the 
efficiency and the accuracy of the diagnoses. The existing approaches are entirely based on deep learning algorithms 
and, to be more exact, Convolutional Neural Networks (CNN), which are able to examine retinal images for different 
states of the disease. So, the final result of this study demonstrates a novel approach that integrates sophisticated 
machine learning with the internet of things-based devices to automatically screen DR. This system not only addresses 
the constraints of the conventional screening process, but also tends to improve patient outcomes and minimize the 
overall threat of vision loss.
"""

# Specify font and image parameters
font_path = r"C:\Users\hp\Desktop\Teaching Assistant\ABC\Python\text_to_handwritting\ShantellSans-Italic-VariableFont_BNCE,INFM,SPAC,wght.ttf"
font_size = 20
text_color = (0, 0, 138)  # RGB color for the text (blue)
image_width = 800
line_spacing = 10  # Space between lines

# Load the handwriting font
try:
    font = ImageFont.truetype(font_path, font_size)
except OSError:
    print("Error: Shantell Sans Light font not found. Please ensure the font file is in the correct path.")
    exit()

# Split text into lines and calculate image height
lines = text.splitlines()
line_height = font.getbbox("A")[3] + line_spacing  # Calculate line height using textbbox
image_height = line_height * len(lines) + 20  # Total image height with padding

# Create a blank white image
image = Image.new("RGB", (image_width, image_height), color="white")
draw = ImageDraw.Draw(image)

# Draw the text line by line
y_text = 10
for line in lines:
    draw.text((10, y_text), line, font=font, fill=text_color)
    y_text += line_height

# Save the image
image.save("notebook_handwritten.png")
print("Image saved as notebook_handwritten.png")
