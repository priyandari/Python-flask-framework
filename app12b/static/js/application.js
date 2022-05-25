
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    //var numbers_received = [];
    var detik;
    var objek;
    var myJSON;

    //receive details from server
    socket.on('newnumber', function(msg) {
        console.log("Received number" + msg.number);
        //maintain a list of ten numbers
        //if (numbers_received.length >= 10){
        //    numbers_received.shift()
        //}
        myJSON = JSON.stringify(msg.number);
        //detik = msg.number;            
        //numbers_received.push(msg.number);
        //detik_string = detik.toString()
        //numbers_string = '';
        //for (var i = 0; i < numbers_received.length; i++){
        //    numbers_string = numbers_string + '<p>' + numbers_received[i].toString() + '</p>';
        //}
        $('#log').html(myJSON);
        //$('#log').html(detik_string);
    });

});