import requests


def check(token):
    req = requests.get(f"https://api.telegram.org/bot{token}/getUpdates")
    return req.json()['ok']
