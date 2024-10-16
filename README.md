# Mood-Based Cinematic Curator 🎬
An AI-powered web application that recommends movies based on your emotional state, built with Flask, OpenAI, and Twilio SendGrid.

## Features ✨

- Emotion analysis through natural language processing
- AI-powered movie recommendations using OpenAI's GPT-3.5 Turbo
- Rich movie details from The Movie Database (TMDb)
- Email notifications with personalized recommendations via Twilio SendGrid
- Modern, responsive UI with Tailwind CSS

## Running the Application 🚀

1. Make sure your virtual environment is activated:
```bash
# On Windows:
moodBooster\Scripts\activate
# On Unix or MacOS:
source moodBooster/bin/activate
```

2. Start the Flask application:
```bash
python app.py
```

3. The application will start and display something like:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: xxx-xxx-xxx
```

4. Access the application:
   - Open your web browser
   - Navigate to `http://127.0.0.1:5000` or `http://localhost:5000`
   - You should see the main page with a text area to describe your mood

5. Using the application:
   - Enter how you're feeling in the text area
   - Optionally provide your email for recommendations
   - Click "Get Recommendations"
   - Wait a few moments for the AI to analyze your mood and suggest movies
   - If you provided an email, check your inbox for the recommendations

6. To stop the application:
   - Return to the terminal
   - Press `CTRL+C` to stop the Flask server
   - Deactivate the virtual environment when you're done:
     ```bash
     deactivate
     ```


```
```

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Author ✍️

Jacob Muganda - Full-stack developer and Machine Learning enthusiast

## Acknowledgments 🙏

- OpenAI for providing the GPT API
- TMDb for movie data
- Twilio SendGrid for email services
- The Flask and Python communities
