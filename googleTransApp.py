import googletrans
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # QT Designer에서 만든 ui를 불러오는 모듈
from PyQt5.QtCore import Qt

from os import environ
import multiprocessing as mp

form_class = uic.loadUiType("ui/googletrans.ui")[0]
# QT Designer에서 만든 외부 ui 불러오기

class GoogleTransApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모 클래스의 생성자 호출
        self.setupUi(self)  # 불러온 ui 파일을 연결

        self.setWindowTitle("구글 한줄 번역기")  # 윈도우 제목 설정
        self.setWindowIcon(QIcon("ui/google.png"))  # 윈도우 아이콘 설정
        self.statusBar().showMessage("구글 번역기 v1.0")  # 윈도우 상태 표시줄 설정
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 항상위에 옵션

        # 버튼 클릭 이벤트 처리
        self.trans_btn.clicked.connect(self.trans_execute)
        # trans_btn 버튼이 실행되면 호출될 메소드를 지정
        self.input_reset_btn.clicked.connect(self.remove_input_edit)  # 입력 초기화 버튼 클릭 이벤트 처리
        self.all_reset_btn.clicked.connect(self.remove_all_edit)  # 모든 에디트 초기화 버튼 클릭 이벤트 처리

        self.trans = googletrans.Translator()

    def trans_execute(self):  # 번역 실행 메소드
        # print("번역실행 버튼이 클릭되었습니다!!")
        kor_input_text = self.kor_input_edit.text()  # 해당 line edit 에 입력된 텍스트 가져오기

        if kor_input_text == "":  # 입력된 내용이 공백인지 확인
            QMessageBox.warning(self, "입력오류!","한글입력란에 반드시\n문장을 넣어주세요.")
        else:
            # trans = googletrans.Translator()  # 구글 번역 객체 생성

            resultEng = self.trans.translate(kor_input_text, dest="en")
            resultJap = self.trans.translate(kor_input_text, dest="en")
            resultChn = self.trans.translate(kor_input_text, dest="en")
            # resultEng = trans.translate(kor_input_text, dest="en")  # 영어 번역 결과
            # resultJap = trans.translate(kor_input_text, dest="ja")  # 일본어 번역 결과
            # resultChn = trans.translate(kor_input_text, dest="zh-cn")  # 중국어 번역 결과

            self.eng_output_edit.append(resultEng.text)  # 영어 출력
            self.jap_output_edit.append(resultJap.text)  # 일본어 출력
            self.chn_output_edit.append(resultChn.text)  # 중국어 출력

    def remove_input_edit(self):  # 입력 에디트 초기화 메소드
        self.kor_input_edit.clear()  # 해당 라인 에디트의 내용 삭제

    def remove_all_edit(self):  # 모든 입력 출력란 초기화 메소드
        self.kor_input_edit.clear()
        self.eng_output_edit.clear()
        self.jap_output_edit.clear()
        self.chn_output_edit.clear()

def suppress_qt_warnings():  # 해상도별 글자크기 강제 고정하는 함수
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


# 해상도 고정 함수 호출
suppress_qt_warnings()
mp.freeze_support()

app = QApplication(sys.argv)
googleWin = GoogleTransApp()
googleWin.show()
sys.exit(app.exec_())