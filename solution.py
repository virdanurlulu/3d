# file: auto_ai_solution.py

import openai

def generate_solution(question, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4",  # atau "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "Kamu adalah asisten AI yang menganalisa masalah dan memberikan solusi logis."},
            {"role": "user", "content": question}
        ],
        max_tokens=500,
        temperature=0.2
    )
    return response.choices[0].message['content'].strip()

if __name__ == "__main__":
    api_key = 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"
    pertanyaan = input("Masukkan pertanyaan/masalah: ")
    solusi = generate_solution(pertanyaan, api_key)
    print("\nAnalisa & Solusi AI:\n", solusi)
