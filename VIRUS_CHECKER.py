import requests
import json
from Check import check
from Shape import shape
api_key = '30a0394aec16f5f15e877bd414011236dc7c43c07adedf591a91aa1d88a88a0f'
get_out = True
counter = 0
chooses = ["Domain", "IP", "URL"]
shape("     <<VIRUS_CHECKER>>     ")
while get_out is True:
    User_in = input("Please Enter URL OR Domain OR IP OR File Hash\n>> ")
    k = check.cheacking(User_in)
    if k == "Domain":
        User_inp = "https://" + User_in
    elif k == "IP":
        User_inp = "http://" + User_in
    else:
        User_inp = User_in
    if k in chooses:
        prams = {'apikey': api_key, 'resource': User_inp}
        URL = 'https://www.virustotal.com/vtapi/v2/url/report'
        res = requests.get(URL, params=prams)
        res_json = json.loads(res.content)
        try:
            if res_json['positives'] > 0:
                print(
                    f"\nThe Type is >>>>>>> {k} \n'{User_in}' is >>>>>>>  Milicious\n")
                get_out = False
            elif res_json['positives'] <= 0:
                print(
                    f"\nThe Type is >>>>>>> {k} \n \n'{User_in}' is >>>>>>>  Clean\n")
                get_out = False
        except:
            print("You don't Input correct Value Please Try again")
    elif k == "File_Hash":
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': api_key, 'resource': User_inp}
        response = requests.get(url, params=params)
        res_json = json.loads(response.content)
        try:
            if res_json['positives'] > 0:
                print(
                    f"\nThe Type is >>>>>>> {k} \n \n'{User_in}' is >>>>>>>  Milicious\n")
                get_out = False
            elif res_json['positives'] <= 0:
                print(
                    f"\nThe Type is >>>>>>> {k} \n'{User_in}' is >>>>>>>  Clean\n")
                get_out = False
        except:
            print("\n>You don't Input correct Value Please Try again<\n")
    counter += 1
    if counter == 2 or counter == 4 and get_out is True:
        h = input("To quit Please Enter (q) to continue (any another key)\n>>>>")
        k = h.lower()
        if k == "q":
            get_out = False
        else:
            get_out = True
    elif counter > 4 and get_out is True:
        print("\nOut of Rtying, Please Make sure about the input and try again later\n")
        get_out = False

print("Thank You For Using <<VIRUS_CHECKER>>\n")
