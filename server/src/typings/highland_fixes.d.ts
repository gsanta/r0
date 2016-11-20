

declare namespace Highland {
    interface Stream<R> extends NodeJS.EventEmitter {
        split<U>(): Stream<U>;
    }
}

// declare module 'highland_fixes' {
//     export interface abcde {
//         a: string;
//     }
// }
