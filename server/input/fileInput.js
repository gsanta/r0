var _ = require('underscore');

exports.parseInstruction = function (instructionLine) {
    var instructions = instructionLine.split(' ');

    return {
        category: 'motion',
        command: _.first(instructions),
        args: _.rest(instructions)
    }
}
