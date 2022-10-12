let toogle_dropdown = (id) =>{
    if (document.getElementById(id).style.display == "none"){
        document.getElementById(id).style.display = "block";
    }
    else{
        document.getElementById(id).style.display = "none";
    }
}


function toogle_content(){
    document.getElementById('item').style = null;
    document.getElementById('optionals').style = null;
    document.getElementById('create-vendor').style = null;
}

let add_contact = function(id){
    document.getElementById(id).style.display = 'block';
    document.getElementById('optionals').style.display = 'none';
    document.getElementById('create-vendor').style = "display : grid; margin: 10px auto;";
}