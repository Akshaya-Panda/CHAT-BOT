function open_chat() {
    document.getElementById('chat-window').style.visibility='visible';
    document.getElementById('chat-btn').style.visibility='hidden';
}

function close_chat() {
    document.getElementById('chat-window').style.visibility='hidden';
    document.getElementById('chat-btn').style.visibility='visible';
}

function input_data() {
    input_txt = document.getElementById('msg-input').value;
    document.getElementById('msg-input').value='';
    document.getElementById('body-inner').innerHTML+='<span class="msg-right">'+input_txt+'</span>';
}

var msg_in = document.getElementById('msg-input');
msg_in.addEventListener("keyup", function(event) {
    console.log("I was here!!!");
    if (event.keyCode === 13) {
        event.preventDefault();
        document.getElementById("msg_btn").click();
    }
});