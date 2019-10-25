#!python3
import json
import requests

def CheckCEP(CEP):
    url = "https://viacep.com.br/ws/"+CEP+"/json/"
    requestCEP = requests.get(url)
    if requestCEP.status_code == 200:
        try:
            jsonRequest = json.loads(requestCEP.text)
            print(jsonRequest["localidade"])
        except:
            jsonRequest["erro"] == True  
            print('Não encontrou esse CEP em lugar nenhum do Brasil')
    else:
        print('Não foi possível pesquisar com o CEP informado')
    
CheckCEP('09581310')
CheckCEP('00000000')
CheckCEP('0000000')
