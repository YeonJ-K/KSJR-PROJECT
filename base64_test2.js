//난독화 종류 중 2,4,6 해제

var str = "D'w''d'''+.ddds";
//var reg = /[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]/gi
var reg = /[+\']/gi;

if(reg.test(str)){
    //특수문자 제거후 리턴
    console.log(str.replace(reg,""));  
} else {
    //특수문자가 없으므로 본래 문자 리턴
    console.log(str);
}
