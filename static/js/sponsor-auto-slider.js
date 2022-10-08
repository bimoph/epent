
var counters = 1;
setInterval(function(){
    document.getElementById('radios' + counters).checked = true;
    counters++;
    if(counters > 4){
        counters = 1;
    }
},5000);
    