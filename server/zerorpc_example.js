var zerorpc = require('zerorpc');
var fs = require('fs');

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var client = new zerorpc.Client();
client.connect('tcp://127.0.0.1:4242');



app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html'); 
});

var timeFrame = 0.2;

io.on('connection', function(socket) {
    console.log('a user connected');

    socket.on('chat message', function(msg) {
        console.log('message: ' + msg);
        if (msg === 'f') {
	    client.invoke('forward', timeFrame, function(error, res, more) {
                console.log(res);
            });
	} else if (msg === 'b') {
	    client.invoke('reverse', timeFrame, function(error, res, more) {
                console.log(res);
            });
	} else if (msg === 'l') {
	    client.invoke('turn_left', timeFrame, function(error, res, more) {
                console.log(res);
            });
	} else if (msg === 'r') {
	    client.invoke('turn_right', timeFrame, function(error, res, more) {
                console.log(res);
            });
	}
    });

    socket.on('disconnect', function() {
        console.log('user disconnected');
    });
});

/*function handleRequest(req, res) {
    fs.readFile('../client/index.html', function (err, data) {
        res.writeHead(200, {'Content-Type': 'text/html', 'Content-Length': data.length});
	res.write(data);
	res.end();
    });
}*/


http.listen(3000, function() {
    console.log('server is listening on port 3000');
});


