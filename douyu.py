import json
import requests

url = "https://www.douyu.com/g_mmo" # g_mmo #g_xyzx

payload={}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': 'dy_did=51bd0a0e9cee0075daa0b6b277241601; dy_did=51bd0a0e9cee0075daa0b6b277241601; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1718378245; _ga=GA1.1.1900918984.1718378245; _clck=1qmyp58%7C2%7Cfmm%7C0%7C1626; acf_ssid=1729705513332647616; acf_web_id=7380378364432902407; acf_ab_pmt=1479%23cover_select_web%23B; acf_ab_ver_all=1479; acf_ab_vs=cover_select_web%3DB; _clsk=1d2b1jb%7C1718378246496%7C1%7C0%7Cx.clarity.ms%2Fcollect; acf_did=51bd0a0e9cee0075daa0b6b277241601; _ga_5JKQ7DTEXC=GS1.1.1718378245.1.1.1718378286.19.0.2047539387; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1718378286',
  'priority': 'u=0, i',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

r_text = response.text.split('window.$DATA = ')[1].split('};')[0] +'}'
with open('test.json','w',encoding='utf-8') as f:
    f.write(r_text)
# print(r_text[-1:-5])
r_json = json.loads(r_text)
cat_list = r_json.get('cateTabList')
cat_list = [i.get('name') for i in cat_list]
print(cat_list)
