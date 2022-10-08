var sponsor_btn1 = document.getElementById("sponsor-btn1");
var sponsor_btn2 = document.getElementById("sponsor-btn2");
var sponsor_btn3 = document.getElementById("sponsor-btn3");
var sponsor_btn4 = document.getElementById("sponsor-btn4");
var sponsor_btn5 = document.getElementById("sponsor-btn5");

var sponsor_slider = document.querySelector('.sponsor-content-frame-slider');

sponsor_btn1.onclick = function(){
    this.style.background = "#5DB075";
    sponsor_btn2.style.background = "white";
    sponsor_btn3.style.background = "white";
    sponsor_btn4.style.background = "white";
    sponsor_btn5.style.background = "white";
    sponsor_slider.style.marginLeft ="0px";

}
sponsor_btn2.onclick = function(){
    this.style.background = "#5DB075";
    sponsor_btn1.style.background = "white";
    sponsor_btn3.style.background = "white";
    sponsor_btn4.style.background = "white";
    sponsor_btn5.style.background = "white";
    sponsor_slider.style.marginLeft ="-900px"
}
sponsor_btn3.onclick = function(){
    this.style.background = "#5DB075";
    sponsor_btn1.style.background = "white";
    sponsor_btn2.style.background = "white";
    sponsor_btn4.style.background = "white";
    sponsor_btn5.style.background = "white";
    sponsor_slider.style.marginLeft ="-1800px"
}
sponsor_btn4.onclick = function(){
    this.style.background = "#5DB075";
    sponsor_btn1.style.background = "white";
    sponsor_btn2.style.background = "white";
    sponsor_btn3.style.background = "white";
    sponsor_btn5.style.background = "white";
    sponsor_slider.style.marginLeft ="-2700px"
}
sponsor_btn5.onclick = function(){
    this.style.background = "#5DB075";
    sponsor_btn1.style.background = "white";
    sponsor_btn2.style.background = "white";
    sponsor_btn3.style.background = "white";
    sponsor_btn4.style.background = "white";
    sponsor_slider.style.marginLeft ="-3600px"
}

