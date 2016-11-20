
declare namespace __Folktale {
    class Validation<T, U> {

    }

    class Either<T, U> {

    }

    class Maybe<T> {
        isNothing(): boolean;
        isJust(): boolean;
        isEqual(maybe: Maybe<any>): boolean;
        static Nothing(): Maybe<undefined>;
        static Just<T>(val: T): Maybe<T>;
        static of<T>(val: T): Maybe<T>;
        static fromNullable<T>(val: T): Maybe<T>;
        static fromEither<T, U>(val: Either<T, U>): Maybe<U>;
        static fromValidation<T, U>(val: Validation<T, U>): Maybe<U>;

    }

    interface nullary<T> {
        (func: (...params: any[]) => T): () => T;
    }

    interface unary<T, U> {
        (func: (param1: T, ...params: any[]) => U): (param1: T) => U;
    }

    interface binary<T, U, V> {
        (func: (param1: T, param2: U, ...params: any[]) => V): (param1: T, param2: U) => V;
    }

    interface ternary<T, U, V, W> {
        (func: (param1: T, param2: U, param3: V, ...params: any[]) => W): (param1: T, param2: U, param3: V) => W;
    }

    interface show {
        (obj: any): string;
        (maxDepth: number): (obj: any) => string;
    }

    interface identity<T> {
        (obj: T): T;
    }

    interface constant<T> {
        (param1: T, param2: any): T;
    }

    interface apply<T, U> {
        (func: (funcParam: T) => U, param: T): U;
    }

    interface flip<T, U, V> {
        (func: (param1: T, param2: U) => V): (param1: U, param2: T) => V;
    }

    interface compose<T, U, V> {
        (func1: (f1p1: V) => T, func2: (f2p1: U) => V): (param: U) => T;
    }

    interface curry {
        <T1, T2, R>(func: (p1: T1, p2: T2) => R): (p: T1) => (p: T2) => R;
        <T1, T2, T3, R>(func: (p1: T1, p2: T2, p3: T3) => R): (p: T1) => (p: T2) => (p: T3) => R;
        <T1, T2, T3, T4, R>(func: (p1: T1, p2: T2, p3: T3, p4: T4) => R): (p: T1) => (p: T2) => (p: T3) => (p: T4) => R;
        <T1, T2, T3, T4, T5, R>(func: (p1: T1, p2: T2, p3: T3, p4: T4, p5: T5) => R): (p: T1) => (p: T2) => (p: T3) => (p: T4) => (p: T5) => R;
    }

    interface partialize {
        a: number;
        (): number;
    }

    // namespace Maybe {
    //     declare var Nothing: () => Maybe<undefined>;
    //     declare var Just: <T>(val: T) => Maybe<T>;
    //     declare var of: <T>(val: T) => Maybe<T>;
    // }
}

declare module 'folktale' {
    export = __Folktale;
}
