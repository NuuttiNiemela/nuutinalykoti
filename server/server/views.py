import os
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()


def hello(request):
    return JsonResponse({'response_text':'hello world!'})


def lighton(request):
    payload = '{ "3311": [{ "5850": 1 }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"' .format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})


def lightoff(request):
    payload = '{ "3311": [{ "5850": 0 }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})