from flask import Flask, jsonify, request

stores = [
    {
        'name': 'Store',
        'items': [
            {
                'name': 'pc',
                'price': 1000,
            }
        ]
    }
]

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, world!"

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store) 

# GET /store
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': f'Store {name!r} not found.'})
# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'Store {name!r} not found.'})

app.run(port=5000)
