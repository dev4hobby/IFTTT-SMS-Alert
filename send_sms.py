from IFTTT import requestAlert
import datetime

def sendMsg(message):
  requestAlert(userApi="YOUR API URL",
                userParam={
                  'value1': str(datetime.datetime.now()),
                  'value2': message,
                })

replyCount = -1
sendMsg(message='보내실 메시지를 입력하세요')

print('done')