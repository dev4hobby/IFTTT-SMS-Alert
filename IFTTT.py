import requests
import json

def requestAlert(userApi, userParam):
  # Key값은 'Webhooks -> Documentation' 에서 확인
  # requests.post("https://maker.ifttt.com/trigger/{EVENT NAME}/with/key/{Your Key}")
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  requests.post(url=userApi, data=json.dumps(userParam), headers=headers)
