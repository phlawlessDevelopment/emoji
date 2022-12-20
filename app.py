from flask import Flask, request, render_template

from blender_emoji import load_from_json

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=['GET', 'POST'])
def home():
    output = []
    if request.method == 'POST':
        json_data = load_from_json("emoji.json")
        output = json_data.get(request.form['prompt'].lower())
        if output is None:
            output.append('Not found')
    return render_template("index.html", data=output)
