from flask import Flask, request, Blueprint
import json

password_parameters = {
    "length": 10,
    "must_have_numbers": True,
    "must_have_caps": True
}


# function to check if some character is upper case
def checkCaps(pwd):
    if any(ele.isupper() for ele in pwd):
        return True
    return False


# function to check if some character is a number
def checkNumber(pwd):
    if any(ele.isdigit() for ele in pwd):
        return True
    return False


# general function to check if the password is correct
def passwordCheck(password):
    is_correct = False

    if isinstance(password, str) and len(password) == password_parameters['length']:
        if password_parameters['must_have_caps']:
            is_correct = checkCaps(password)
            if not is_correct: return False
        if password_parameters['must_have_numbers']:
            is_correct = checkNumber(password)
            if not is_correct: return False
    return is_correct


# function to create basic flask app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app


bp = Blueprint('myapp', __name__)


@bp.route('/password_check', methods=['GET'])
def password_check():
    json_data = request.json
    password = json_data["password"]
    return json.dumps({'response': passwordCheck(password)}), 200


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
