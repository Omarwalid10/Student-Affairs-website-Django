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
    document.getElementById('gpa').onkeyup = () =>{
        if(document.getElementById('gpa').value.length > 0){
            var x = parseInt(document.getElementById('gpa').value);
            if(isNaN(x)){
                alert("please enter numbers");
                 document.getElementById('gpa').value = '';
                }
          }
        }
    });
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