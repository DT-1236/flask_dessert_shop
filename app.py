from flask import Flask, render_template, jsonify, request, session
from desserts import dessert_list

app = Flask(__name__)
app.config['SECRET_KEY'] = "Cakes and Pies"


@app.route("/")
def home():
    """Return home page with basic info"""

    return render_template("index.html")


@app.route("/desserts")
def get_all_desserts():
    """Return JSON containing all dessert info"""

    return jsonify(dessert_list.serialize())


@app.route("/desserts/<int:dessert_id>")
def get_one_dessert(dessert_id):
    """Return JSON containing all dessert info"""

    dessert = dessert_list.find(dessert_id)
    if dessert:
        return jsonify(dessert.serialize())
    else:
        return generate_missing_id_response(dessert_id)


@app.route("/desserts", methods=['POST'])
def add_new_dessert():
    """Add a new dessert!"""
    json = request.json
    # We can get fancy later and handle requests that were not properly signed as JSON
    assert json['name'] and json['description'] and isinstance(
        json['calories'],
        (int, float)), "Incoming Dessert Parameters are incomplete"
    dessert_list.add(json['name'], json['description'], json['calories'])

    return jsonify(dessert_list.desserts[-1].serialize())


@app.route("/desserts/<int:dessert_id>/eat", methods=['POST'])
def eat_dessert(dessert_id):
    dessert = dessert_list.find(dessert_id)
    if not dessert:
        return generate_missing_id_response(dessert_id)

    session['total_calories'] = session.get('total_calories',
                                            0) + dessert.calories

    return jsonify({"total_calories": session['total_calories']})


@app.route("/desserts/<int:dessert_id>", methods=['PUT', 'PATCH'])
def update_existing_dessert(dessert_id):
    json = request.json
    dessert = dessert_list.find(dessert_id)
    if not dessert:
        return generate_missing_id_response(dessert_id)

    name = json.get('name')
    description = json.get('description')
    calories = json.get('calories')

    if name:
        dessert.name = name
    if description:
        dessert.name = description
    if isinstance(calories, (int, float)):
        dessert.calories = calories

    return jsonify(dessert.serialize())


@app.route("/desserts/<int:dessert_id>", methods=['DELETE'])
def delete_existing_dessert(dessert_id):
    dessert = dessert_list.find(dessert_id)
    if not dessert:
        return generate_missing_id_response(dessert_id)
    dessert_list.desserts.remove(dessert)
    return jsonify(dessert.serialize())


def generate_missing_id_response(id):
    response = jsonify(f"No dessert with id {id}")
    response.status_code = 404
    return response
