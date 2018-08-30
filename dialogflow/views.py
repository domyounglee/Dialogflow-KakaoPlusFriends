from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
 
 
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
 
