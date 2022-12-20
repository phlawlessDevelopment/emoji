from flask import Flask, request, render_template
from blender_emoji import load_from_json

app = Flask(__name__, template_folder="templates")


@app.route("/", methods=['GET', 'POST'])
def home():
    output = []
    if request.method == 'POST':

        prompt = request.form['prompt'].lower()
        json_data = load_from_json("emoji.json")
        output = json_data.get(prompt, None)

        if output is None:
            output.append('Not found')

    return render_template("index.html", data=output)
