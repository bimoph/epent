var event_btn1 = document.getElementById("event-btn1");
var event_btn2 = document.getElementById("event-btn2");
var event_btn3 = document.getElementById("event-btn3");
var event_btn4 = document.getElementById("event-btn4");
var event_btn5 = document.getElementById("event-btn5");

var slider = document.querySelector('.event-content-frame-slider');

event_btn1.onclick = function(){
    this.style.background = "#5DB075";
    event_btn2.style.background = "white";
    event_btn3.style.background = "white";
    event_btn4.style.background = "white";
    event_btn5.style.background = "white";
    slider.style.marginLeft ="0px"

}
event_btn2.onclick = function(){
    this.style.background = "#5DB075";
    event_btn1.style.background = "white";
    event_btn3.style.background = "white";
    event_btn4.style.background = "white";
    event_btn5.style.background = "white";
    slider.style.marginLeft ="-900px"
}
event_btn3.onclick = function(){
    this.style.background = "#5DB075";
    event_btn1.style.background = "white";
    event_btn2.style.background = "white";
    event_btn4.style.background = "white";
    event_btn5.style.background = "white";
    slider.style.marginLeft ="-1800px"
}
event_btn4.onclick = function(){
    this.style.background = "#5DB075";
    event_btn1.style.background = "white";
    event_btn2.style.background = "white";
    event_btn3.style.background = "white";
    event_btn5.style.background = "white";
    slider.style.marginLeft ="-2700px"
}
event_btn5.onclick = function(){
    this.style.background = "#5DB075";
    event_btn1.style.background = "white";
    event_btn2.style.background = "white";
    event_btn3.style.background = "white";
    event_btn4.style.background = "white";
    slider.style.marginLeft ="-3600px"
}

