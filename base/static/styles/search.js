
document.addEventListener('DOMContentLoaded',function (){
    document.querySelector('#search').disabled = true;
    document.getElementById('searchAssign').onkeyup = () =>{
        if(document.getElementById('searchAssign').value.length > 0){
            var x = parseInt(document.getElementById('searchAssign').value);
            if(!isNaN(x)){
                alert("please enter a valid name");
                 document.getElementById('searchAssign').value = '';
            }
            else{
                document.querySelector('#search').disabled = false;
             
            }
        }
        else{
           
            document.querySelector('#search').disabled = true;
           
        }

    }
});
