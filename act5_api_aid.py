from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id":1, "nombre":"corpi", "enable":True},
    {"id":2, "nombre":"vinaja", "enable":True},
    {"id":3, "nombre":"beto", "enable":True},
    {"id":4, "nombre":"jessie", "enable":True},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True)