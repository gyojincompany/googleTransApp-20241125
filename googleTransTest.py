import googletrans

# print(googletrans.LANGUAGES)  # -> 각 언어의 약자 출력(dest 값)
# 영어 en, 일본어 ja, 중국어 zh-cn

trans = googletrans.Translator()  # 구글 번역기 객체 생성

resultEng = trans.translate("안녕하세요", dest="en")  # 영어로 번역
resultJa = trans.translate("안녕하세요", dest="ja")  # 일본어로 번역
resultCn = trans.translate("안녕하세요", dest="zh-cn")  # 중국어로 번역

print(f"영어 : {resultEng.text}")
print(f"일본어 : {resultJa.text}")
print(f"중국어 : {resultCn.text}")



