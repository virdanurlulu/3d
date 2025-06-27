# app.py
from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    solution = ""
    if request.method == "POST":
        question = request.form["question"]
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}],
            max_tokens=500
        )
        solution = response.choices[0].message['content'].strip()
    return render_template("index.html", solution=solution)

if __name__ == "__main__":
    app.run(debug=True)
