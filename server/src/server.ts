declare var require: any;
import {Instruction} from './instruction/Instruction';
import {readFromFile} from './instruction/readFromFile';
import * as fs from 'fs';
var kafka = require('kafka-node'),
    Producer = kafka.Producer,
    client = new kafka.Client('localhost:2181'),
    producer = new Producer(client);

var inputFile = process.argv[2];//'directions.txt';
console.log(inputFile);
fs.readFile(inputFile, 'utf8', (err: any, data: any) => {
  if (err) throw err;
  console.log(data);
});
// producer.on('ready', function() {
//     console.log('connection established');
//     readFromFile(inputFile, (instr: Instruction) => {
//         // socket.send(instr);
//
//         let payloads = [
//             {
//                 topic: 'test',
//                 messages: JSON.stringify(instr)
//             }
//         ];
//         producer.send(payloads, function(err: any, data: any) {
//             console.log(data);
//         });
//     });
// });
//
// producer.on('error', function(err: any) {
//     console.log(err);
// });
