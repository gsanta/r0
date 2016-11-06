"use strict";
var _ = require('underscore');
var Instruction = (function () {
    function Instruction(category, args) {
        this.category = category;
        this.args = args;
    }
    Instruction.prototype.getCategory = function () {
        return this.category;
    };
    Instruction.prototype.getArgs = function () {
        return this.args;
    };
    return Instruction;
}());
exports.Instruction = Instruction;
function parseSleep(tokens) {
    if (_.first(tokens) === 'SLEEP') {
        return new Instruction('DELAY', _.rest(tokens));
    }
}
exports.parseSleep = parseSleep;
function parseMotion(tokens) {
    var commands = ['FORWARD', 'REVERSE', 'TURN_LEFT', 'TURN_RIGHT', 'STOP'];
    if (_.indexOf(commands, _.first(tokens)) !== -1) {
        return new Instruction(_.first(tokens), _.rest(tokens));
    }
}
exports.parseMotion = parseMotion;
function parseInstruction(parsers, tokens) {
    var instruction = parsers.reduce(function (instr, parser) {
        if (!instr) {
            return parser(tokens);
        }
        return instr;
    }, undefined);
    if (!instruction) {
        throw new Error('Tokens could not be parsed, no matching parser');
    }
    return instruction;
}
exports.parseInstruction = parseInstruction;
//# sourceMappingURL=fileInput.js.map