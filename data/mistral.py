
import requests
from data.config import load_config, Config

API_URL = "https://api.mistral.ai/v1/chat/completions"
config: Config = load_config()
mistral_api_key = config.tg_bot.mistral_api_key

def get_mistral_response(user_message: str, language: str = "ru") -> str:
    headers = {
        "Authorization": f"Bearer {mistral_api_key}",
        "Content-Type": "application/json"
    }

    # Явное указание языка
    system_prompt = f"Ты — полезный ассистент. Отвечай на {language.upper()} языке. Будь дружелюбным, но профессиональным."

    data = {
        "model": "mistral-medium",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    print(f"Статус код: {response.status_code}")
    print(f"Ответ API: {response.text}")

    if response.status_code != 200:
        return f"Ошибка API: {response.json().get('message', 'Неизвестная ошибка')}"

    response_data = response.json()
    return response_data.get("choices", [{}])[0].get("message", {}).get("content", "Ошибка ответа от модели.")


















# import requests
# from data.config import load_config, Config
#
# API_URL = "https://api.mistral.ai/v1/chat/completions"  # Убедись, что URL правильный
# config: Config = load_config()
# mistral_api_key = config.tg_bot.mistral_api_key
#
# def get_mistral_response(user_message):
#     headers = {
#         "Authorization": f"Bearer {mistral_api_key}",
#         "Content-Type": "application/json"
#     }
#
#
#     data = {
#         "model": "mistral-medium",  # Попробуй этот вариант, если mistral-7b не работает
#         "messages": [{"role": "user", "content": user_message}]
#     }
#
#     response = requests.post(API_URL, headers=headers, json=data)
#
#     # Логируем весь ответ от сервера
#     print(f"Статус код: {response.status_code}")
#     print(f"Ответ API: {response.text}")
#
#     if response.status_code != 200:
#         return f"Ошибка API: {response.json().get('message', 'Неизвестная ошибка')}"
#
#     response_data = response.json()
#     return response_data.get("choices", [{}])[0].get("message", {}).get("content", "Ошибка ответа от модели.")
