

Contract demo1 {
    uint128 a;
    uint256 b;
    uint128 c;
    ...
}

Contract demo1_1 {
    functionA() {
        Storage uint128 a;
        ...
    }
    functionB() {
        Storage uint128 b;
        ...
    }
}


Contract demo2 {
    uint128 a;
    uint64 b;
    uint64 c;
    functionA() {
        do something on a;
        ...
    }
    functionB() {
        do something on b;
    }
    functionC() {
        do something on c;
    }
}


Contract demo {
    uint128 state_var1;
    uint64 state_var2;
    ...
    function fun1() {
        ...
        do something(on state var);
        ...
    }
    ... 
    function funx() {
        ...
        do something(on state var);
        ...
    }
}

608060405234801561001057600080fd5b506102c
6d69742e34396132646239390058
0x60
0x80
0x60
0x40
0x52
0x34
0x80
0x15
...
0x39
0x61
0x32
0x64
0x62
0x39
0x39
0x00
0x58