from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json


ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해주세요.'
URL_OPEN_TIME_OUT = 10
 
 
#----------------------------------------------------
# Dialogflow에서 대답 구함
#----------------------------------------------------
def get_answer(text, user_key):
    
    #--------------------------------
    # Dialogflow에 요청
    #--------------------------------
    data_send = { 
        'lang': 'ko',
        'query': text,
        'sessionId': user_key,
        'timezone': 'Asia/Seoul'
    }
    
    data_header = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer 67de79573...' # Dialogflow의 Client access token 입력
    }
    
    dialogflow_url = 'https://api.dialogflow.com/v1/query?v=20150910'
    
    res = requests.post(dialogflow_url,
                            data=json.dumps(data_send),
                            headers=data_header)

    #--------------------------------
    # 대답 처리
    #--------------------------------
    if res.status_code != requests.codes.ok:
        return ERROR_MESSAGE
    
    data_receive = res.json()
    answer = data_receive['result']['fulfillment']['speech'] 
    
    return answer


def keyboard(request):
    return JsonResponse({
       'type' : 'buttons',
       'buttons' : ['썸톡번역기','맛집 찾기','SomeTip', 'Q&A', '개발자의 한마디']
    })


@csrf_exempt
def message(request) :
    str = ((request.body).decode('utf-8'))
    return_json_str = json.loads(str)
    return_str = return_json_str['content']
    user_key = return_json_str['user_key']
    content_type = return_json_str['type']     
    
    if len(user_key) <= 0 or len(return_str) <= 0:
        speech = ERROR_MESSAGE
    elif return_str == '대화하기':
        speech = '안녕하세요! 전 피자 주문을 받는 챗봇입니다~'
    else:
        speech = get_answer(return_str, user_key)
        #speech = "hello"
    
    return JsonResponse({
        'message' : {
        'text' : speech
        },
        'keyboard' : {
            'type' : 'text' # 텍스트로 입력받기 위하여 키보드 타입을 text로 설정
        }
    })
    """
    if return_str == '썸톡번역기' :
        return JsonResponse({
             'message' : {
                 'text' : "번역할 내용을 다음과 같이 입력해 주세요.(개발중)\n ex)번역 뭐해?, 번역 안녕ㅋㅋ\n 형식을 갖추지 않으면 답변이 나오지 않습니다ㅜㅜ."
             },
             'keyboard' : {
                 'type' : 'text' # 텍스트로 입력받기 위하여 키보드 타입을 text로 설정
             }
        })
    else:
        return JsonResponse({
                'message': {
                        'text': "you type "+user_key+"!"
                },
                'keyboard': {
                        'type': 'buttons',
                        'buttons': ['1','2']
                }
        })
    
    """
