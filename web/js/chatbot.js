function open_chat() {
    document.getElementById('chat-window').style.visibility='visible';
    document.getElementById('chat-btn').style.visibility='hidden';
}

function close_chat() {
    document.getElementById('chat-window').style.visibility='hidden';
    document.getElementById('chat-btn').style.visibility='visible';
}

function input_data() {
    baseUrl = "http://localhost:8080";
    input_txt = document.getElementById('msg-input').value;
    if(input_txt=="")
        return;
    document.getElementById('msg-input').value='';
    var body_inner = document.getElementById('body-inner');
    body_inner.innerHTML+='<span class="msg-right">'+input_txt+'</span>';
    fetch(baseUrl+"/getReply/"+input_txt).then(response=>response.json()).then(json=>{
        json.forEach(element => {
            if(element!="")
                body_inner.innerHTML+='<span class="msg-left">'+element+'</span>';
        });
        body_inner.scrollTop=body_inner.scrollHeight;
    });
}

document.getElementById('msg-input').addEventListener("keyup", function(event) {
    console.log("I was here!!!");
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("msg_btn").click();
    }
});