import requests
import json
from Check import check
from Shape import shape
shape("     <<VIRUS_CHECKER>>     ")
User_in = input("Please Enter URL OR Domain OR IP OR File Hash\n>> ")
k = check.cheacking(User_in)
api_key = '30a0394aec16f5f15e877bd414011236dc7c43c07adedf591a91aa1d88a88a0f'
if k == "Domain":
    User_inp = "https://" + User_in
elif k == "IP":
    User_inp = "http://" + User_in
else:
    User_inp = User_in
if k == "Domain" or k == "IP" or k == "URL":
    prams = {'apikey': api_key, 'resource': User_inp}
    URL = 'https://www.virustotal.com/vtapi/v2/url/report'
    res = requests.get(URL, params=prams)
    res_json = json.loads(res.content)
    if res_json['positives'] > 0:
        print(f"The Type is {k} \nAnd '{User_in}' is Milicious")
    elif res_json['positives'] <= 0:
        print(f"The Type is {k} \nAnd '{User_in}' is Clean")
    else:
        print("NOT FOUND")
elif k == "File_Hash":
    url = 'https://www.virustotal.com/vtapi/v2/file/report'
    params = {'apikey': api_key, 'resource': User_inp}
    response = requests.get(url, params=params)
    res_json = json.loads(response.content)
    if res_json['positives'] > 0:
        print(f"The Type is {k} \nAnd '{User_in}' is Milicious")
    elif res_json['positives'] <= 0:
        print(f"The Type is {k} \nAnd '{User_in}' is Clean")
    else:
        print("NOT FOUND")
else:
    print("You don't Input correct Value Please Try again")
