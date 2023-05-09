import datetime
import pyttsx3
import speech_recognition as sr
import openai
import nltk
import webbrowser
import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')[0].get_text()
    return search_results


def jarvis():
    # Set up text-to-speech engine
    engine = pyttsx3.init()

    # Set up speech recognition
    recognizer = sr.Recognizer()

    # Set up OpenAI API
    openai.api_key = "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"

    # Greet the user based on the time of day
    now = datetime.datetime.now()
    if now.hour < 12:
        speak("Good morning, sir.")
    elif now.hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")

    # Enter standby mode
    standby = True

    # Continuously listen for voice commands
    while standby:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Convert speech to text
            command = recognizer.recognize_google(audio).lower()

            # Wake up JARVIS
            if "jarvis" in command:
                speak("Yes, sir? How may I assist you?")
                standby = False

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            speak("Sorry, I didn't catch that. Could you please repeat?")

    # Process voice commands
    while not standby:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Convert speech to text
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")

            # Turn off JARVIS
            if "thank you jarvis" in command:
                speak("You're welcome, sir. Goodbye.")
                standby = True

            # Get the current time
            elif "what time is it" in command:
                now = datetime.datetime.now()
                speak(f"The time is {now.strftime('%I:%M %p')}")

            # Get the current date
            elif "what's today's date" in command or "what's the date today" in command:
                now = datetime.datetime.now()
                speak(f"Today is {now.strftime('%B %d, %Y')}")

                # Search the web
            elif "search" in command:
                query = command.replace("search", "")
                speak(f"Searching for {query} on Google.")
                search_url = "https://www.google.com/search?q=" + query
                webbrowser.open(search_url)


            # Answer a question
            elif "what is" in command or "who is" in command or "where is" in command or "when is" in command:
                speak("Let me look that up for you.")
                question = command
                search_results = google_search(question)
                webbrowser.open(f"https://www.google.com/search?q={question}")
                speak(search_results)            
                 
            elif "who made you" in command or "who is your owner" in command or "who is your developer" in command or "who is your dev" in command:
                speak("sir PragneshKumar Shrikesh Singh also known as Maximus")

            # Analyze sentiment of a topic
            elif "what do people think about" in command:
                topic = command.replace
                speak("Let me check the sentiment of the topic.")
                topic = topic.replace("what do people think about", "")
                sia = SentimentIntensityAnalyzer()
                results = openai.Completion.create(
                    engine="davinci",
                    prompt=f"Get opinions about {topic}.",
                    max_tokens=100,
                )
                opinions = results.choices[0].text
                sentiment_score = sia.polarity_scores(opinions)
                if sentiment_score['compound'] >= 0.05:
                    speak(f"Overall, people seem to have a positive sentiment about {topic}.")
                elif sentiment_score['compound'] <= -0.05:
                    speak(f"Overall, people seem to have a negative sentiment about {topic}.")
                else:
                    speak(f"Overall, people seem to have a neutral sentiment about {topic}.")

            # Catch-all response for unrecognized commands
            else:
                speak("I'm sorry, sir. I don't understand what you mean.")

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
            speak("Sorry, I didn't catch that. Could you please repeat?")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    jarvis()
