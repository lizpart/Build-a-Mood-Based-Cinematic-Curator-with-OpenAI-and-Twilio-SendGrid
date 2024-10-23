from flask import Flask, request, render_template, jsonify
import openai
import os
from transformers import pipeline
import torch
from dotenv import load_dotenv 
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
tmdb_api_key = os.getenv('TMDB_API_KEY')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
senders_email= os.getenv('SENDGRID_FROM_EMAI')

classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

def get_movie_details(title):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={tmdb_api_key}&query={title}"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json()['results']
        if results:
            movie = results[0]
            return {
                'title': movie['title'],
                'poster': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie['poster_path'] else None,
                'link': f"https://www.themoviedb.org/movie/{movie['id']}"
            }
    return None

def send_recommendation_email(to_email, emotion, movies):
    message = Mail(
        from_email='senders_email',
        to_emails=to_email,
        subject='Your Movie Recommendations Based on Your Mood',
        html_content=f'''
        <h2>Your detected mood: {emotion}</h2>
        <h3>Here are your movie recommendations:</h3>
        <ul>
        {''.join([f"<li><a href='{movie['link']}'>{movie['title']}</a></li>" for movie in movies])}
        </ul>
        ''')
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email sent. Status code: {response.status_code}")
        return True
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return False

@app.route('/')
def index():
    return render_template('mood_check.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        user_input = request.form['user_input']
        user_email = request.form.get('user_email')
        app.logger.info(f"User input received: {user_input}")

        classification = classifier(user_input)[0]
        emotion = classification['label']
        app.logger.info(f"Detected emotion: {emotion}")

        openai_client = openai.OpenAI(api_key=openai.api_key)
        system_message = """You are a movie recommendation assistant. Based on the user's detected emotion, suggest 3 appropriate movies. For each emotion:
        - Joy/Love: Suggest uplifting or romantic movies
        - Sadness: Recommend heartwarming or inspirational films
        - Anger: Propose calming or comedy movies
        - Surprise: Suggest thrilling or mind-bending films
        - Fear: Recommend light-hearted or family-friendly movies
        Provide only the titles of the 3 recommended movies, separated by commas."""

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": f"The user's detected emotion is: {emotion}"}
            ]
        )

        movie_titles = response.choices[0].message.content.split(', ')
        movies = []
        for title in movie_titles:
            movie_details = get_movie_details(title)
            if movie_details:
                movies.append(movie_details)
            app.logger.info(f"Movie details for {title}: {movie_details}")

        result = {
            'emotion': emotion,
            'movies': movies
        }

        if user_email:
            email_sent = send_recommendation_email(user_email, emotion, movies)
            result['email_sent'] = email_sent

        app.logger.info(f"Returning result: {result}")
        return jsonify(result)

    except Exception as e:
        app.logger.error(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
