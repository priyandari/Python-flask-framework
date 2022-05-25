
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var myJSON;

    //receive details from server
    socket.on('newdata', function(msg) {
        console.log("Received data" + msg.dataAzan);
        myJSON = JSON.stringify(msg.dataAzan);
        $('#log').html(myJSON);
    });

});