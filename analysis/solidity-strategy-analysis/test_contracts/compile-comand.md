# command 1
dsr@dell-PowerEdge-R740:~/compilers/solidity/build/solc$ ./solc test_contracts/location-test.sol --bin --abi --asm -o ./test_out

# command 2
dsr@dell-PowerEdge-R740:~/compilers/solidity/build/solc$ ./solc test_contracts/storage-layout-test.sol -o ./layout_test/ --optimize --storage-layout --asm --opcodes --bin --abi --overwrite
Warning: This is a pre-release compiler version, please do not use it in production.

// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract LocationTest {
    uint128 sa128;
    uint256 sb256;
    uint128 sc128;
    uint64 sd64;
    uint64 se64;
    uint128[4] arrf;
    
    function store(uint128 _sa128, uint256 _sb256, uint128 _sc128, uint64 _sd64, uint64 _se64) public {
        sa128 = _sa128;
        sb256 = _sb256;
        sc128 = _sc128;
        sd64 = _sd64;
        se64 = _se64;
        arrf = [_sa128, _sc128, _sc128, _sc128];
        uint128[4] storage fa = arrf;
    }

}


contract LocationTest {

    mapping (address => mapping (address => uint256)) private _allowances;
    function store(address owner, uint256 val) public {
        mapping (address => uint256) storage _fm = _allowances[msg.sender];
        _fm[owner] += val;
    }
}


contract LocationTest {

    uint64[4] state_array;

    function store(uint64[4] memory arg) public {
        // uint64[16] storage local_sarr = arg;
        // uint64[16] storage local_sarr = [1, 2, 3, 4];
        uint64[4] storage local_sarr = state_array;
        for ( uint idx = 0; idx < 4; idx++) {
            local_sarr[idx] += arg[idx];
        }
        state_array = local_sarr;
    }
}


./solc test_contracts/fibonacci-heavy-only.sol --bin --abi --asm -o ./test_out
