from flask import Flask, request
import EmotionDetection as ed

app = Flask(__name__)

@app.route("/emotionDetector")
def emotionDetector():
    statement = request.args.get('statement')
    response = ed.emotion_detector(statement)

    result = "For the given statement, the system response is "

    # Build a list of (emotion, score) pairs, excluding "dominant_emotion"
    emotions = [(k, v) for k, v in response.items() if k !="dominant_emotion"]
    
    for i, (emotion, score) in enumerate(emotions):
        result += f"'{emotion}': {score}"

        if i == len(emotions) - 2:
            result += " and "
        elif i < len(emotions) - 1:
            result += ", "
            
    result += f". The dominant emotion is {response['dominant_emotion']}.\n"

    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
