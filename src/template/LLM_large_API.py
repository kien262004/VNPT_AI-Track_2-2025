import requests
headers = {
    'Authorization': 'Bearer #Authorization',
    'Token-id': '#TokenID',
    'Token-key': '#TokenKey',
    'Content-Type': 'application/json',
}
json_data = {
    'model': 'vnptai_hackathon_large',
    'messages': [
        {
            'role': 'user',
            'content': 'Hi, VNPT AI.',
        },
    ],
    'temperature': 1.0,
    'top_p': 1.0,
    'top_k': 20,
    'n': 1,
    'max_completion_tokens': 10,
}
response = requests.post('https://api.idg.vnpt.vn/data-service/vnptai-hackathon-large', headers=headers, json=json_data)
response.json()