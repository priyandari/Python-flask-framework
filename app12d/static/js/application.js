
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var myJSON;

    //receive details from server
    socket.on('newdata', function(msg) {
        console.log("Received data" + msg.dataAzan);
        //console.log()
        //myJSON = JSON.stringify(msg.dataAzan);
        myJSON = JSON.stringify(msg.dataAzan.zuhr);
        fajr = JSON.stringify(msg.fajr);
        ttime = JSON.stringify(msg.ttime);
        $('#log').html(myJSON);
        $('#logfajr').html(fajr);
        $('#logtime').html(ttime);
    });

});