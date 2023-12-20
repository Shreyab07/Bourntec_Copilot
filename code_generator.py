

from flask import Flask, request
import openai

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"

@app.route('/code', methods=['POST'])
def generate_code():
    prompt = request.form['prompt']

    response = openai.Completion.create(
        engine="code-davinci-002",
        prompt=prompt,
        max_tokens=500,
        n=1,
        temperature=0
    )

    code = response['choices'][0]['text']
    
    return code

if __name__ == '__main__':
    app.run()