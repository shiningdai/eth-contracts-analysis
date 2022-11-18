// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract LocationTest {

    uint64[4] state_array;

    function store(uint64[4] memory arg) public {
        uint64[4] storage local_sarr = state_array;
        for ( uint idx = 0; idx < 4; idx++) {
            local_sarr[idx] += arg[idx];
        }
        state_array = local_sarr;
    }
}