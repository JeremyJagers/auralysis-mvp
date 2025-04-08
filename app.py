from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "your_openai_api_key"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    playlist_url = data.get("playlistUrl")

    # Simulate song parsing (in practice you'd pull from Spotify API)
    songs = [
        "Nights by Frank Ocean",
        "Motion Picture Soundtrack by Radiohead",
        "After Dark by Mr. Kitty",
        "505 by Arctic Monkeys"
    ]

    prompt = f"""You are an emotionally intelligent AI trained in musical psychology and symbolic analysis.
A user submitted a playlist:
{chr(10).join(songs)}

Provide a 3-paragraph psychological snapshot, a one-line archetype, and a poetic summary of the listener."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    analysis = response['choices'][0]['message']['content']
    return jsonify({ "analysis": analysis })