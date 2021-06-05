#사용자가 입력해야 하는 명령어 양식
#python fileopen.py 경로+파일명
#tip. flask 값 넘기는 방법
#서버 필요?
import sys
import re
import json
import glob
import argparse
from rules import *


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



'''

#Rule 읽어오는 파일
rule_files = glob.glob(r'rules/*.json')
rules = [] # 
key_list = []
title = []
descriptions = []
deobfuscation = []
code_convert = []


#문자열을 전부 읽어와서 for문 돌리기 (전부 읽어오기와 한줄씩 읽어오기가 동시에 불가)
for i in r.split("\n"):
    #index는 나중에 p태그의 id값으로 사용될 예정, 지금은 예시로 출력만
    #i는 받아온 파싱 내용 중에서 한줄씩 들어감
    print('%d %s' %(index, i))
    for a in rule_files:
        json_data = json.loads(open(a).read()) 
        key = json_data['regexp']
        detect = re.compile(key)
        show = re.search(detect, i)
        print(show)
        if show:
            print("탐지 : " + show.group())
    index += 1

#html 파일에 추가하기
with open('html_file.html', 'a') as html_file:
    html_file.write(html_text1 + r + html_text2)

f.close()

'''



def  load_rules(rule_path:str) -> list:

    rules = []

    rule_pattern = f'{rule_path}/*.json'
    rule_files = glob.glob(rule_pattern)

    for rule_file in rule_files:
        try:
            json_data = json.loads(open(rule_file).read()) 
            rules.append(json_data)
        except Exception as e:
            pass
    return rules

def load_malware(path:str) -> list:
    try:
        lines = open(path).readlines()
        return lines
    except:
        return []

def match_rule(lines:list, rules:list) -> dict:


    for line_idx in range(len(lines)):
        line_res = {}

        for rule in rules:
            print(f'{line_idx} match {rule["title"]}')

            pattern = rule['regexp']
            print(pattern)
            try:
                regexp = re.compile(pattern)
            except Exception as e:
                print(f'error {rule["title"]}')
            #matched_res = re.search(regexp, lines[line_idx])

            #print(matched_res)




def main():
    parser = argparse.ArgumentParser(description='Parse Script')
    parser.add_argument('input', type=str, 
                    help='input file')
    
    parser.add_argument('--rules', type=str, 
                    help='rule path')

    args = parser.parse_args()

    rule_path = './rules'
    if args.rules != None and  args.rules != '':
        rule_path = args.rules

    print('[+] Load Rules')
    rules = load_rules(rule_path)
    print(f'    [-] {len(rules)} rules loaded')

    source_lines = load_malware(args.input)

    match_rule(source_lines, rules)




if __name__ == '__main__':
    main()