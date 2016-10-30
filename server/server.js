var fs = require('fs')
socket = require('socket.io-client')('http://localhost:5000');


fs.readFile('directions.txt', 'utf8', function (err,data) {
  if (err) {
    return console.log(err);
  }
  var lines = data.split(/\r?\n/)
	.filter(line => line != '')
	.map(line => line.split(' '))

  console.log(lines);
});

socket.on('connect', function(){
   console.log('connection established')
   
   var message =   {
       category: 'motion',
       command: 'FORWARD'
   }

   socket.emit('message', JSON.stringify(message));
});

socket.on('message', function(data){
   console.log(data)
});

socket.on('disconnect', function(){});


