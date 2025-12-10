import requests
headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0cmFuc2FjdGlvbl9pZCI6IjhjMWM5YmRiLWY0YzItNDU2ZC05MTI5LTc0OWVhNzY4M2JjYyIsInN1YiI6IjBhYmIzZDJhLWQxMmEtMTFmMC1hNzY5LWFmYzg0Y2ExZGFjMiIsImF1ZCI6WyJyZXN0c2VydmljZSJdLCJ1c2VyX25hbWUiOiJua2llbjY4MjdAZ21haWwuY29tIiwic2NvcGUiOlsicmVhZCJdLCJpc3MiOiJodHRwczovL2xvY2FsaG9zdCIsIm5hbWUiOiJua2llbjY4MjdAZ21haWwuY29tIiwidXVpZF9hY2NvdW50IjoiMGFiYjNkMmEtZDEyYS0xMWYwLWE3NjktYWZjODRjYTFkYWMyIiwiYXV0aG9yaXRpZXMiOlsiVVNFUiIsIlRSQUNLXzIiXSwianRpIjoiYWQ0N2NhODItMjEzNy00NTk3LTkzZTEtMDAxOTgwY2NjODI2IiwiY2xpZW50X2lkIjoiYWRtaW5hcHAifQ.P2y-mbl6YWXAct9P--Ema_Ao5659RLRQAXchONlAx9Xl8VtrwHPZMvy-NmwL4evYffpJBMZ0lHAiUiY9h15MpBCdApWyzxckC6W4Up3UqGWKgiHzghigu-W8V5MICC5Mzk8M9NnlCuWtZbo6NU2ezB59FYrjbPY72DMJtknpPtjBjXRd7R3-Ruf-gn7TB2z3DLrUEWNuWg2li3xWAThA-vDhnqWEr7dvm0sT1xlvn1dwWxEJuCZnjF1GUv5f-DddcMj_HZwXtcpd_qHsQ-rfssvSPhXqHSNY-e5ZNPm7txoqTG8m4p4WZGvZ4kX2sDlcyWixpcyESEuS67AUfFD_8w',
    'Token-id': '4525a88b-e821-4f0c-e063-62199f0a3a11',
    'Token-key': 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJ118i5OgOqroz+Wn5mWwI13O8vFz6OFCAWk7Zymb2p5wq/XsMqqwFhEfWlo1jGxFG2lcbWNSUSaGenMP/TdmI8CAwEAAQ==',
    'Content-Type': 'application/json',
}
json_data = {
    'model': 'vnptai_hackathon_embedding',
    'input': 'Xin chào, mình là VNPT AI.',
    'encoding_format': 'float'
}
response = requests.post('https://api.idg.vnpt.vn/data-service/vnptai-hackathon-embedding', headers=headers, json=json_data)
print(response.json())