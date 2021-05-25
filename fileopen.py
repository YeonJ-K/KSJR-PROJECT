#사용자가 입력해야 하는 명령어 양식
#python fileopen.py 경로+파일명
#tip. flask 값 넘기는 방법
#서버 필요?
import sys

html_text1 = """
    <!DOCYTPE html>
    <html>
    <head>
    <title>TEST Page</title>
    </head>
    <body>
    <p>
    """

html_text2 = """
    </p>
    </body>
    </html>
    """

#파일 열기
f = open(sys.argv[1])

#파일 전체 읽기
r = f.read()
print(r)

#html 파일에 추가하기
with open('html_file.html', 'a') as html_file:
    html_file.write(html_text1 + r + html_text2)

f.close()





