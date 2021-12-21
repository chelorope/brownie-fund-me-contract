from brownie import FundMe
from scripts.utils import get_account

def fund():
  fund_me = FundMe[-1]
  account = get_account()
  entrance_fee = fund_me.getEntranceFee()
  print(f"The current entry fee is {entrance_fee}")
  print("Funding")
  fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
  fund_me = FundMe[-1]
  account = get_account()
  print("Withdrawing funds")
  funds = fund_me.withdraw({"from": account})
  print(f"Funds withdrawn {funds}")

def main():
  fund()
  withdraw()