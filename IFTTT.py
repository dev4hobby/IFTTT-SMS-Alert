import requests
import json

def requestAlert(userApi, userParam):
  # Key값은 'Webhooks -> Settings' 에서 확인
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  requests.post(url=userApi, data=json.dumps(userParam), headers=headers)
