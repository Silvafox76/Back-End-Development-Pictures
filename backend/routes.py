from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa: F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################
@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################
@app.route("/count")
def count():
    """Return length of data"""
    if data:
        return jsonify(length=len(data)), 200
    return {"message": "Internal server error"}, 500

######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    """Return the list of all pictures"""
    return jsonify(data), 200

######################################################################
# GET A PICTURE BY ID
######################################################################
@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    """Return a picture by its ID"""
    for pic in data:
        if pic.get("id") == id:
            return jsonify(pic), 200
    return {"error": "Picture not found"}, 404

######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    """Create a new picture"""
    if request.json:
        new_picture = request.json
        # Check if ID already exists
        for pic in data:
            if pic.get("id") == new_picture.get("id"):
                return jsonify({"Message": f"picture with id {new_picture['id']} already present"}), 302
        data.append(new_picture)
        return jsonify(new_picture), 201
    return {"error": "Invalid request"}, 400

######################################################################
# UPDATE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    """Update a picture by ID"""
    for idx, pic in enumerate(data):
        if pic.get("id") == id:
            data[idx] = request.json
            return jsonify(data[idx]), 200
    return {"error": "Picture not found"}, 404

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    """Delete a picture by ID"""
    for idx, pic in enumerate(data):
        if pic.get("id") == id:
            del data[idx]
            return {}, 204
    return {"error": "Picture not found"}, 404

