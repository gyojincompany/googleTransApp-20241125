import googletrans
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # QT Designer에서 만든 ui를 불러오는 모듈

form_class = uic.loadUiType("ui/googletrans.ui")[0]
# QT Designer에서 만든 외부 ui 불러오기

class GoogleTransApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출
        self.setupUi(self)  # 불러온 ui 파일을 연결

        self.setWindowTitle("구글 한줄 번역기")  # 윈도우 제목 설정
        self.setWindowIcon(QIcon("ui/google.png"))  # 윈도우 아이콘 설정
        self.statusBar().showMessage("구글 번역기 v1.0")  # 윈도우 상태 표시줄 설정



app = QApplication(sys.argv)
googleWin = GoogleTransApp()
googleWin.show()
sys.exit(app.exec_())