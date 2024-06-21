import requests,json
import pandas as pd
import time
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

class daduoduo:
    def __init__(self) -> None:
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'authtoken': 'Pc:ShuJu:9ec72f89e4ec471b98ea2ccefb10ce83',
            'content-length': '0',
            'cookie': 'ESDataStatusInfo1_2024-06-20={"isDayDataOk":1,"isWeekDataOk":1,"isMonthDataOk":1,"dayDays":2}; _clck=qb0hgg%7C2%7Cfms%7C0%7C1632; utoken=Pc:ShuJu:9ec72f89e4ec471b98ea2ccefb10ce83; acw_tc=0b3283ba17188557220278230e3c103b46733ad434678bdcbbdbd3c2363da6; _clsk=2hdl46%7C1718855729092%7C3%7C1%7Cx.clarity.ms%2Fcollect; SERVERID=b6ea75e1f0be2384bba107e2b2b61342|1718855731|1718855722; SERVERID=b6ea75e1f0be2384bba107e2b2b61342|1718855781|1718855722',
            'origin': 'https://daduoduo.com',
            'priority': 'u=1, i',
            'referer': 'https://daduoduo.com/live/liveSearch?keyword=%E4%BA%91%E4%B8%8A%E5%A4%A7%E9%99%86',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
            }
        self.df_headers = ['房间id','平台','直播间名字','房间地址','主播名','公会','礼物','送礼人数','观众数量','弹幕数量','弹幕人数','小时','直播时长','封面']

    def get_detail(self,RoomID):
        url = f"https://daduoduo.com/ajax/dyRoomDetailAjax.ashx?action=GetLiveRoomDetail&roomId={RoomID}&fromSrc=&exactValueFlag="
        payload = {}
        headers = self.headers
        response = requests.request("POST", url, headers=headers, data=payload)
        return json.loads(response.text)


    def search(self,keyword):
        liver_list = []
        url = f'https://daduoduo.com/ajax/dyLiveDataAjax.ashx?action=GetLiveRoomRankList&keyword={keyword}&dayType=7&sortType=2&sortValue=DESC&pageIndex=1&pageSize=100&exactValueFlag='
        # url = f"https://daduoduo.com/ajax/dyLiveDataAjax.ashx?action=GetSearchTipForLiveRoom&keyword={keyword}&dayType=30&exactValueFlag="
        print(url)
        payload = {}
        headers = self.headers
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        if data.get('msg') == 'success':
            total = data.get('data').get('total')
            print(f'get data {total}')
            room_data = data.get('data').get('data')          
            for room in room_data:
                RoomId = room.get('RoomId')
                blogger = room.get('blogger')
                UserId = blogger.get('UserId')
                Name = blogger.get('Name')
                FansCnt = blogger.get('FansCnt')
                # HeaderImg = blogger.get('HeaderImg').spilt('/resize')[0]
                LiveName = room.get('LiveName')
                RoomPic = room.get('RoomPic').split('/resize')[0]
                BeginTime = room.get('BeginTime')
                LiveTime = room.get('LiveTime')
                room_detail = self.get_detail(RoomId).get('data').get('room')
                room_url = 'https://live.douyin.com/'+room_detail.get('WebRoomId')
                TotalUser = room_detail.get('TotalUser')
                MaxUserCnt = room_detail.get('MaxUserCnt')
                time.sleep(0.5)
                row_data = [RoomId,'抖音',LiveName,room_url,Name,None,None,None,TotalUser,None,MaxUserCnt,BeginTime,LiveTime,RoomPic]
                liver_list.append(row_data)
            df = pd.DataFrame(data = liver_list,columns = self.df_headers)
            print(len(df.index))
        return df

    def main(self,keyword_list=['mmo']):
        concat_list = []
        for keyword in keyword_list:
            df = self.search(keyword)
            concat_list.append(df)
        df = pd.concat(concat_list)
        df.sort_values(by="观众数量",ascending=False)
        df.to_excel('抖音主播数据.xlsx')
        a = HTML(df.to_html(escape=False ,formatters=dict(封面=path_to_image_html)))
        html = a.data
        with open('抖音主播数据.html', 'w',encoding='utf-8') as f:
            f.write(html)

if __name__ == '__main__':
    d = daduoduo()
    keyword_list = ['mmo','mmorpg','手游',]
    d.main(keyword_list)