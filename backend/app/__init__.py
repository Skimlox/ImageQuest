from flask import Flask
from .config import Config
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  


from app import routes
if __name__ == "__main__":
    app.run(debug=True)