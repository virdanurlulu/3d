# app.py
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    question = data.get("question", "")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        max_tokens=500,
        temperature=0.2
    )
    solution = response.choices[0].message['content'].strip()
    return jsonify({"solution": solution})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
