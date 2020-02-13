import requests
import json
import sys

if len(sys.argv) >= 2:
    target = sys.argv[1]
    url = "https://crt.sh/?q="+ target + "&output=json"
    r = requests.get(url = url) 
    data = r.json()
    res = [ sub['name_value'] for sub in data ] 
    subdomains = list(dict.fromkeys(res))
    if len(sys.argv) >= 3:
        filename = str(sys.argv[2])
        f = open(filename,'a+')
        for subdomain in subdomains:
            print(subdomain)
            f.write(subdomain + "\n")
        print("[+] Results Saved in "+filename)
        f.close()

    else: 
        for subdomain in subdomains:
            print(subdomain) 
else: 
    print("Usage : ",sys.argv[0]," target.com rsltfile.txt")