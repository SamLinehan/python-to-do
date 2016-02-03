from flask import Flask, jsonify
app = Flask(__name__)


tasks = [
    {
    "id": 1,
    "title": "Go grocery shopping",
    "description": "Eggs, ground beef, spinach",
    "done": False
    },
    {
    "id": 2,
    "title": "Study Python",
    "description": "Make an API",
    "done": True
    }
]

@app.route("/todo/api/v1.0/tasks")
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/")
# def index():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run(debug=True)
