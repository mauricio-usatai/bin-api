import json
from pydoc import cli
import redis
from flask import request, jsonify

import app as App
from app import app
from app.auth import check_auth_key
from app.redis import RedisClient

@app.route('/version')
def version():
  return jsonify({ 'version': App.Config.VERSION })

@app.route('/bin/<bin_id>', methods=['GET', 'POST'])
def bin(bin_id):
  if not request.args.get('key', None):
    return jsonify({ 'message': 'api key not provided' }), 401
  if not check_auth_key(request.args.get('key')):
    return jsonify({ 'message': 'api key not valid' }), 401

  if request.method == 'GET':
    client = RedisClient.get_client()
    data = client.get(bin_id)
    if data:
      data = json.loads(data)
      return jsonify({ 'data': data }), 200
    else: 
      return jsonify({ 'message' : f'bin {bin_id} not found' }), 404
  
  if request.method == 'POST':
    post_data = request.get_json()

    if not post_data.get('data', None):
      return jsonify({ 'message': 'mandatory field: "data"' }), 400

    client = RedisClient.get_client()
    client.set(bin_id, json.dumps(post_data.get('data')))

    return jsonify({ bin_id: post_data }), 201
