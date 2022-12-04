pragma solidity ^0.6.0;

contract Vuln{
    address payable private _owner;
    mapping(address => uint) private balances;

    constructor(uint _value) public{
        _owner = msg.sender;
        balances[_owner] = _value;
    }

    function transfer(uint _amount) public returns(bool){
        require(balances[msg.sender] + _amount >= 20 && balances[msg.sender] + _amount <= 100);

        if(balances[msg.sender] == 0){
            balances[msg.sender] += _amount - 20;
        }else{
            balances[msg.sender] -= _amount + 20;
        }

        if(balances[_owner] < balances[msg.sender]){
            _owner = msg.sender;
        }

        return true;
    }

    function getBalance() public view returns (uint){
        return balances[msg.sender];
    }

    function getOwner() public view returns (address){
        return _owner;
    }
}
