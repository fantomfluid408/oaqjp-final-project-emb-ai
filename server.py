''' Executing this function initiates the application of emotion detection to be executed 
    over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initial the flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emotion_detection():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detector()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
        # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the label and score from the response
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emo = response['dominant_emotion']
    if dominant_emo is None:
        return "Invalid text! Please try again!. "
    return (f"For the given statement, the system response is "
            f"'anger': {anger_score}, "
            f"'disgust': {disgust_score}, "
            f"'fear': {fear_score}, "
            f"'joy': {joy_score} and 'sadness': {sadness_score}." 
            f"The dominant emotion is {dominant_emo}.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
