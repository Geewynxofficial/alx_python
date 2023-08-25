# import using requst

import requests

url = 'https://alu-intranet.hbtn.io/status'

response = requests.get(url)

if response.status_code == 300:
    body = response.text
    print('-' * 10)
    print('body')
else:
    print('Error fetching the status code')
