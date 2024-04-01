#!/usr/bin/python3
<<<<<<< HEAD
"""states.py"""
=======
"""
THE State Endpoints for AN  API
"""
>>>>>>> e56c0be3cb236f4e008a46784f036884691339a2

from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage
from models.state import State
from flask import abort, request, jsonify


<<<<<<< HEAD
@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """get state information for all states"""
    states = []
    for state in storage.all("State").values():
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """get state information for specified state"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """deletes a state based on its state_id"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return (jsonify({}))


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """create a new state"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """update a state"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for attr, val in request.get_json().items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(state, attr, val)
    state.save()
    return jsonify(state.to_dict())
=======
@app_views.route('/states', methods=['GET', 'POST'])
def states():
    """Return status OK for status route"""
    if request.method == 'GET':
        states = []
        for state in storage.all(State).values():
            states.append(state.to_dict())
        return jsonify(states), 200
    if request.method == "POST":
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        name = body.get('name')
        if not name:
            abort(400, "Missing name")
        state = State(**body)
        state.save()
        return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def state_id(state_id):
    """Return status OK for status route"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if request.method == 'GET':
        return jsonify(state.to_dict()), 200
    if request.method == 'PUT':
        forbidden = ['id', 'created_at', 'updated_at']
        if not state:
            abort(404)
        try:
            body = request.get_json()
        except Exception:
            abort(400, "Not a JSON")
        for key, val in body.items():
            if key not in forbidden:
                setattr(state, key, val)
        state.save()
        return jsonify(state.to_dict()), 200
    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return jsonify({}), 200
>>>>>>> e56c0be3cb236f4e008a46784f036884691339a2
