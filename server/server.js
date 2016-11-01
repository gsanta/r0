var fs = require('fs');
var socket = require('socket.io-client')('http://localhost:5000');
var _ = require('highland');
var fileInput = require('./input/fileInput.js');

// fs.readFile('directions.txt', 'utf8', function (err,data) {
//   if (err) {
//     return console.log(err);
//   }
//   var lines = data.split(/\r?\n/)
// 	.filter(line => line != '')
// 	.map(line => line.split(' '))
//
//   console.log(lines);
// });


socket.on('connect', function(){
   console.log('connection established')

   // var message =   {
   //     category: 'motion',
   //     command: 'FORWARD'
   // }
    var inputFile = 'directions.txt';
    var data = _([inputFile]);

    data
        .flatMap(_.wrapCallback(fs.readFile))
        .split()
        .filter((line) => {
            console.log(line)
            return line !== '';
        })
        .map(fileInput.parseInstruction)

   socket.emit('message', JSON.stringify(message));
});

socket.on('message', function(data){
   console.log(data)
});

socket.on('disconnect', function(){});
