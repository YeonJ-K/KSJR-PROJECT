"use strict";

function display(a) {
    var str = "ele"+a;
    var name = document.getElementById(str);
    if (name.style.display=="none"){
        name.style.display="block";
    } else {
        name.style.display="none";
    }
}

/*
window.onload = () => {
    var box = document.getElementsByTagName("div");
    var ele = document.getElementById("ele");
    var pre = document.getElementById("pre");
    if (box.onclick == "pre"){
        ele.style.display="block";
    } else {
        ele.style.display="none";
    }

};
/
function display(a) {
    str = "ele"+a;
    elements = document.getElementById(str);
    if (ele1.style.display=="none"){
        ele1.style.display="block";
    } else {
        ele1.style.display="none";
    }
}
*/

