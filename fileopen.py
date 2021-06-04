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
#print(r)
index=1

#Rule 읽어오는 파일
path = glob.glob(r'rules/*.json')
rules = []
key_list = []
for a in path:
    json_data = json.loads(open(a).read()) 
    rules.append(json_data)
    key_list.append(json_data['regexp'])
# print(json.dumps(key_list, indent='\t'))
# print(json.dumps(rules, indent='\t'))  # 제대로 읽어오는지 test용


#문자열을 전부 읽어와서 for문 돌리기 (전부 읽어오기와 한줄씩 읽어오기가 동시에 불가)
for i in r.split("\n"):
    #index는 나중에 p태그의 id값으로 사용될 예정, 지금은 예시로 출력만
    #i는 받아온 파싱 내용 중에서 한줄씩 들어감
    print('%d %s' %(index, i))
    index += 1


#html 파일에 추가하기
with open('html_file.html', 'a') as html_file:
    html_file.write(html_text1 + r + html_text2)

f.close()
