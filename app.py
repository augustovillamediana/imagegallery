from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from models import db, Image

app = Flask(__name__)

# Load configuration from config.txt
with open('config.txt') as config_file:
    for line in config_file:
        name, value = line.strip().split('=', 1)
        app.config[name] = value

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        new_image = Image(file_path=file_path)
        db.session.add(new_image)
        db.session.commit()
        return jsonify({'message': 'File uploaded successfully'})

@app.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    images_list = [{'file_path': image.file_path} for image in images]
    return jsonify({'images': images_list})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
