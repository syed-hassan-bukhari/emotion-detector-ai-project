"""
Emotion Detector Flask App
This module provides a web interface for detecting emotions from text input
using the emotion_detector function from EmotionDetection package.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the home page with an input form for emotion detection.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect emotions from the text input provided by the user.
    Returns a formatted string containing detected emotions and dominant emotion.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is '{response['dominant_emotion']}'."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

