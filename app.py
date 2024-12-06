from flask import Flask, request, jsonify
from database import get_form_template, create_test_db
from validators import get_field_type
app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    fields = request.form.to_dict()
    if not fields:
        return jsonify({"error": "No data provided"}), 400

    matching_template = get_form_template(fields)

    if matching_template:
        return jsonify({"form_name": matching_template['name']})

    field_types = {}
    for field_name, field_value in fields.items():
        field_type = get_field_type(field_value)
        field_types[field_name] = field_type

    return jsonify(field_types)


if __name__ == "__main__":
    create_test_db()
    app.run(debug=True)
