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
}

let add_contact = function(){
    window.location = '/customers/test/';
}


