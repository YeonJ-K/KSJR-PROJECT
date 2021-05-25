import base64
base64_str =  '' # 해당 변수에 파싱, 탐지한 Base64 코드 담는다.
'''
파싱한 부분을 담는 곳은
주석처리해서 말씀해주세요
'''
base64_bytes = base64.b64decode(base64_str)
base64_decode = base64_bytes.decode('ascii')
