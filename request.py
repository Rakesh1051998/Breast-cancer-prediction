import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ClumpThickness':2,'Unisize':3,'Unishape':6,'MargAd':8,'SingEpiCelsize':4,'Barenuc':1,'Blandchr':5,'NormalNuc':5,'Mito':8})

print(r.json())