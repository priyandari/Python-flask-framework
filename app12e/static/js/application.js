
$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var logdate;
    var logfajr;
    var logtime;

    //receive details from server
    socket.on('newdata', function(msg) {
        console.log("Received data" + msg.dataAzan);
        //console.log()
        //myJSON = JSON.stringify(msg.dataAzan);
        logdate = JSON.stringify(msg.dataAzan.ddate);
        logdatetime = JSON.stringify(msg.dataAzan.dtime);
        logfajr = JSON.stringify(msg.dataAzan.fajr);
        logtime = JSON.stringify(msg.dataAzan.ttime);
        //$('#txtdate').html(logdate.replace(/['"]+/g, ''));
        $('#txtdatetime').html(logdatetime.replace(/['"]+/g, ''));
        $('#txtfajr').html(msg.dataAzan.fajr.replace(/['"]+/g, ''));
        $('#txttime').html(msg.dataAzan.ttime.replace(/['"]+/g, ''));
    });

});