<h1 align="center">EasyEquities for Python</h1>

<p align="center">
  <img width="512" src="https://github.com/lohanjs/images/blob/main/EasyEquities.png?raw=true" alt="Logo">
</p>

<p align="center">An unofficial Python library for interacting with EasyEquities.</p>

## Requirements
- Time
- Selenium
- Firefox
- Geckodriver

## Warning
Code might require modification, depending on which accounts you have activated. As-is usage assumes you have all accounts activated except RA, Provident and Pension

## Guide
```python
#Import the library and login to you account
import EasyEquities
EasyEquities.Login("Username", "Password")

#Get an overview of one of your accounts - options are "ZAR"/"Demo ZAR"/"TFSA"/"USD"/"Demo USD"/"AUD"
EasyEquities.SelectOverviewAccount("ZAR")

#Get price details for a Stock/ETF/ETN from EE - Exchange options are "ZA"/"US"/"AU"
EasyEquities.GetTickerDetails("US", "INTC")

#Get price details for the EC10 token from EE
EasyEquities.GetTokenDetails()

#Select an account to place trades with - options are "ZAR"/"Demo ZAR"/"TFSA"/"USD"/"Demo USD"/"AUD" - has to be set before continuing with commands below
EasyEquities.SelectTradeAccount("ZAR")

#Buy or sell a Stock/ETF/ETN on ZAR/Demo ZAR/USD/Demo USD/AUD - options are "Buy"/"Sell", "Value"/"Units" (for choosing a currency value or instrument amount/percentage)
EasyEquities.TradeEEE("Buy", "SSW", "Units", "10")

#Buy or sell on TFSA
EasyEquities.TradeTFSA("Sell", "STXNDQ", "Units", "100")

#Buy or sell the EC10 token
EasyEquities.TradeCrypto("Buy", "Value", "111.11")

#Refresh the active command - for getting update account overview or price details
EasyEquities.Refresh()

#Close the background Firefox instance after usage
EasyEquities.Quit()
```
