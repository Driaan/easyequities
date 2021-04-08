from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep

#DECLARES GLOBAL VARIABLES

exchange = ""

#LOADS LOGIN PAGE

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(options= options)
driver.maximize_window()
driver.get("https://platform.easyequities.io/Account/SignIn")

#LOGIN

def Login(Username, Password):
    global driver
    global element
    element = element = driver.find_element_by_id("user-identifier-input")
    element.send_keys(Username)
    element = driver.find_element_by_id("Password")
    element.send_keys(Password)
    element.send_keys(Keys.RETURN)
    print("\n Logging In...")
    sleep(5)
    element = driver.find_element_by_link_text("ACCOUNT OVERVIEW")
    element.click()
    print("\n Logged In")

#OVERVIEW ACCOUNT SELECTION

def SelectOverviewAccount(OverviewAccount):
    global driver
    global element
    if OverviewAccount == "ZAR":
        print("\n Loading ZAR Account Overview...")
        sleep(5)
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[1]")
        element.click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]").text
        movement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]").text  
        profitorloss = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text 
        print("\n ZAR Account Value:", value, "(", movement, "/", profitorloss, ")")
    elif OverviewAccount == "TFSA":
        print("\n Loading TFSA Account Overview...")
        sleep(5)
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[2]")
        element.click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]").text
        movement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]").text  
        profitorloss = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text 
        print("\n TFSA Account Value:", value, "(", movement, "/", profitorloss, ")")
    elif OverviewAccount == "Demo ZAR":
        print("\n Loading Demo ZAR Account Overview...")
        sleep(5)
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[6]")
        element.click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]").text
        movement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]").text  
        profitorloss = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text 
        print("\n Demo ZAR Account Value:", value, "(", movement, "/", profitorloss, ")")
    elif OverviewAccount == "USD":
        print("\n Loading USD Account Overview...")
        sleep(5)
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[3]")
        element.click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]").text
        movement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]").text  
        profitorloss = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text 
        print("\n USD Account Value:", value, "(", movement, "/", profitorloss, ")")
    elif OverviewAccount == "Demo USD":
        print("\n Loading Demo USD Account Overview...")
        sleep(5)
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector(".outer-slider-container-nav .slick-next > .slider-arrow")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[7]")
        element.click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]").text
        movement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]").text  
        profitorloss = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text  
        print("\n Demo USD Account Value:", value, "(", movement, "/", profitorloss, ")")
    elif OverviewAccount == "AUD":
        print("\n Loading AUD Account Overview...")
        sleep(5)
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[4]")
        element.click()
        value = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[1]").text
        movement = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/div[1]").text  
        profitorloss = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div/div[3]/div[1]").text 
        print("\n AUD Account Value:", value, "(", movement, "/", profitorloss, ")")

#GET PRICE DETAILS FOR A TICKER

def GetTickerDetails(Exchange, Ticker):
    global driver
    global element
    if Exchange == "ZA":
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[6]")
        element.click()
    elif Exchange == "US":
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector(".outer-slider-container-nav .slick-next > .slider-arrow")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[7]")
        element.click()
    elif Exchange == "AU":
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[4]")
        element.click()
    driver.get("https://platform.easyequities.io/ValueAllocation/Buy?contractCode=EQU." + Exchange + "." + Ticker)
    print("\n Loading Ticker...")
    sleep(5)
    name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
    bid = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/span").text
    ask = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/span").text
    last = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[3]/div/span").text
    print("\n Price Details For", name, ": BID =", bid, "; ASK =", ask, "; LAST =", last)

#GET PRICE DETAILS FOR EC10 TOKEN

def GetTokenDetails():
    global driver
    global element
    element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
    element.click()
    element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
    element.click()
    element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[6]")
    element.click()
    driver.get("https://platform.easyequities.io/ValueAllocation/Buy?contractCode=TOKEN.EC.EC10")
    print("\n Loading Token...")
    sleep(5)
    name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
    bid = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/span").text
    ask = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/span").text
    last = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[3]/div/span").text
    print("\n Price Details For", name, ": BID =", bid, "; ASK =", ask, "; LAST =", last)

#TRADE ACCOUNT SELECTION

def SelectTradeAccount(TradeAccount):
    global driver
    global element
    global exchange
    if TradeAccount == "ZAR":
        exchange = "ZA"
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[1]")
        element.click()
        print("\n ZAR Account Selected")
    elif TradeAccount == "TFSA":
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[2]")
        element.click()
        print("\n TFSA Account Selected")       
    elif TradeAccount == "Demo ZAR":
        exchange = "ZA"
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[6]")
        element.click()
        print("\n Demo ZAR Account Selected")
    elif TradeAccount == "USD":
        exchange = "US"
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[3]")
        element.click()
        print("\n USD Account Selected")
    elif TradeAccount == "Demo USD":
        exchange = "US"
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector(".outer-slider-container-nav .slick-next > .slider-arrow")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[7]")
        element.click()
        print("\n Demo USD Account Selected")
    elif TradeAccount == "AUD":
        exchange = "AU"
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_css_selector("#trustaccount-slider > .slick-prev")
        element.click()
        element = driver.find_element_by_xpath("(//div[@id=\'trust-account-types\'])[4]")
        element.click()
        print("\n AUD Account Selected")

#TRADE PARAMETERS SELECTION FOR EQUITIES, ETFS OR ETNS IN ZAR, DEMO ZAR, USD, DEMO USD OR AUD

def TradeEEE(BuyOrSell, Ticker, ValueOrUnits, Amount):
    global driver
    global element
    global exchange
    if BuyOrSell == "Buy":
        driver.get("https://platform.easyequities.io/ValueAllocation/Buy?contractCode=EQU." + exchange + "." + Ticker)
        print("\n Loading Ticker...")
        sleep(5)
        print("\n Placing Trade...")
        name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
        if ValueOrUnits == "Value":
           element = driver.find_element_by_id("js-value-amount")
           element.click()
           element.send_keys(Amount)
           element.send_keys(Keys.RETURN)
           sleep(5)
           element = driver.find_element_by_css_selector(".trade-action-container__right-action-button > .col-xs-12")
           element.click()
           print("\n Bought", Amount, "worth of", name)
        elif ValueOrUnits == "Units":
           element = driver.find_element_by_id("js-number-of-shares")
           element.click()
           element.send_keys(Amount)
           element.send_keys(Keys.RETURN)
           sleep(5)
           element = driver.find_element_by_css_selector(".trade-action-container__right-action-button > .col-xs-12")
           element.click()
           print("\n Bought", Amount, "units of", name)
    elif BuyOrSell == "Sell":
        driver.get("https://platform.easyequities.io/ValueAllocation/Sell?contractCode=EQU." + exchange + "." + Ticker)
        print("\n Loading Ticker...")
        sleep(5)
        print("\n Placing Trade...")
        name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
        if ValueOrUnits == "Value":
            element = driver.find_element_by_id("js-value-amount")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Amount)
            element.send_keys(Keys.RETURN)
            sleep(5)
            element = driver.find_element_by_css_selector("div.content-box:nth-child(14) > div:nth-child(1) > div:nth-child(1)")
            element.click()
            print("\n Sold", Amount, "worth of", name)
        elif ValueOrUnits == "Units":
            element = driver.find_element_by_id("js-percentage-to-sell")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Amount)
            element.send_keys(Keys.RETURN)
            sleep(5)
            element = driver.find_element_by_css_selector("div.content-box:nth-child(14) > div:nth-child(1) > div:nth-child(1)")
            element.click()
            print("\n Sold", Amount, "percent of", name)

#TRADE PARAMETERS SELECTION FOR TFSA

def TradeTFSA(BuyOrSell, Ticker, ValueOrUnits, Amount):
    global driver
    global element
    if BuyOrSell == "Buy":
        driver.get("https://platform.easyequities.io/ValueAllocation/Buy?contractCode=TFSA." + Ticker)
        print("\n Loading Ticker...")
        sleep(5)
        print("\n Placing Trade...")
        name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
        if ValueOrUnits == "Value":
           element = driver.find_element_by_id("js-value-amount")
           element.click()
           element.send_keys(Amount)
           element.send_keys(Keys.RETURN)
           sleep(5)
           element = driver.find_element_by_css_selector(".trade-action-container__right-action-button > .col-xs-12")
           element.click()
           print("\n Bought", Amount, "worth of", name)
        elif ValueOrUnits == "Units":
           element = driver.find_element_by_id("js-number-of-shares")
           element.click()
           element.send_keys(Amount)
           element.send_keys(Keys.RETURN)
           sleep(5)
           element = driver.find_element_by_css_selector(".trade-action-container__right-action-button > .col-xs-12")
           element.click()
           print("\n Bought", Amount, "units of", name)
    elif BuyOrSell == "Sell":
        driver.get("https://platform.easyequities.io/ValueAllocation/Sell?contractCode=TFSA." + Ticker)
        print("\n Loading Ticker...")
        sleep(5)
        print("\n Placing Trade...")
        name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
        if ValueOrUnits == "Value":
            element = driver.find_element_by_id("js-value-amount")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Amount)
            element.send_keys(Keys.RETURN)
            sleep(5)
            element = driver.find_element_by_css_selector("div.content-box:nth-child(14) > div:nth-child(1) > div:nth-child(1)")
            element.click()
            print("\n Sold", Amount, "worth of", name)
        elif ValueOrUnits == "Units":
            element = driver.find_element_by_id("js-percentage-to-sell")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Amount)
            element.send_keys(Keys.RETURN)
            sleep(5)
            element = driver.find_element_by_css_selector("div.content-box:nth-child(14) > div:nth-child(1) > div:nth-child(1)")
            element.click()
            print("\n Sold", Amount, "percent of", name)

#TRADE PARAMETERS SELECTION FOR EC10 CRYPTO TOKEN

def TradeCrypto(BuyOrSell, ValueOrUnits, Amount):
    global driver
    global element
    if BuyOrSell == "Buy":
        driver.get("https://platform.easyequities.io/ValueAllocation/Buy?contractCode=TOKEN.EC.EC10")
        print("\n Loading Token...")
        sleep(5)
        print("\n Placing Trade...")
        name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
        if ValueOrUnits == "Value":
           element = driver.find_element_by_id("js-value-amount")
           element.click()
           element.send_keys(Amount)
           element.send_keys(Keys.RETURN)
           sleep(5)
           element = driver.find_element_by_css_selector(".trade-action-container__right-action-button > .col-xs-12")
           element.click()
           print("\n Bought", Amount, "worth of", name)
        elif ValueOrUnits == "Units":
           element = driver.find_element_by_id("js-number-of-shares")
           element.click()
           element.send_keys(Amount)
           element.send_keys(Keys.RETURN)
           sleep(5)
           element = driver.find_element_by_css_selector(".trade-action-container__right-action-button > .col-xs-12")
           element.click()
           print("\n Bought", Amount, "units of", name)
    elif BuyOrSell == "Sell":
        driver.get("https://platform.easyequities.io/ValueAllocation/Sell?contractCode=TOKEN.EC.EC10")
        print("\n Loading Token...")
        sleep(5)
        print("\n Placing Trade...")
        name = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]").text
        if ValueOrUnits == "Value":
            element = driver.find_element_by_id("js-value-amount")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Amount)
            element.send_keys(Keys.RETURN)
            sleep(5)
            element = driver.find_element_by_css_selector("div.content-box:nth-child(14) > div:nth-child(1) > div:nth-child(1)")
            element.click()
            print("\n Sold", Amount, "worth of", name)
        elif ValueOrUnits == "Units":
            element = driver.find_element_by_id("js-percentage-to-sell")
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(Amount)
            element.send_keys(Keys.RETURN)
            sleep(5)
            element = driver.find_element_by_css_selector("div.content-box:nth-child(14) > div:nth-child(1) > div:nth-child(1)")
            element.click()
            print("\n Sold", Amount, "percent of", name)

#REFRESH PAGE

def Refresh():
    global driver
    global element
    driver.refresh()
    sleep(5)

#CLOSE FIREFOX INSTANCE

def Quit():
    global driver
    global element
    driver.quit()      