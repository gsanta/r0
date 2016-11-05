import * as fs from 'fs';
import * as highland from 'highland';
import * as _ from 'underscore';
import {parseInstruction, parseSleep, parseMotion, InstructionParser, Instruction} from './input/fileInput'
// var socket = require('socket.io-client')('http://localhost:5000');
// var _ = require('highland');
// var fileInput = require('./input/fileInput.js');

var inputFile = 'directions.txt';
var data = highland([inputFile]);

data
    .flatMap(highland.wrapCallback(fs.readFile) as any)
    // .split()
    .filter((line: string) => {
        return line !== '';
    })
    .map((line: string) => line.split(' '))
    .map<Instruction | undefined | Highland.Nil>(
        _.partial<InstructionParser[], string[], Instruction | undefined>(parseInstruction, [parseSleep, parseMotion])
    )
    .consume((err: Error, instruction: Instruction | Highland.Nil, push: Function, next: Function) => {
            if (instruction === highland.nil) {
                push(null, instruction);
            } else {
                instruction = <Instruction> instruction;
                if (instruction.getCategory() === 'DELAY') {
                    setTimeout(() => {
                        console.log('next')
                        next();
                    }, parseInt(instruction.getArgs()[0]) * 1000)
                } else {
                    push(null, instruction);
                    next();
                }
            }
    })
    .each((val: any) => {
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
