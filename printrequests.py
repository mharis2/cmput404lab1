import requests

print(requests.__version__)
print(requests.get('http://www.google.com'))
req = requests.get('https://raw.githubusercontent.com/mharis2/cmput404lab1/master/printrequests.py','html.parser')
print(req)
with open("source_code",'w') as f:
    f.write(req.text)
    f.close()
