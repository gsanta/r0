import * as fs from 'fs';
import * as highland from 'highland';
import * as _ from 'underscore';
import {parseInstruction, parseSleep, parseMotion, InstructionParser} from './instruction/parser';
import {InstructionConsumer, InstructionConsumerArgs, consumeInstruction} from './instruction/consumer';
import {Instruction} from './instruction/Instruction';
import {consumeNil, consumeDelay, consumeCommand} from './instruction/consumer';
import * as http from 'http';
import * as socketIO from 'socket.io-client';

var socket = socketIO('http://localhost:5000');
// var app = http.createServer(handler)
// var io = socketIO(app);
//
// app.listen(80);
//
// function handler (req: any, res: any) {
//   // fs.readFile(__dirname + '/index.html',
//   // function (err, data) {
//   //   if (err) {
//   //     res.writeHead(500);
//   //     return res.end('Error loading index.html');
//   //   }
//   //
//   //   res.writeHead(200);
//   //   res.end(data);
//   // });
// }

socket.on('connect', function (s: any) {
    console.log('connection established');
    socket.send('abcde');
});
  // socket.emit('news', { hello: 'world' });
  // socket.on('my other event', function (data) {
  //   console.log(data);
  // });

var inputFile = 'directions.txt';
var data = highland([inputFile]);

var consumeInstructionPartial = _.partial<InstructionConsumer[], InstructionConsumerArgs, void>(
    consumeInstruction,
    [consumeNil, consumeDelay, consumeCommand]
);

data
    .flatMap(highland.wrapCallback(fs.readFile) as any)
    .split()
    .filter((line: string) => {
        return line !== '';
    })
    .map((line: string) => {
        return line.split(' ');
    })
    .map<Instruction | undefined | Highland.Nil>(
        _.partial<InstructionParser[], string[], Instruction | undefined>(parseInstruction, [parseSleep, parseMotion])
    )
    .consume((err: Error, instruction: Instruction | Highland.Nil, push: Function, next: Function) => {
        consumeInstructionPartial({
            err: err,
            instruction: instruction,
            push: push,
            next: next
        });
    })
    .each((val: any) => {
        console.log(val)
    });
