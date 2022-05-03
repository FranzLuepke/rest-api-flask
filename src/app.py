from flask import Flask, jsonify

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
    pass

# GET /store
@app.route('/store/<string:name>')
def get_store(name):
    pass

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
    pass

app.run(port=5000)
