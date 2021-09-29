# python-email-telegram
- 궁금해서 만들어본 읽지 않은 메일 텔레그램으로 받아보기
- 나중엔 카카오채널api를 써봐야 겠다

```python
# 딜레이를 주기위해
import time
# 텔레그램 쓰기위해
import telegram
# 셀레니움 쓰려고
from selenium import webdriver
# 일단 크롬드라이버를 받아 경로를 지정해준다. ex) e:do/chromedriver.exe
driver = webdriver.Chrome('chromedriver경로')

# 접속할 사이트 주소
url = 'naver.com'
driver.get(url)
# id, pw값 지정해주기
id = '~~'
pw = '~~'

# find_element_by_xpath를 이용하여 id,pw에 값을 넣고 로그인 버튼 클릭
driver.find_element_by_xpath("//input[@id='userid']").send_keys(id)
driver.find_element_by_xpath("//input[@id='userpass']").send_keys(pw)
driver.find_element_by_xpath("//button[@id='login_btn']").click()

# 무한반복하여 언제든 메일 확인
while True:
    # 혹시몰라 과부하가 걸릴까봐 딜레이를 줫다
    time.sleep(1)
    # 메일 사이트가 자동새로고침이 되지 않기 때문에 새로고침해준다
    driver.refresh()
    time.sleep(2)
    for i in range(3):
        # 확인하지 않은 메일 찾기
        notReadEmail = driver.find_elements_by_xpath("//a[@style='font-weight: bold;']")
        print(driver.find_elements_by_xpath("//a[@style='font-weight: bold;']"))
        for title in notReadEmail:
            print(title.text)
            # 이부분은 텔레그렘 토큰을 받아 넣어주고
            bot = telegram.Bot(token='~~~~')
            # 텔레그램 chat_id를 통해 메세지를 받아볼 수 있다.
            bot.send_message(chat_id=~~~~, text="`"+title.text)


```

