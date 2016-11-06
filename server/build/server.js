"use strict";
var fs = require('fs');
var highland = require('highland');
var _ = require('underscore');
var fileInput_1 = require('./input/fileInput');
var inputFile = 'directions.txt';
var data = highland([inputFile]);
data
    .flatMap(highland.wrapCallback(fs.readFile))
    .split()
    .filter(function (line) {
    return line !== '';
})
    .map(function (line) {
    return line.split(' ');
})
    .map(_.partial(fileInput_1.parseInstruction, [fileInput_1.parseSleep, fileInput_1.parseMotion]))
    .consume(function (err, instruction, push, next) {
    if (instruction === highland.nil) {
        push(null, instruction);
    }
    else {
        instruction = instruction;
        if (instruction.getCategory() === 'DELAY') {
            setTimeout(function () {
                console.log('next');
                next();
            }, parseInt(instruction.getArgs()[0]) * 1000);
        }
        else {
            push(null, instruction);
            next();
        }
    }
})
    .each(function (val) {
    console.log(val);
});
//# sourceMappingURL=server.js.map