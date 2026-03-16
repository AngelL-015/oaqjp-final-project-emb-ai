"""
Flask server for the Emotion Detector application.
"""

from flask import Flask, request
import EmotionDetection as ed

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector():
    """
    Analyzes the emotions in a given text statement

    Retrieves a query parameter 'statement' from the URL and passes it 
    to the emotion detector. Returns a formatted string containing each 
    emotion with its confidence score, and the dominant emotion.

    Args:
        statement (str): The text to analyze, passed as a URL query parameter

    Returns:
        str: A formatted string listening all emotion scores and the dominant emotion.
        e.g. "For the given statement, the system response is 'anger': 0.006,
        'joy': 0.96 and 'sadness': 0.04. The dominant emotion is joy."
    """
    statement = request.args.get('statement')
    response = ed.emotion_detector(statement)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!\n"

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
