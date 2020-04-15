import requests
import random
import re
from bs4 import BeautifulSoup
from PIL import Image,ImageTk
from io import BytesIO


class TEC(object):
    def __init__(self,zh,name):
        super(TEC, self).__init__()

        self.url = ['http://cache.neea.edu.cn/Imgs.do']
        self.header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'cache.neea.edu.cn',
            'Referer': 'http://cet.neea.edu.cn/cet/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
        }
        self.session = requests.session()
        self.zh = zh
        self.name = name
        self.login_url = "http://cache.neea.edu.cn/cet/query"
    def yzm(self):
        parm = {
            'c': 'CET',
            'ik': self.zh,
            't': random.random()
        }
        a = self.session.get(url=self.url[0], headers=self.header, params=parm)
        img_url = re.search(r".*?\(\"(.*?)\"\)", str(a.text)).group(1)
        self.img_url = 'http://cet.neea.edu.cn/imgs/' + img_url + '.png'
        cookie = a.headers["Set-Cookie"]
        self.header['Cookie'] = cookie.split(';')[0]
        YZM = self.session.get(url=self.img_url)
        Yzm_img = BytesIO(YZM.content)
        self.img = Image.open(Yzm_img).resize((100,50))
        rander = ImageTk.PhotoImage(self.img)
        return rander
    def getresult(self,yzm):
        self.formdata = {
            'data': 'CET4_192_DANGCI' + ',' + self.zh + ',' + self.name,
            'v': yzm
        }
        result = self.session.get(url=self.login_url, headers=self.header, params=self.formdata)
        return result.text

