import {Instruction} from './Instruction';
import * as _ from 'underscore';

export interface InstructionParser {
    (tokens: string[]): Instruction | undefined;
}

export function parseSleep(tokens: string[]): Instruction | undefined {
    if (_.first(tokens) === 'SLEEP') {
        return new Instruction('DELAY', _.rest(tokens));
    }
}

export function parseMotion(tokens: string[]): Instruction | undefined {
    var commands = ['FORWARD', 'REVERSE', 'TURN_LEFT', 'TURN_RIGHT', 'STOP'];
    if (_.indexOf(commands, _.first(tokens)) !== -1) {
        return new Instruction(_.first(tokens), _.rest(tokens));
    }
}

export function parseInstruction(parsers: InstructionParser[], tokens: string[]): Instruction | undefined {
    var instruction = parsers.reduce(
        (instr: Instruction | undefined, parser: InstructionParser) => {
            if (!instr) {
                return parser(tokens);
            }
            return instr;
        },
        undefined
    );

    if (!instruction) {
        throw new Error('Tokens could not be parsed, no matching parser');
    }

    return instruction;
}
