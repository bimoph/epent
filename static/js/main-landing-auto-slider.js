
var next = 1;
var nexts = 1;
setInterval(function(){
   
    document.getElementById('radios' + nexts).checked = true;
    document.getElementById('radio' + next).checked = true;
    next++;
    if(next > 4){
        next = 1;
    }
},5000);

