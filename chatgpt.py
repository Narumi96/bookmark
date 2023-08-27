import openai
import pandas as pd
import sys
import json
import CallDatabase
#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
openai.api_key = "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"
def gpt(msg):
    messages = []
    total_tokens = 0 #トークン総消費量

    usr_msg = {'role': 'user', 'content': msg}

    messages.append(usr_msg)

    response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo',
                    messages=messages,
                    temperature=1.0,#低いと厳密になる
    )#chatGPTの返答

    print('\n' + 'ChatGPT: ' + response['choices'][0]['message']['content'] + '\n')
    
    ans = json.loads(response['choices'][0]['message']['content'])
    print(type(ans))
    
    CallDatabase.CallingData(ans)

    #messagesにChatGPT側の返答内容を追加
    messages.append({'role': response['choices'][0]['message']['role'], 
                    'content': response['choices'][0]['message']['content']})
    
    total_tokens += int(response['usage']['total_tokens'])

    return
    
#if __name__ == '__main__':
#    gpt('以下の文章をもとに詳細な旅行のプランを日程と時刻ごとにまとめた文章の情報を抽出して，日時をdatetimeをに入れて，内容をscheduleにいれてJSONとして出力せよ\n\n## 文章\n広島から東京まで3日間旅行に行きたい.予算は100000円で考えています.\n')