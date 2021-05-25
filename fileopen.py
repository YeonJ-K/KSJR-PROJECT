#사용자가 입력해야 하는 명령어 양식
#python fileopen.py 경로+파일명
import sys

#파일 열기
f = open(sys.argv[1])

#파일 전체 읽기
r = f.read()
print(r)

f.close()


