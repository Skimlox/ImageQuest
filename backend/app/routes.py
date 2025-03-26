from flask import Flask, request, jsonify
from flask_cors import CORS
from app import app


@app.route('/index', methods=['GET'])
def index():
    return jsonify({"message": "Flask is working!"})



