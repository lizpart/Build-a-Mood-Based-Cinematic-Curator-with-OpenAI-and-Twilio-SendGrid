# Mood-Based Cinematic Curator 🎬
In an era of information overload and decision fatigue, tools that simplify our choices while catering to our emotional needs are invaluable. The right movie can turn your day around. Feeling down, anxious, or stuck? Movies tap into emotions and offer escape or a refresh.  The Mood-Based Cinematic Curator syncs your mood with the perfect film.
 
An AI-powered web application that recommends movies based on your emotional state, built with Flask, OpenAI, and Twilio SendGrid.

## Features ✨

- Emotion analysis through natural language processing
- AI-powered movie recommendations using OpenAI's GPT-3.5 Turbo
- Rich movie details from The Movie Database (TMDb)
- Email notifications with personalized recommendations via Twilio SendGrid
- Modern, responsive UI with Tailwind CSS

## Prerequisites 📋

Before you begin, ensure you have the following:

- Python 3.7 or later
- A Twilio SendGrid account
- An OpenAI API key
- A TMDb API key
- Basic understanding of Python

## Installation 🚀

1. Clone the repository:
```bash
git clone [your-repository-url]
cd mood-based-cinematic-curator
```

2. Create and activate a virtual environment:
```bash
python -m venv moodBooster
# On Windows:
moodBooster\Scripts\activate
# On Unix or MacOS:
source moodBooster/bin/activate
```

3. Install required packages:
```bash
pip install flask openai python-dotenv requests transformers sendgrid
```

4. Create a `.env` file in the project root and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
TMDB_API_KEY=your_tmdb_api_key
SENDGRID_API_KEY=your_sendgrid_api_key
SENDGRID_FROM_EMAIL=your_sendgrid_email
```

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

## Troubleshooting 🔧

If you encounter any issues:

1. Check that all API keys in your `.env` file are correct
2. Ensure all required packages are installed
3. Verify your Python version is 3.7 or later
4. Check that the virtual environment is activated
5. Make sure ports 5000 is not in use by another application
6. Look for error messages in the terminal running the Flask application

## Project Structure 📁

```
mood-based-cinematic-curator/
├── app.py                # Main Flask application
├── templates/
│   └── mood_check.html   # Frontend template
├── .env                  # Environment variables
└── README.md            # Project documentation
```

## API Configuration 🔑

### OpenAI Setup
1. Visit [OpenAI](https://platform.openai.com/signup)
2. Create an account and generate an API key
3. Add the key to your `.env` file

### TMDb Setup
1. Create an account on [TMDb](https://www.themoviedb.org/signup)
2. Request an API key
3. Add the key to your `.env` file

### SendGrid Setup
1. Sign up for a [Twilio SendGrid account](https://signup.sendgrid.com)
2. Create an API key with full access
3. Add the key and sender email to your `.env` file

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Author ✍️

Jacob Muganda - Full-stack developer and Machine Learning enthusiast

## Acknowledgments 🙏

- OpenAI for providing the GPT API
- TMDb for movie data
- Twilio SendGrid for email services
- The Flask and Python communities
