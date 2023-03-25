from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    print(user['name'], user['age'])
    return jsonify("ok")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)