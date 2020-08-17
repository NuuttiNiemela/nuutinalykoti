import os
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()


def hello(request):
    return JsonResponse({'response_text':'hello world!'})


def lighton(request):
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{ "3311": [{ "5850": 1 }] }\' "coaps://{}:5684/15001/65536"' .format(
        os.getenv('USER'), os.getenv('LIGHT_PASSWORD'), os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response': result})


def lightoff(request):
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{ "3311": [{ "5850": 0 }] }\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('USER'), os.getenv('LIGHT_PASSWORD'), os.getenv('GW_IP'))
    
    result = os.popen(api)
    
    return JsonResponse({'response': result})
