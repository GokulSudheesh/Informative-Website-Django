function other(){
    let notOthers = document.getElementsByClassName("findUs-choice");
    Array.prototype.forEach.call(notOthers, element => {
        element.checked = false;
    });
    document.getElementById("other").checked = true;
    document.getElementById("other_text").required = true;
}

function notOther(){
    document.getElementById("other_text").value = "";
    document.getElementById("other").checked = false;
    document.getElementById("other_text").required = false;
}