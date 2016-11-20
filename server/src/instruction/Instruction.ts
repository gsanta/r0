
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
