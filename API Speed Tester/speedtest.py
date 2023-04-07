"""this code also works as the ping command used in linux 
as you can input urls of website and check your connection times to it"""

import requests
import time


#api_url = "https://disposable.debounce.io/?email=info@example.com"
api_url=input("Enter your API URL to be tested: ") 


num_requests = 20


response_times = []
for i in range(num_requests):
    start_time = time.time()
    response = requests.get(api_url)
    end_time = time.time()
    response_time = end_time - start_time
    response_times.append(response_time)
    print(f"Request {i+1}: {response_time} seconds")


avg_response_time = sum(response_times) / len(response_times)
max_response_time = max(response_times)
min_response_time = min(response_times)
print(f"\nNumber of requests: {num_requests}")
print(f"Average response time: {avg_response_time} seconds")
print(f"Maximum response time: {max_response_time} seconds")
print(f"Minimum response time: {min_response_time} seconds")
if avg_response_time<0.200:
    print("Your Website/Api is faster than the average")
elif 0.200<avg_response_time<1.000:
    print("You Website/Api response time is average")
else:
    print("your Website/Api is slower than the average")
        
    
