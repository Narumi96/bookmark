import InputForm
'''
Created on 2023/07/27

@author: MD23006
'''
class TriplusData():
    def __init__(self):
        self.bookmark = None
    '''
    画面操作のイベントはここに入れる
    '''
    def setBookmark(self,bookmark):
        self.bookmark = bookmark

class GenerateData(TriplusData):
    def __init__(self):
        self.question = {"現在地" :'広島',
                         "行先"   :'東京',
                         "日数"   :'3日間',
                         "目的"   :'旅行に行きたいです',
                         "予算"   :'1000円'}
        self.send_text = None
    
    def setQuestion(self,key,text):
        self.question[key] = text
        
    def generateSendText(self):
        self.send_text = '以下の文章をもとに詳細な旅行のプランを計画して，その日程と時刻を1000文字以内でまとめた文章の情報を抽出して，以下のフォーマットに従いJSONとして出力せよ\n'+\
        '\n## 文章\n'+self.question["現在地"]+"から"+self.question["行先"]+"まで"+self.question["日数"]+self.question["目的"]+"."+\
        "予算は"+self.question["予算"]+'で考えています.この条件で旅行を計画してください．'+\
        '\n\n## フォーマット\n[\n\t{"activity":アクティビティ,"datetime":YYYY-MM-DD HH:MM:SS}\n]\n'
    
    def getSendText(self):
        #print(self.send_text)
        return self.send_text
        