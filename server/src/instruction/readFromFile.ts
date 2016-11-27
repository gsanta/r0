import * as fs from 'fs';
import * as highland from 'highland';
import * as _ from 'underscore';
import {parseInstruction, parseSleep, parseMotion, InstructionParser} from './parser';
import {InstructionConsumer, InstructionConsumerArgs, consumeInstruction} from './consumer';
import {Instruction} from './Instruction';
import {consumeNil, consumeDelay, consumeCommand} from './consumer';

export function readFromFile(fileName: string, callback: (inst: Instruction) => void) {

    var consumeInstructionPartial = _.partial<InstructionConsumer[], InstructionConsumerArgs, void>(
        consumeInstruction,
        [consumeNil, consumeDelay, consumeCommand]
    );

    highland([fileName])
    .flatMap(highland.wrapCallback(fs.readFile) as any)
    .split()
    .filter((line: string) => {
        return line !== '';
    })
    .map((line: string) => {
        return line.split(' ');
    })
    .map<Instruction | undefined | Highland.Nil>(
        _.partial<InstructionParser[], string[], Instruction | undefined>(parseInstruction, [parseSleep, parseMotion])
    )
    .consume((err: Error, instruction: Instruction | Highland.Nil, push: Function, next: Function) => {
        consumeInstructionPartial({
            err: err,
            instruction: instruction,
            push: push,
            next: next
        });
    })
    .each((val: any) => {
        callback(val);
    });
}
