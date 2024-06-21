import requests,json,traceback
import pandas as pd
import datetime
from IPython.display import Image, HTML
from urllib.parse import quote

def path_to_image_html(path):
    '''
     This function essentially convert the image url to 
     '<img src="'+ path + '"/>' format. And one can put any
     formatting adjustments to control the height, aspect ratio, size etc.
     within as in the below example. 
    '''

    return '<img src="'+ path + '" style=max-height:124px;"/>'

class live_rank:
    def __init__(self):
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json; charset=utf-8',
            'Referer': 'https://www.bojianger.com/list-intime.html',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'token': 'null'
            }
        self.df_headers = ['房间id','平台','直播间名字','房间地址','主播名','公会','礼物','送礼人数','观众数量','弹幕数量','弹幕人数','小时','直播时长','封面']

    def get_category(self):
        
        url = f"https://bojianger.com/data/api/common/get_categorys.do?date={today}"
        data = requests.get(url,headers=self.headers,data = {})
        cat_data = json.loads(data.text).get('data').get('total')
        cat_dict = {item["cate_id"]:item["cate_name"] for item in cat_data}
        return cat_dict

    def live_crawl(self,url):
        liver_list = []
        print(f'url before response {url}')
        response = requests.get(url,headers=self.headers,data = {})
        totalCount = json.loads(response.text).get('data').get('totalCount')
        
        url = url.replace('pageSize=20',f'pageSize={totalCount}')
        print(f'live crawl {url}')
        response = requests.get(url,headers=self.headers,data = {})
        data = json.loads(response.text)
        rows = data.get('data').get('rows')
        for row in rows:
            name = row.get('name')
            room_id = row.get('rid')
            room_title = row.get('room_title')
            club_name = row.get('club_name')
            gift_person_count = row.get('gift_person_count')
            audience_count = row.get('audience_count')
            danmu_person_count = row.get('danmu_person_count')
            danmu_count = row.get('danmu_count')
            gift_value = row.get('yc_gift_value')
            duration = row.get('duration')
            room_title = row.get('room_title')
            room_thumb = row.get('room_thumb')
            if 'huya' in url:
                room_url = f'www.huya.com/{room_id}'
                platfrom = '虎牙'
            else:
                room_url = f'https://www.douyu.com/{room_id}'
                platfrom = '斗鱼'
            hours = datetime.datetime.now().hour

            row_data = [room_id,platfrom,room_title,room_url,name,club_name,gift_value,gift_person_count,audience_count,danmu_count,danmu_person_count,hours,duration,room_thumb]
            liver_list.append(row_data)
        
        df = pd.DataFrame(data = liver_list,columns = self.df_headers)
        return df
 
    def main(self, url_list):
        concat_list = []
        for url in url_list:
            if 'huya' in url:
                url = url
            else:
                watch_cat = {i:cat_dict[i] for i in cat_dict if cat_dict[i] in watch_list}
                for cat_id,cat_name in watch_cat.items():
                    cat_name = quote(cat_name)
                    url = f'https://bojianger.com/data/api/common/anchor_list.do?date={today}&keyword=&categoryName={cat_name}&categoryId={cat_id}&clubName=total&clubNo=total&orderBy=audience_count&getType=all&pageNum=1&pageSize=20'
            try:
                df = self.live_crawl(url)
                concat_list.append(df)
            except Exception as e:
                print(f'{url} 查询失败',f'失败原因：{e}')
                traceback.print_exc()
        df = pd.concat(concat_list)
        df.to_excel('主播数据.xlsx')
        a = HTML(df.to_html(escape=False ,formatters=dict(封面=path_to_image_html)))
        html = a.data
        with open('主播数据.html', 'w',encoding='utf-8') as f:
            f.write(html)

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


if __name__ == '__main__':
    l = live_rank()
    watch_list = cat_list
    today = datetime.date.today()
    print(today)
    url_list = [
    f'https://bojianger.com/data/api/common/anchor_list.do?date={today}&keyword=&categoryName=%E7%83%AD%E9%97%A8%E6%B8%B8%E6%88%8F&categoryId=270&clubName=total&clubNo=total&orderBy=audience_count&getType=all&pageNum=1&pageSize=20',
    f'https://www.bojianger.com/huya/data/api/common/anchor_intime.do?date={today}&keyword=&window=1h&categoryName=total&orderBy=audience_count&pageNum=1&pageSize=20'
    ]
    cat_dict = l.get_category()
    l.main(url_list)
    
