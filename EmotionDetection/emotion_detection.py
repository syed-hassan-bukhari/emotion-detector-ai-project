import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Handle blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=headers)

    if response.status_code == 400:  # Handle invalid text or empty input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_data = response.json()
    emotion_predictions = response_data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

    return {
        'anger': emotion_predictions['anger'],
        'disgust': emotion_predictions['disgust'],
        'fear': emotion_predictions['fear'],
        'joy': emotion_predictions['joy'],
        'sadness': emotion_predictions['sadness'],
        'dominant_emotion': dominant_emotion
    }
