"use strict";

window.onload = () => {
    var elements = document.getElementsByTagName("div");

    // 모든 영역 접기
    for (var i = 0; i < elements.length; i++) {
      if (elements[i].className == "elements") {
        elements[i].style.display="none";
      } else if (elements[i].className == "label") {
        elements[i].onclick=switchDisplay;
      }
    }

    // 상태에 따라 접거나 펼치기
    function switchDisplay() {

      var parent = this.parentNode;
      var target = parent.getElementsByTagName("div")[1];

      if (target.style.display == "none") {
        target.style.display="block";
      } else {
        target.style.display="none";
      }
      return false;
    }    

};

