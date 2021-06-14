'''def mal_var(change_p, label, result_deobfuscation) :
    
    funLabel = 
    """        <div>
                <div id="section1" class="label">
                    <p>"""+label+"""</p>
                </div>
                <div class="elements">
    """+result_deobfuscation+"""            </div>
            </div>
    """
'''
        
right_box = ""

html_head =
"""<!DOCTYPE html>
<head>
    <link rel="stylesheet" href="temp.css">
</head>
"""

html_body_1 =
"""<body>
<form>
    <div>
        <div id="left_section" class="left_box">
"""
    num = len(label)
    for i range (num):
        funLabel = 
        """        <div>
                    <div id="section1" class="label">
                        """+str(label[i])+"""
                    </div>
                    <div class="elements">
        """
        funElements = funLabel+str(result_deobfuscation[i])+"""            </div>
                </div>
        """
        right_box += funElements    


html_body_2 =
"""        </div>
    </div>
    
    <div class="right_box">
"""

html_body_3 =
"""    </div>
</form>
    <script src="temp.js"></script>
</body>
"""




#result와 label은 같은 값이 들어가야하고, elements가 자세한 값
#body1뒤에 누르면 열릴 결과값 텍스트
#body2뒤엔 div 하나로 넣으면 됨


html_text = html_head+html_body_1+pre+html_body_2+right_box+html_body_3


with open('test_file.html', 'w') as html_file:
    html_file.write(html_text)
