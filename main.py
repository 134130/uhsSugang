from macro import Macro
from sugang import Sugang
from time import sleep
from datetime import datetime

def waitLogin():
    now = datetime.now()
    while now.minute < 59 and now.hour < 10:
        print('로그인 대기중.. 1분전에 로그인 합니다.  %d시 %d분' % (now.hour, now.minute))
        sleep(20)
        now = datetime.now()

def waitTiming():
    now = datetime.now()
    while now.second <= 50:
        print('수강신청 대기중.. 50초부터 신청합니다. %d초 남음' % (50 - now.second))
        sleep(1)
        now = datetime.now()

if __name__ == '__main__':
    
    sugangList = []

    now = datetime.now()
    year = str(now.year)
    shtm = '1' if now.month < 5 else '2'
    userId, userPw = '', ''

    file = open('SugangList.txt')
    for line in file.readlines():
        if line[0] == '#':
            tmp = line[1:].split(',')
            userId = tmp[0].strip()
            userPw = tmp[1].strip()
        else:
            tmp = [year, shtm]
            for li in line.split(','):
                tmp.append(li.strip())
            sugangList.append(Sugang())
            sugangList[len(sugangList) - 1].setData(tmp, userId)
    file.close()

    # 매크로 시작
    waitLogin()
    
    m = Macro()
    m.login(userId, userPw)

    waitTiming()

    while True:
        for sug in sugangList:
            m.regist(sug)
        sleep(0.25)
