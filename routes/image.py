from flask import Blueprint, request, jsonify
import os
from app import db
from models import Image

bp = Blueprint('image', __name__)

@bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = os.path.join(os.getenv('UPLOAD_FOLDER', 'uploads/'), file.filename)
        file.save(file_path)
        new_image = Image(file_path=file_path, uploader_id=request.form['uploader_id'])
        db.session.add(new_image)
        db.session.commit()
        return jsonify({'message': 'File uploaded successfully'})

@bp.route('/images', methods=['GET'])
def get_images():
    images = Image.query.all()
    images_list = [{'file_path': image.file_path} for image in images]
    return jsonify({'images': images_list})
