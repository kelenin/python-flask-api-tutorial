from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos =[
    {"label": "My first task", "done": False},
    {"label": "My second task","done": False}
]

data = [
    { "done": True, "label": "Sample Todo 1"}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'
    #decoded_object = json.loads(request_body)
    #p= decoded_object.append(todos)
    #return jsonify(p)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)