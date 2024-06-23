# Image Gallery

A simple booru-like image gallery application built with Flask. This project allows users to upload and view images, providing a basic interface for an image gallery.

## Features
- Display images uploaded by users
- Upload new images through a web form
- Hover effect to slightly enlarge images
- Click on images to view a larger version in a modal

## Installation

1. Clone the repository:

```bash
git clone https://github.com/augustovillamediana/imagegallery
cd image-gallery
```

2. Start the app.:

This will automatically create a virtual environment and install dependencies:

```bash
./start.sh
```

3. Access the application:

Open your web browser and navigate to http://127.0.0.1:5000

## Configuration

You can update the configuration settings in the config.txt file:

```txt
UPLOAD_FOLDER=uploads
ALLOWED_EXTENSIONS=jpg,jpeg,png,gif
MAX_CONTENT_LENGTH=16 * 1024 * 1024 # 16 MB
```

## Folder Structure

```plain
image-gallery/
│
├── static/
│ ├── uploads/
│ ├── styles.css
│
├── templates/
│ └── index.html
│
├── app/
│ ├── init.py
│ ├── routes.py
│ └── db.py
│
├── config.txt
├── main.py
├── requirements.txt
├── start.sh
└── README.md
```

## License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.