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
    <!DOCTYPE html>
    <head>
        <link rel="stylesheet" href="temp.css">
        <script src="temp.js"></script>
    </head>
    <body>
        <div>
            <div id="left_section" class="left_box">
    """

html_text2 = """
            </div>
            <div class="right_box">
                <div id="section1" class="label">
                 res[match_idx][0]['rule_no'],res[match_idx][0]['title'],res[match_idx][0]['descriptions'])
                </div>
                <div class="elements">
                상세한 내용1
                </div>
            </div>
        </div>
    </body>
    </html>    
"""

    




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
                    
            
                    line_res.append({'rule_no':rule["no"],'title':rule["title"], 'descriptions':rule["descriptions"], 'matched':matched, 'pos': (current_pos+matched_pos, current_pos+matched_pos+len(matched))})

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

    title_line=[]
#    print(rules)
    with open('html_file.html', 'a') as html_file:
        html_file.write(html_text1)

        for match_idx in res:
            deobfuscation = (res[match_idx][0]['matched'])
            change_p = "<p id=pid" + match_idx + ">" + str(deobfuscation) + "</p>"
            for source_idx in source_lines:
                if deobfuscation in source_idx:
                    source_idx = source_idx.replace(deobfuscation, change_p)
                    html_file.write(source_idx)
            for rule_idx in rules :
                title_line=res[match_idx][0]
                if res[match_idx][0]['rule_no'] == rules[rule_idx]['no'] :
                    title_line = res[match_idx][0]['rule_no'],res[match_idx][0]['title'],res[match_idx][0]['descriptions']
                    ob_path = rules[rule_idx]['deobfuscation']
                    mod_name = os.path.basename(ob_path)
            spec = importlib.util.spec_from_file_location(mod_name, ob_path)
            foo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(foo)
            cls = foo.deobfus_code(deobfuscation)

        html_file.write(html_text2)
        print(res[match_idx][0]['title'])


        

"""
    with open('html_file.html', 'a') as html_file:
        html_file.write(html_text1)
        for source_idx in source_lines:
            html_file.write(source_idx)
        html_file.write(html_text2)
"""
    
if __name__ == '__main__':
    main()
