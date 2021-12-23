from brownie import network, accounts, exceptions
from scripts.utils import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
import pytest;

def test_can_fund_and_withdraw():
    print(f"Network name {network.show_active()}")
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
  if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
    pytest.skip("only for local testing")
  account = get_account()
  fund_me = deploy_fund_me()
  bad_actor = accounts.add() # Returns a random blanck account
  with pytest.raises(exceptions.VirtualMachineError): # Tests "Only owner" modifier
    fund_me.withdraw({"from": bad_actor})