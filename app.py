from flask import Flask, render_template, jsonify, request
import json, os

app = Flask(__name__)

def available_curricula():
    """List all .json curricula in the app root."""
    files = [f for f in os.listdir(os.path.dirname(__file__)) if f.endswith(".json")]
    return sorted(files)

def load_curriculum(filename):
    """Safely load a JSON file."""
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    filename = request.args.get("file", "curr_gis.json")
    curriculum = load_curriculum(filename)
    return render_template(
        "curriculum.html",
        curriculum=curriculum,
        filename=filename,
        files=available_curricula()
    )

@app.route("/api/<path:filename>")
def api_curriculum(filename):
    return jsonify(load_curriculum(filename))

if __name__ == "__main__":
    app.run(debug=True)
