from IFTTT import requestAlert
import datetime

def sendMsg(message):
  requestAlert(userApi="https://maker.ifttt.com/trigger/{EventName}/with/key/{YourKey}",
                userParam={
                  'value1': str(datetime.datetime.now()),
                  'value2': message,
                })

sendMsg(message='안녕하세요. 테스트 메시지입니다.')

print('done')