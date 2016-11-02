var fs = require('fs');
// var socket = require('socket.io-client')('http://localhost:5000');
var _ = require('highland');
var fileInput = require('./input/fileInput.js');

var inputFile = 'directions.txt';
var data = _([inputFile]);

data
    .flatMap(_.wrapCallback(fs.readFile))
    .split()
    .filter((line) => {
        return line !== '';
    })
    .map(fileInput.parseInstruction)
    .consume((err, x, push, next) => {
            if (x === _.nil) {
                push(null, x);
            } else {
                if (x.category === 'delay') {
                    setTimeout(() => {
                        console.log('next')
                        next();
                    }, x.value * 1000)
                } else {
                    push(null, x);
                    next();
                }
            }
    })
    .each((val) => {
        console.log(val)
    })

// socket.on('connect', function(){
//    console.log('connection established')
//
//    // var message =   {
//    //     category: 'motion',
//    //     command: 'FORWARD'
//    // }
//     var inputFile = 'directions.txt';
//     var data = _([inputFile]);
//
//     data
//         .flatMap(_.wrapCallback(fs.readFile))
//         .split()
//         .filter((line) => {
//             console.log(line)
//             return line !== '';
//         })
//         .map(fileInput.parseInstruction)
//         .consume((err, x, push, next) => {
//             setTimeout(() => {
//                 push(null, x);
//             }, 1)
//         })
//         .each((val) => {
//             console.log(val)
//         })
//
//    socket.emit('message', JSON.stringify(message));
// });
//
// socket.on('message', function(data){
//    console.log(data)
// });
//
// socket.on('disconnect', function(){});
