let toogle_dropdown = (id) =>{
    if (document.getElementById(id).style.display == "none"){
        document.getElementById(id).style.display = "block";
    }
    else{
        document.getElementById(id).style.display = "none";
    }
}




let add_new_expense = function (){
    window.location = '/expenses/new_expense';
 }


let close_item = function (id){
    document.getElementById(id).style.display = 'none';
}
 
 