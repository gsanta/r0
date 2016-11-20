import {Instruction} from './Instruction';
import * as highland from 'highland';

export interface InstructionConsumerArgs {
    err: Error;
    instruction: Instruction | Highland.Nil;
    push: Function;
    next: Function;
}

export interface InstructionConsumer {
    (args: InstructionConsumerArgs): boolean;
}

export function consumeNil(args: InstructionConsumerArgs): boolean {
    var {instruction, push} = args;

    if (instruction === highland.nil) {
        push(null, instruction);
        return true;
    }

    return false;
}

export function consumeDelay(args: InstructionConsumerArgs): boolean {
    var {instruction, next} = args;

    if ((<Instruction> instruction).getCategory() === 'DELAY') {
        setTimeout(
            () => {
                next();
            },
            parseInt((<Instruction> instruction).getArgs()[0], 10) * 1000
        );
        return true;
    }
    return false;
}

export function consumeCommand(args: InstructionConsumerArgs): boolean {
    var {instruction, push, next} = args;
    if ((<Instruction> instruction).getCategory() !== 'DELAY') {
        push(null, instruction);
        next();
        return true;
    }
    return false;
}

export function consumeInstruction(consumers: InstructionConsumer[], args: InstructionConsumerArgs) {
    consumers.reduce(
        (consumed: boolean, nextConsumer: InstructionConsumer) => {
            if (!consumed) {
                var success = nextConsumer(args);
                return success;
            }

            return true;
        },
        false
    );
}
