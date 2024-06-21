import requests

url = "https://www.douyu.com/g_mmo"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'max-age=0',
  'cookie': 'dy_did=e9345c7698ec1c061870d65100041701; dy_did=e9345c7698ec1c061870d65100041701; _ga=GA1.1.622830132.1717469499; acf_ssid=1729709911377771554; acf_web_id=7376475334377486095; acf_ab_pmt=1479%23cover_select_web%23B; acf_ab_ver_all=1479; acf_ab_vs=cover_select_web%3DB; acf_did=e9345c7698ec1c061870d65100041701; _clck=rqe3u8%7C2%7Cfmm%7C0%7C1626; loginrefer=pt_hfc9ig98i4e4; smidV2=202406141157283ef90777e79e7491fb91382cc4b2dba5002d10f82e1bee910; _ga_7RMFJRR7D2=GS1.1.1718353825.3.0.1718353826.59.0.1367554951; _clsk=1mli8hi%7C1718358540313%7C1%7C0%7Cf.clarity.ms%2Fcollect; _ga_5JKQ7DTEXC=GS1.1.1718356728.8.1.1718360810.56.0.1842471749',
  'priority': 'u=0, i',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.split('window.$DATA = ')[1])
