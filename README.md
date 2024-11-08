# Handwriting Generator Web App

This is a simple web app that converts user input text into a handwritten-style image. It uses **Flask** as the backend and **Pillow** for generating the handwritten-style images. The font used for the handwriting effect is **Shantell Sans Light**.

## Features
- Users can input text via a form.
- The app converts the text into a handwritten image.
- The generated image is returned to the user for download.

## Technologies Used
- **Flask**: A lightweight Python web framework.
- **Pillow**: A Python Imaging Library used to generate the image.
- **HTML/CSS**: For creating the front-end form.

## Requirements
Make sure to install the following Python libraries:

1. Flask
2. Pillow

You can install them using `pip`:

```bash
pip install flask pillow
```

## Setup Instructions

1. **Clone this repository or download the code**.

2. **Ensure you have the required font file**:
   - Download the **Shantell Sans Light** font (or the one you want to use).
   - Place the font file in the appropriate directory, and update the `font_path` in the `app.py` file to point to the correct location of the `.ttf` font file.

   Example (if your font is located in the project directory):
   ```python
   font_path = r"C:\path\to\your\font\ShantellSans-Italic-VariableFont_BNCE,INFM,SPAC,wght.ttf"
   ```

3. **Run the Flask app**:
   Navigate to the project folder in your terminal, then run:

   ```bash
   python app.py
   ```

   This will start the Flask server, and you can access the web app at `http://127.0.0.1:5000/`.

4. **Use the web app**:
   - Open a browser and visit `http://127.0.0.1:5000/`.
   - Enter the text you want to convert into handwriting and click "Generate Handwriting."
   - The generated handwritten image will be available for download.

## Project Structure

```
/handwriting-generator
    ├── app.py                # Main Flask application
    ├── /templates
    │   └── index.html        # HTML form for user input
    ├── /static
    │   └── (optional)        # Any static files (e.g., CSS, images)
    ├── README.md             # This README file
    └── requirements.txt      # List of dependencies (Flask, Pillow)
```

## Troubleshooting

- If you receive the error `HTTP ERROR 405`, make sure your form uses `method="POST"` in `index.html`.
- If the image isn't being generated, check that the **font path** is correct, and the font file exists.

### How to Use the README:

1. **Project Overview**: Describes the purpose of the project.
2. **Technologies Used**: Lists the technologies and libraries used.
3. **Setup Instructions**: Walks the user through installation and running the app.
4. **Project Structure**: Explains the file structure and organization.
5. **Troubleshooting**: Provides common issues and their solutions.

### Add Dependencies

You can also add a `requirements.txt` file for easy installation of dependencies:

```
Flask
Pillow
```

This way, others can install everything by running:
```bash
pip install -r requirements.txt
```

Let me know if you'd like any changes or further details!
