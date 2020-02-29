class Sugang():
    def __init__(self):
        self.data = {
            'strCommand': '',       # Save1, Del    $ 필수
            'strSugangYy': '',      # 수강신청 년도 $ 필수
            'strSugangShtm': '',    # 수강신청 학기 $ 필수
            'strDanFg': '1',        # 주간 / 야간   $ 필수
            'strDecs': '',          # 분반          $ 필수
            'strSbjtCd': '',        # 과목코드      $ 필수
            'strUserId': '',        # 학번 (! 타인으로 입력해도 가능 !) $ 필수
            
            'strMajor': '01',       # 전공코드
            'strPobtDiv': '',       # M(전공/교필/기타), C(교선), T(트랙)
            'strSustCd': '',        # (전공일 경우) 학과코드
            'strShyr': '',          # (전공일 경우) 학년
            'strCult': '',          # (교양선택일 경우) 영역
            'strTrackCd': '200590'  # (트랙일 경우) 융복합트랙
            
        }

    def setData(self, args, userId=''):
        self.data['strSugangYy']   = args[0] # 연도
        self.data['strSugangShtm'] = args[1] # 학기
        self.data['strCommand']    = args[2] # Save1, Del
        self.data['strSbjtCd']     = args[3] # 학수번호
        self.data['strDecs']       = args[4] # 분반
        if len(args) > 5:
            self.data['strUserId'] = args[5]
        else:
            self.data['strUserId'] = userId
