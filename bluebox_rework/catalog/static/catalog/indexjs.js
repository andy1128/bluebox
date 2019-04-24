function addMovie() {
    
    
    var i;
//    while (i < 6){
//        
//        var img = document.createElement("img");    
//        img.src = "Images/poster" + i + ".jpg";
//        img.height = 400;
//        document.getElementById('col_id').appendChild(img);
//        
//        i++;
//    }
    for(i = 1; i < 6; i++){
        var img = document.createElement("img");    
        img.src = "Images/poster" + i + ".jpg";
        img.height = 400;
        document.getElementById('col_id').appendChild(img);
    }
    
}

function gotoMainPage(){
    window.location.replace="index.html";
}
