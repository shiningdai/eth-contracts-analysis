pragma solidity ^0.8.0;

// Fibonacci sequence test
contract FibonacciSeq {
    uint public expecctedNum;
    uint fib1 = 0;
    uint fib2 = 1;
    uint public finalFib;

    function setFibonacci(uint n) public {
        expecctedNum = n;
    }

    function fibonacci() public returns (uint) {
        if (expecctedNum == 0) {
            return 0;
        }
        if (expecctedNum == 1) {
            return 1;
        }
        uint _idx = 2;
        fib1 = 0;
        fib2 = 1;
        for (_idx = 2; _idx < expecctedNum; _idx++) {
            finalFib = fib1 + fib2;
            fib1 = fib2;
            fib2 = finalFib;
        }
        return finalFib;
    }

    function fibonacci_light() public returns (uint) {
        uint _expecctedNum = expecctedNum;
        if (_expecctedNum == 0) {
            return 0;
        }
        if (_expecctedNum == 1) {
            return 1;
        }
        uint _idx = 2;
        uint _fib1 = 0;
        uint _fib2 = 1;
        uint _finalFib = finalFib;
        for (_idx = 2; _idx < _expecctedNum; _idx++) {
            _finalFib = _fib1 + _fib1;
            _fib1 = _fib2;
            _fib2 = _finalFib;
        }
        finalFib = _finalFib;
        return finalFib;
    }

    function getFinalFibonacci() public view returns (uint) {
        return finalFib;
    }
}