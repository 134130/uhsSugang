import requests
import re
from sugang import Sugang

class Macro():
    def __init__(self):
        self.session = requests.Session()
        self.host = 'https://shiis.uhs.ac.kr/'
        self.hdr = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729)'
        }
        self.regex = re.compile('/<strRsltMsg>(.+)</strRsltMsg>/')

    def login(self, userid, userpw):
        url = self.host + 'hsudoc/sys.Login.doj'
        loginData = {
            'strCommand': 'LOGIN',
            'strTarget' : 'MAIN',
            'strLoginId': userid,
            'strLoginPw': userpw
        }

        res = self.session.post(url, data=loginData, headers=self.hdr)
        print('[+] Login Success!')

    def regist(self, sugang):
        url = self.host + 'hsudoc/sug.SugSugangMng.do'
        res = self.session.post(url, data=sugang.data, headers=self.hdr)

        print(regex.findall(res.text))
