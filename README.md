# Repository for final project
A Flask-based web application that analyzes emotions in a given text statement using the Watson NLP library.

## Features
- Detects emotions from a text statement via a REST API endpoint
- Returns confidence scores for each emotion
- Identifies the dominant emotion

## Requirements
- Python 3.10+
- Flask
- Requests

## Installation
1. Clone the repository and navigate to the project directory.
2. Install the dependencies: `pip install flask` and `pip install requests`

## Usage
1. Start the server: `python3 server.py`
2. The server will run on `http://localhost:5000`.
3. Call the emotion detector endpoint with a statement:
```
curl "http://localhost:5000/emotionDetector?statement=I%20think%20I%20am%20having%20fun"
```

## API
GET `/emotionDetector`
Analyzes the emotions in a given text statement.

### Query Parameter:
`statement` (str) — The text to analyze

### Example Response:
```
For the given statement, the system response is 'anger': 0.006274985,
'disgust': 0.0025598293, 'fear': 0.009251528, 'joy': 0.9680386 and
'sadness': 0.049744144. The dominant emotion is joy.
```
