from coinbase.wallet.client import Client
from time import sleep
from secret import key, secret #secret is another python file holding Coinbase API key and secret pass
import sys 
#   Set up coinbase client
client = Client(key, secret)

#   Uncomment this to  grab payment id to actually make the purchase
#payment_method = client.get_payment_method()[0] 

#   take user input
currency = input("Enter the crypto currency you want to buy. i.e. BTC , ETH , BCH , LTC: ").upper()

#   Show crypto's current price
buy_price = client.get_buy_price(currency_pair = f'{currency}-USD')
print(f"Here's {currency}'s current buy price {buy_price.amount}")

user_limit_price = float(input("Enter limit order price (USD): "))

#   Ask for padding, padding will make the limit order price into a limit range allows buyer a higher chance at a fill
try:
    padding = float(input("If you want padding, enter a value (2 --> +/- 2USD to limit price, creating range) otherwise enter no:"))
except ValueError:
    padding = None

#   Ask for how much to be spent
user_amount_to_spend = float(input("Enter amount to spend (USD): "))

#   Action loop
while(True):
    #Check current buy price at top of loop
    buy_price = client.get_buy_price(currency_pair = f'{currency}-USD')

    #   If padding is valid, run the price comparison in the range
    if padding != None:
        if((user_limit_price-padding) <= float(buy_price.amount) <= (user_limit_price+padding)):
            #execute a buy
            #buy = client.buy(amount= str( user_amount_to_spend / float(buy_price.amount),currency='LTC', payment_method=payment_method.id))
            #   Exit once bought
            sys.exit("Bought $" + str(user_amount_to_spend) + f" of {currency} or " + str(user_amount_to_spend / float(buy_price.amount)) + f"{currency} at " + buy_price.amount)
    #   Otherwise perform a regular limit order
    else:
        if(float(buy_price.amount) <= user_limit_price):
            #execute a buy
            #buy = client.buy(amount= str( user_amount_to_spend / float(buy_price.amount),currency='LTC', payment_method=payment_method.id))
            #   Exit once bought
            sys.exit("Bought $" + str(user_amount_to_spend) + f" of {currency} or " + str(user_amount_to_spend / float(buy_price.amount)) + f"{currency} at " + buy_price.amount)        
    
    print("Sleeping.")
    sleep(10) #15 mins

