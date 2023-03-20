import requests

#function to convert currencies
def curr_conv(amt,from_curr,to_curr):
        #api endpoint for conversion
        api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"


        #sending request to api
        responses=requests.get(api_endpoint)

        #json data from response
        data=responses.json()

        #taking rate for our requested currency
        ex_rate=data["rates"][to_curr]

        #calculating converted amount
        conv_amt=amt * ex_rate

        #returning converted amt
        return conv_amt

#inputting amt and currencies from the user
amt=float(input("Enter the amount: "))
from_curr=input("Enter source currency: ").upper()
to_curr=input("Enter target currency: ").upper()

#printing the result
result=curr_conv(amt,from_curr,to_curr)
print(f"{amt} {from_curr} is equal to {result} {to_curr}")


