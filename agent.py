import os

import requests
from dotenv import load_dotenv

load_dotenv()


def chat_with_agent(user_id, agent_id, session_id, message):
    url = os.getenv("STUDIO_URL")
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": os.getenv("X-API-KEY"),
    }
    data = {
        "user_id": user_id,
        "agent_id": agent_id,
        "session_id": session_id,
        "message": message,
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=900)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None
    except Exception as err:
        print(f"Other error occurred: {err}")
        return None


def perform_research(session_id, message):
    user_id = "default_user"
    agent_id = os.getenv("RESEARCH_AGENT_ID")
    response = chat_with_agent(user_id, agent_id, session_id, message)
    return response


def generate_content(session_id, message):
    user_id = "default_user"
    agent_id = os.getenv("CONTENT_AGENT_ID")
    response = chat_with_agent(user_id, agent_id, session_id, message)
    return response
