var _ = require('underscore');

exports.parseInstruction = function (instructionLine) {
    var instructions = instructionLine.split(' ');
    if (_.first(instructions) === 'SLEEP') {
        return {
            category: 'delay',
            value: _.last(instructions)
        }
    }
    
    return {
        category: 'motion',
        command: _.first(instructions),
        args: _.rest(instructions)
    }
}
