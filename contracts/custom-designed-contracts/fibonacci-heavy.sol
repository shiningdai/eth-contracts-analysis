pragma solidity ^0.8.0;

// Fibonacci sequence test
contract FibonacciSeq {
    uint public expecctedNum;
    uint public finalFib;
    uint fib1 = 0;
    uint fib2 = 1;

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
    
    function setFibonacci(uint n) public {
        expecctedNum = n;
    }
    function getFibonacci() public view returns (uint){
        return expecctedNum;
    }

    function setFinalFibonacci() public {
        finalFib = 0;
    }
    function getFinalFibonacci() public view returns (uint) {
        return finalFib;
    }
}