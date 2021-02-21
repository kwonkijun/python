from PyQt5.QtWidgets import *
import sys
from PyQt5 import uic
from selenium import webdriver
import time
from PyQt5.QtCore import QThread, QObject, pyqtSignal
import random
import urllib.request as req
from PyQt5.QtGui import QPixmap

instagramUI = r'C:\Users\스타트코딩\Desktop\main\python\python\GUI프로그래밍\03_PYQT5_인스타그램.ui'

# 로그인 작업할 스레드
class SeleniumWork(QObject):
    login_progress_signal = pyqtSignal(int) # 데이터를 같이 담아 보낼 때 
    login_success_signal = pyqtSignal(bool)
    search_progress_signal = pyqtSignal(int)
    search_success_signal = pyqtSignal(bool)
    image_signal = pyqtSignal(str)
    content_signal = pyqtSignal(str)
    def __init__(self):
        QObject.__init__(self, None)
        self.driver = webdriver.Chrome("C:/chromedriver")
        self.input_id = ""
        self.input_pw = ""
        self.input_keyword = ""

    def login(self):
        self.login_progress_signal.emit(10)
        LOGIN_URL = "https://www.instagram.com/accounts/login/?hl=ko"
        self.driver.get(LOGIN_URL)
        self.driver.implicitly_wait(3)
        self.login_progress_signal.emit(20)
        self.driver.find_element_by_name("username").send_keys(self.input_id)
        time.sleep(1)
        self.login_progress_signal.emit(40)
        self.driver.find_element_by_name("password").send_keys(self.input_pw)
        time.sleep(1)
        self.login_progress_signal.emit(60)
        self.driver.find_element_by_css_selector("div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB").click()
        time.sleep(3)
        self.login_progress_signal.emit(100)
        # 로그인에 성공했다면
        if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F&hl=ko":
            self.login_success_signal.emit(True)
        else:
            self.login_success_signal.emit(False)

    def search(self):
        self.search_progress_signal.emit(10)
        TAG_URL = f"https://www.instagram.com/explore/tags/{self.input_keyword}/?hl=ko"
        self.driver.get(TAG_URL)
        self.search_progress_signal.emit(40)
        time.sleep(4)
        self.search_progress_signal.emit(70)
        first_post = self.driver.find_element_by_css_selector(".v1Nh3.kIKUG._bz0w > a")
        first_post.click()
        time.sleep(2)
        self.search_progress_signal.emit(100)
        self.search_success_signal.emit(True)
        while True:
            time.sleep(2)
            # 좋아요버튼
            self.driver.find_element_by_css_selector("span.fr66n > button.wpO6b").click()
            time.sleep(random.randint(1,3))
            nick_name = self.driver.find_element_by_css_selector("a.sqdOP.yWX7d._8A5w5.ZIAjV")
            content = self.driver.find_element_by_css_selector("div.C4VMK > span").text
            # 비디오 태그로 되어 있는 경우가 있음. 
            try:
                img = self.driver.find_element_by_css_selector("article.M9sTE.L_LMM.JyscU.ePUX4 div.KL4Bh > img.FFVAD")
                img_url = img.get_attribute('src')
            except:
                img = self.driver.find_element_by_css_selector("video.tWeCl")
                img_url = img.get_attribute('poster')
            # 크롤링 결과 신호 보내기
            print(img_url)
            self.image_signal.emit(img_url)
            self.content_signal.emit(content)
            try:
                self.driver.find_element_by_css_selector("a._65Bje.coreSpriteRightPaginationArrow").click()
            except:
                print("마지막 포스팅입니다...")
                print("작업완료")
                break

class MainDialog(QDialog):
    # 신호 만들기
    login_signal = pyqtSignal()
    search_signal = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(instagramUI, self)
        self.login_progressbar.setValue(0)
        self.search_progressbar.setValue(0)
        self.search_button.setEnabled(False)

        # 쓰레드에 worker를 옮김
        self.worker = SeleniumWork() # 작업자 만들기
        self.thread = QThread() # 작업공간 만들기
        self.worker.moveToThread(self.thread) # 작업자 작업공간에 배치
        self.thread.start() # 작업 시작
        
        # 로그인 버튼
        self.login_button.clicked.connect(self.LoginButtonClicked) # 버튼을 눌렀을 때 showString 함수를 호출해라
        
        # 로그인 신호 연결
        self.login_signal.connect(self.worker.login)
        self.worker.login_progress_signal.connect(self.login_progressbar.setValue) # emit 데이터는 setValue에 인자로 들어간다.
        self.worker.login_success_signal.connect(self.finish_login)

        # 검색 버튼
        self.search_button.clicked.connect(self.SearchButtonClicked)

        # 검색 신호 연결
        self.search_signal.connect(self.worker.search)
        self.worker.search_progress_signal.connect(self.search_progressbar.setValue)
        self.worker.search_success_signal.connect(self.finish_search)


        # 크롤링 결과 신호 연결
        self.worker.image_signal.connect(self.ShowImage)
        self.worker.content_signal.connect(self.ShowContent)

    def ShowImage(self, img_url):
        print(img_url)
        data = req.urlopen(img_url).read()
        print(data)
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        pixmap = pixmap.scaled(300,300) # 이미지 resizing
        self.img_label.setPixmap(pixmap)

    def ShowContent(self, content):
        self.content_label.clear() # 지우기
        self.content_label.append(content) # 텍스트 브라우저에는 setText 가 없다. append는 추가모드

    def finish_search(self, data):
        if data == True:
            self.search_status.setText("검색 완료! 좋아요 작업 중..")

    def SearchButtonClicked(self):
        self.search_status.setText("검색 중...")
        self.search_button.setEnabled(False) # 검색 버튼 비활성화
        keyword = self.input_search.text()
        self.worker.input_keyword = keyword
        self.search_signal.emit()

    def finish_login(self, data):
        if data == True:
            self.login_status.setText("로그인 성공!")
            self.search_button.setEnabled(True)
        else:
            self.login_status.setText("로그인 실패!")
            self.login_button.setEnabled(True) # 로그인 버튼 비활성화

    def LoginButtonClicked(self):
        self.login_status.setText("로그인 중...")    
        self.login_button.setEnabled(False) # 로그인 버튼 비활성화
        user_id = self.input_id.text()
        user_pw = self.input_pw.text()
        self.worker.input_id = user_id
        self.worker.input_pw = user_pw
        self.login_signal.emit() # 신호 발생시키기
        
QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())