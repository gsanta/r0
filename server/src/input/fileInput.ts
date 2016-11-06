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
        return new Instruction(_.first(tokens), _.rest(tokens));
    }
}

export function parseInstruction(parsers: InstructionParser[], tokens: string[]): Instruction | undefined {
    var instruction = parsers.reduce((instr: Instruction | undefined, parser: InstructionParser) => {
        if (!instr) {
            return parser(tokens);
        }
        return instr;
    }, undefined)

    if (!instruction) {
        throw new Error('Tokens could not be parsed, no matching parser');
    }

    return instruction;
}
