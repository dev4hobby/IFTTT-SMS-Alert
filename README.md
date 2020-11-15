# IFTTT
SMS로 알림을 보낸다거나 .. 혼자 쓰기 편할것 같아서 기록해둠.  
이후 다른 모듈들이 필요하면 추가될듯

## 요구사항
pip 패키지 설치
```bash
pip install -r requirements.txt
```

## 실행방법
- IFTTT API 주소 정보 변경
- 실행
```bash
python3 send_sms.py
```

### IFTTT.py
```python
from IFTTT import requestAlert
requestAlert(userApi, userParam)
```