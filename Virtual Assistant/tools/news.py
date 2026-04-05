import requests
from core.config import NEWS_API_KEY
from output.voice import speak

NEWS_URL = "https://newsapi.org/v2/top-headlines"


def get_news(country: str = "pk", count: int = 5) -> None:
    """Fetch and read top headlines aloud."""
    try:
        resp = requests.get(
            NEWS_URL,
            params={"country": country, "apiKey": NEWS_API_KEY},
            timeout=5,
        )
        resp.raise_for_status()
        articles = resp.json().get("articles", [])[:count]

        if not articles:
            speak("No headlines found right now.")
            return

        speak(f"Here are the top {len(articles)} headlines.")
        for i, article in enumerate(articles, 1):
            speak(f"{i}. {article['title']}")

    except requests.exceptions.ConnectionError:
        speak("No internet connection. Can't fetch news.")
    except requests.exceptions.Timeout:
        speak("News request timed out.")
    except Exception as e:
        print(f"[News error] {e}")
        speak("Couldn't fetch news right now.")