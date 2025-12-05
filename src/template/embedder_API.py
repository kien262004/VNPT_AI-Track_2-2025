import requests
headers = {
    'Authorization': 'Bearer #Authorization',
    'Token-id': '#TokenID',
    'Token-key': '#TokenKey',
    'Content-Type': 'application/json',
}
json_data = {
    'model': 'vnptai_hackathon_embedding',
    'input': 'Xin chào, mình là VNPT AI.',
    'encoding_format': 'float',
}
response = requests.post('https://api.idg.vnpt.vn/data-service/vnptai-hackathon-embedding', headers=headers, json=json_data)
response.json()