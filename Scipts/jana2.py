import requests
 
url = "https://elasticsearch-astap.oraclecorp.com/listing"
 
payload = {}
headers ={
        'Username': 'elastic',
        'Password': 'elastic@3'}
 
response = requests.request("POST", url, headers=headers, data = payload,verify=False)
 
print(response.text.encode('utf8'))