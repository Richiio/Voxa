from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    mode = request.form.get('mode')  # 'audio', 'image', or 'video'
    if file:
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)

        # Dummy extract logic (replace with model inference)
        if mode == 'audio':
            text = "Transcribed audio text..."
        elif mode == 'image':
            text = "Extracted text from image..."
        elif mode == 'video':
            text = "Extracted speech from video..."
        else:
            text = "Unknown mode"

        return jsonify({"status": "completed", "text": text})
    return jsonify({"status": "failed"})
