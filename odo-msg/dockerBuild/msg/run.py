#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS
import connexion
import logging

logging.basicConfig(level=logging.INFO, format='[ %(asctime)s ] %(levelname)s %(message)s')

if __name__ == '__main__':
    app = Flask(__name__)
    CORS(app)
    options = {
        "swagger_ui": True
    }
    app = connexion.FlaskApp(
        __name__,
        specification_dir='specs/',
        options=options
    )
    app.add_api("msg.yaml")
    app.run(port=80, debug=True)
