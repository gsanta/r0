import * as fs from 'fs';
import * as highland from 'highland';
import * as _ from 'underscore';
import {parseInstruction, parseSleep, parseMotion, InstructionParser} from './instruction/parser';
import {InstructionConsumer, InstructionConsumerArgs, consumeInstruction} from './instruction/consumer';
import {Instruction} from './instruction/Instruction';
import {consumeNil, consumeDelay, consumeCommand} from './instruction/consumer';
import * as http from 'http';
import * as socketIO from 'socket.io-client';
import {readFromFile} from './instruction/readFromFile';

var socket = socketIO('http://localhost:5000');

var inputFile = 'directions.txt';
socket.on('connect', function (s: any) {
    console.log('connection established');
    readFromFile(inputFile, (instr: Instruction) => {
        socket.send(instr);
    });
});

// var data = highland([inputFile]);
//
// var consumeInstructionPartial = _.partial<InstructionConsumer[], InstructionConsumerArgs, void>(
//     consumeInstruction,
//     [consumeNil, consumeDelay, consumeCommand]
// );
