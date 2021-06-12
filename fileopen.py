#사용자가 입력해야 하는 명령어 양식
#python fileopen.py 경로+파일명
#tip. flask 값 넘기는 방법
#서버 필요?
import sys
import re
import os
import json
import glob
import argparse
import inspect
import importlib.util

html_text1 = """
    <!DOCYTPE html>
    <html>
    <head>
        <title>TEST Page</title>
        <link href="pTag.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
    """

html_text2 = """
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

'''



def  load_rules(rule_path:str) -> dict:

    rules = {}

    rule_pattern = f'{rule_path}/*.json'
    rule_files = glob.glob(rule_pattern)

    for rule_file in rule_files:
        try:
            json_data = json.loads(open(rule_file).read()) 
            rules[str(json_data['no'])]= json_data
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

    result = {}

    for line_idx in range(len(lines)):
        line_res = []

        for rule in rules.values():
            print(f'{line_idx+1} match {rule["title"]}')

            pattern = rule['regexp']
            regexp = re.compile(pattern)
            matched_list = re.findall(regexp, lines[line_idx])
            
            line_temp = lines[line_idx]

            current_pos = 0
            for matched in matched_list:
                
                while True:
                    matched_pos = line_temp.find(matched)

                    if matched_pos == -1:
                        break
                    line_temp = line_temp[matched_pos+len(matched):]
                    
            
                    line_res.append({'rule_no':rule["no"], 'matched':matched, 'pos': (current_pos+matched_pos, current_pos+matched_pos+len(matched))})

                    current_pos += matched_pos+len(matched)

    #    for res in line_res:
    #        print(f'{res["rule_no"]} in {res["pos"]}')
        result[str(line_idx+1)] = line_res
    return result
       
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

    res = match_rule(source_lines, rules)

    print(res['1'][0])
    print(rules)
    pCreate = []
    for match_idx in res:
        print(match_idx)
        deobfuscation = (res[match_idx][0]['matched'])
        for rule_idx in rules :
            if res[match_idx][0]['rule_no'] == rules[rule_idx]['no'] :
                pCreate.append("<p id=pid" + str(match_idx) + ">" + str(res[match_idx][0]['matched']) + "</p>")
                print("P->", pCreate)
                ob_path = rules[rule_idx]['deobfuscation']
                mod_name = os.path.basename(ob_path)
        spec = importlib.util.spec_from_file_location(mod_name, ob_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        cls = foo.deobfus_code(deobfuscation)

        


    with open('html_file.html', 'a') as html_file:
        for p_idx in pCreate :
            html_file.write(html_text1 + p_idx + html_text2)
     
    
if __name__ == '__main__':
    main()
