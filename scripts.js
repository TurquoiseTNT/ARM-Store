function start() {
    document.getElementById("connect").style.visibility = 'visible';
    document.getElementById("main").style.visibility = 'hidden';
}
function setserver() {
    var ip = document.getElementById('address').value
    document.getElementById("connect").style.visibility = 'hidden';
    document.getElementById("main").style.visibility = 'visible';
    document.getElementById("ipshow").innerHTML = "<button class='button' onclick='start()'>CONNECT TO DIFFERENT SERVER</button> Connected To: " + ip;
}