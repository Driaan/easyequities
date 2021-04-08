<h1 align="center">EasyEquities for Python</h1>

<p align="center">
  <img width="512" src="https://github.com/lohanjs/images/blob/main/EasyEquities.png?raw=true" alt="Logo">
</p>

<p align="center">An unofficial Python library for interacting with an EasyEquities account, built with Selenium.</p>

## Requirements
- Selenium Module for Python
- Firefox
- Geckodriver

## Installation
```
pip install EasyEquities
```

## Example Usage
#### Import the library and set your login details
```
import EasyEquities

EasyEquities.Login("Username", "Password")
```
#### Get an overview of one of your accounts
```
EasyEquites.SelectOverviewAccount("Demo USD")
```
#### Get the price details for an instrument
```
EasyEquities.GetTickerDetails("US", "INTC")
```
#### Set the account to use for trading
```
EasyEquities.SelectTradeAccount("ZAR")
```
#### Place a trade with Equity, ETFs or ETNs
```
EasyEquities.TradeEEE("Buy", "SSW", "Units", "10")
```
#### Close the Firefox instance after usage
```
EasyEquities.Quit()
```
