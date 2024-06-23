    #!/bin/bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install -r requirements.txt

# Create uploads directory if it doesn't exist
mkdir -p uploads

# Run the Flask application
export FLASK_APP=app.py
export FLASK_DEBUG=True
flask run
