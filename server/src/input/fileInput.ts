import * as _ from 'underscore';

export class Instruction {
    private category: string;
    private args: string[];

    constructor(category: string, args: string[]) {
        this.category = category;
        this.args = args;
    }

    public getCategory(): string {
        return this.category;
    }

    public getArgs(): string[] {
        return this.args;
    }
}

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
        return new Instruction('DELAY', _.rest(tokens));
    }
}

export function parseInstruction(parsers: InstructionParser[], tokens: string[]): Instruction | undefined {
    // return parsers.reduce(())
    var instruction = _.compose(...parsers)(tokens);

    if (!instruction) {
        throw new Error('Tokens could not be parsed, no matching parser');
    }

    return instruction;
    // parsers
    //
    // if (_.first(instructions) === 'SLEEP') {
    //     return {
    //         category: 'delay',
    //         value: _.last(instructions)
    //     }
    // }
    //
    // return {
    //     category: 'motion',
    //     command: _.first(instructions),
    //     args: _.rest(instructions)
    // }
}
