document.addEventListener('DOMContentLoaded',function (){
    document.getElementById('name').onkeyup = () =>{
        if(document.getElementById('name').value.length > 0){
            var x = parseInt(document.getElementById('name').value);
            if(!isNaN(x)){
                alert("please enter a valid name");
                 document.getElementById('name').value = '';
                }
           }
        }
    });
    document.addEventListener('DOMContentLoaded',function (){
    document.getElementById('idName').onkeyup = () =>{
        if(document.getElementById('idName').value.length > 0){
            var x = parseInt(document.getElementById('idName').value);
            if(isNaN(x)){
                alert("please enter numbers");
                 document.getElementById('idName').value = '';
                }
          }
        }
    });
    document.addEventListener('DOMContentLoaded',function (){
        document.getElementById('gba').onkeyup = () =>{
            if(document.getElementById('gba').value.length > 0){
                var x = parseInt(document.getElementById('gba').value);
                if(isNaN(x)){
                    alert("please enter numbers");
                    document.getElementById('gba').value = '';
                }
            }
        }
    });
    var level = parseInt(document.querySelector('#lvl').value);
    if(level == 1 || level == 2){
        document.querySelector('#dep').disabled = true; 
    }

    document.addEventListener('DOMContentLoaded',function (){
    document.getElementById('phone').onkeyup = () =>{
        if(document.getElementById('phone').value.length > 0){
            var x = parseInt(document.getElementById('phone').value);
            if(isNaN(x)){
                alert("please enter numbers");
                 document.getElementById('phone').value = '';
                }
          }
        }
});