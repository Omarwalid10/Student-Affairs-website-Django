var dlt = "Student has been deleted successfully";
function deleted(){
    alert(`${dlt}`)
    document.getElementById('sid').value = '';

}
function update(){
    document.getElementById('sid').value = '';
}
document.addEventListener('DOMContentLoaded',function (){
    document.querySelector('#update').disabled = true;
    document.querySelector('#delete').disabled = true;
    document.getElementById('sid').onkeyup = () =>{
        if(document.getElementById('sid').value.length > 0){
            var x = parseInt(document.getElementById('sid').value);
            if(isNaN(x)){
                alert(`Only Numbers is allowed.`);
                 document.getElementById('sid').value = '';
            }
            else{
                document.querySelector('#delete').disabled = false;
                document.querySelector('#update').disabled = false;
            }
        }
        else{
           
            document.querySelector('#delete').disabled = true;
            document.querySelector('#update').disabled = true;
        }

    }
    document.querySelector('#delete').onclick = deleted;
    // document.getElementById('update').onclick = update;

});