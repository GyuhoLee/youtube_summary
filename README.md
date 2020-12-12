# Youtube_Summary
유튜브 영상의 URL과 원하는 압축률을 입력하면 해당 영상의 자막을 압축률만큼 요약하여 제공합니다.
  
Youtube_Summary는 다음과 같은 상황에서 사용하는 것을 추천드립니다.
  
  - 자동 생성이 아닌, 수동적으로 만든 한국어 자막이 있는 영상만 사용할 수 있습니다.
  - 짧은 문장들보다, 긴 문장들이 많은 경우 더 효과적입니다.
  - 주로 교육적 목적을 갖는 영상들에 대해 사용하시는 것을 추천드립니다.

## Preview

![입력](https://raw.githubusercontent.com/GyuhoLee/youtube_summary/master/img/input.png)

![출력](https://raw.githubusercontent.com/GyuhoLee/youtube_summary/master/img/output.png)



## Installation

1. local 환경에 레파지토리를 clone 해주세요
```
$ git clone https://github.com/GyuhoLee/yotube_summary.git
$ cd youtube_summary/src
```
2. 프로그램 실행을 위해 Python 환경이 필요합니다.

3.Python이 설치되었으면 설정해놓은 가상환경을 실행해주세요. 
```
$ venv\Scripts\activate.bat
```
4. 메인 app을 실행하시고, 로컬 환경에서 프로그램을 사용하실 수 있습니다.
```
$ python app.py
```

## Reference

https://lovit.github.io/nlp/2019/04/30/textrank/
