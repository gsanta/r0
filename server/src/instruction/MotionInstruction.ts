import {Instruction} from './Instruction';

export class MotionInstruction extends Instruction {
    private direction: string;

    constructor(direction: string, args: string[]) {
        super('MOTION', args);
        this.direction = direction;
    }

    public getDirection() {
        return this.direction;
    }
}
