import flask
from flask import request

from data_preocessing import item_similarity, popularity

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    user_id = request.args['user_id']
    response = item_similarity(user_id)
    print(response['song'])
    js = response['song'].to_json(orient='split')
    return js


# @app.route('/popularity', methods=['GET'])
# def popularity():
#     user_id = request.args['user_id']
#     response = popularity(user_id)
#     print(response)
#     js = response['song'].to_json()
#     return js


# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port=5000)
