from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/PCHardwareInvent"
mongo = PyMongo(app)

# CREATE
@app.route('/add/<collection>', methods=['POST'])
def add_item(collection):
    _json = request.json
    _atribut1 = _json['atribut1']
    _value1 = _json['value1']
    _atribut2 = _json['atribut2']
    _value2 = _json['value2']
    _atribut3 = _json['atribut3']
    _value3 = _json['value3']

    if _atribut1 and _value1 and _atribut2 and _value2 and _atribut3 and _value3 and request.method == 'POST':
        id = mongo.db[collection].insert({_atribut1: _value1, _atribut2: _value2, _atribut3: _value3})
        resp = jsonify("Item added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

# READ ALL FROM ONE COLLECTION
@app.route('/items/<collection>')
def items(collection):
    items = mongo.db[collection].find()
    resp = dumps(items)
    return resp

# READ ALL FROM ALL COLLECTIONS
@app.route('/allitems')
def all_items():
    collections = ['RAM', 'SSD', 'Motherboard', 'Processor']
    all_items = {collection: dumps(mongo.db[collection].find()) for collection in collections}
    return jsonify(all_items)

# UPDATE
@app.route('/update/<collection>/<id>', methods=['PUT'])
def update_item(collection, id):
    _json = request.json
    _atribut1 = _json['atribut1']
    _value1 = _json['value1']
    _atribut2 = _json['atribut2']
    _value2 = _json['value2']
    _atribut3 = _json['atribut3']
    _value3 = _json['value3']

    if _atribut1 and _value1 and _atribut2 and _value2 and _atribut3 and _value3 and request.method == 'PUT':
        mongo.db[collection].update_one({'_id': ObjectId(id)}, {'$set': {_atribut1: _value1, _atribut2: _value2, _atribut3: _value3}})
        resp = jsonify("Item updated successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

# DELETE
@app.route('/delete/<collection>/<id>', methods=['DELETE'])
def delete_item(collection, id):
    mongo.db[collection].delete_one({'_id': ObjectId(id)})
    resp = jsonify("Item deleted successfully")
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)
