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


with open('test_file.html', 'w') as html_file:
    html_file.write(html_text)
