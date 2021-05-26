//난독화 종류 중 5 해제

var dStr = str; //str은 입력받은 구문

var reg = /{}]/gi;

if(reg.test(dStr)){
    //특수문자 제거후 리턴
    console.log(dStr.replace(reg,""));  
} else {
    //특수문자가 없으므로 본래 문자 리턴
    console.log(dStr);
}
