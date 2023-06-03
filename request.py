import requests

url = 'https://lkhhg706o4.execute-api.ap-northeast-3.amazonaws.com/dev'

response = requests.get(url)
print(response.text)

submit_data = {
    'user_id': 'TaroYamada',
    'password': 'PaSSwd4TY'
}

new_url = url + '/kake'
response = requests.post(
    new_url,
    json=submit_data
)
print(response.text)
