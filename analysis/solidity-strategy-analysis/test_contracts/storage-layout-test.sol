// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

// uint256 out;    // v4 error :Only constant variables are allowed at file level.
contract StorageLayoutTest {
    uint128 un128;
    uint64 un64;
    uint256 un256;
    bool bl;
    // uint64[4] unarr; // v1
    uint64[8] unarr; // v2
    mapping(address => uint256) balance;
    // v3
    uint256[] dynarr;
    uint256 un256_1;

    function store(uint256 num) public {
        un256 = num;
    }
}