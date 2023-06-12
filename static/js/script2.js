document.body.style.zoom = "75%";

let values = []
let values2 = []
let values3 = []

function add(element,number){
    if (element.className=="select"){
        if(number==1){
            if (values.length < 4){
                values.push(element.value)
                element.className = "dark-select";
            }else{
                text = document.getElementById("hide");
                text.className = "error"
            }
        }else if(number==2){
            if (values2.length < 4){
                values2.push(element.value)
                element.className = "dark-select";
            }else{
                text = document.getElementById("hide2");
                text.className = "error"
            }
        }else{
            if (values3.length < 9){
                values3.push(element.value)
                element.className = "dark-select";
            }
            else{
                text = document.getElementById("hide3");
                text.className = "error"
            }
            
        }
        
    }else{
        element.className = "select";
        if(number==1){
            text = document.getElementById("hide");
            text.className = "hide"
            let index = values.indexOf(element.value);
            values.splice(index, 1);
        }else if(number==2){
            text = document.getElementById("hide2");
            text.className = "hide"
            let index = values2.indexOf(element.value);
            values2.splice(index, 1);
        }else{
            text = document.getElementById("hide3");
            text.className = "hide"
            let index = values3.indexOf(element.value);
            values3.splice(index, 1);
        }
    }
    console.log(values)
}

function send(){
    txt = document.getElementsByClassName("txt")[0]
    var url = "result?txt=" + txt.value + "&values=" + values + "&values2=" + values2 + "&values3=" + values3;
    window.location.href = url;
}