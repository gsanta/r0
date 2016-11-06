import * as fs from 'fs';
import * as highland from 'highland';
import * as _ from 'underscore';
import {parseInstruction, parseSleep, parseMotion, InstructionParser, Instruction} from './input/fileInput'
var inputFile = 'directions.txt';
var data = highland([inputFile]);

data
    .flatMap(highland.wrapCallback(fs.readFile) as any)
    .split()
    .filter((line: string) => {
        return line !== '';
    })
    .map((line: string) => {
        return line.split(' ')
    })
    .map<Instruction | undefined | Highland.Nil>(
        _.partial<InstructionParser[], string[], Instruction | undefined>(parseInstruction, [parseSleep, parseMotion])
    )
    .consume((err: Error, instruction: Instruction | Highland.Nil, push: Function, next: Function) => {
            if (instruction === highland.nil) {
                push(null, instruction);
            } else {
                instruction = <Instruction> instruction;
                if (instruction.getCategory() === 'DELAY') {
                    setTimeout(() => {
                        console.log('next')
                        next();
                    }, parseInt(instruction.getArgs()[0]) * 1000)
                } else {
                    push(null, instruction);
                    next();
                }
            }
    })
    .each((val: any) => {
        console.log(val)
    })
