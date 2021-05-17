//난독화 종류 중 8번 해제 - 코드 수정 필요

var str = "'iglzxcsec'.replace('zxc','o')";

//함수만들기 - 특수문자 제거
function del(stringre){
    var reg = /[\']/gi;

    if(reg.test(stringre)){
        //특수문자 제거후 리턴
        return stringre.replace(reg,"");  
    } else {
        //특수문자가 없으므로 본래 문자 리턴
        return stringre;
    }
}

//replace뒤 문자 가져오기
if(str.indexOf('.replace')>0){
    var result1 = str.substring(0,str.indexOf('.replace'));
    var result2 = str.substring(str.indexOf('.replace')+9, str.length-1);
    console.log(result1);
    console.log(result2);
    var re = result2.split(",");
    console.log(result1.replace(del(re[0]),del(re[1])));

    
}else{
    console.log(str);
}