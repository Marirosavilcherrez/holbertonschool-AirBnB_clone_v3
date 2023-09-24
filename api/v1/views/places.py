#!/usr/bin/python3
"""objects that handle all default REStfull api actions for places"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models.place import Place
from models import storage


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places():
    """retrives the list of places"""
    all_places = storage.all(Place).values()
    list_places = []
    for place in all_places:
        list_places.append(place.to_dict())
    return jsonify(list_places)


@app_views.route('/places/<place_id>',
                 methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """retrives users of objects"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    storage.delete(place)
    storage.save()

    return make_response(jsonify({}, 200))


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def post_place():
    """create a place"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    if 'user_id' not in request.get_json(User):
        abort(400)

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Place(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/places/<place_id>',
                 methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """update an place object"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']

    user = storage.get(Place, place_id)

    if not place:
        abort(404)

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)
