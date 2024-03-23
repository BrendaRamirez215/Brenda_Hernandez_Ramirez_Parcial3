from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nombre":"Martha", "enable":True},
    {"id":2, "nombre":"China", "enable":False},
    {"id":3, "nombre":"Karem", "enable":True},
    {"id":4, "nombre":"Sara", "enable":False}
]

@app.route('/tasks', methods=['GET'])
def get_tasks(): 
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)