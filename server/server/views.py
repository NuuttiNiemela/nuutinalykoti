import os
import time
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()


def hello(request):
    return JsonResponse({'response_text':'hello world!'})


@csrf_exempt
def lighton(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "f5faf6" }] }'
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


def red(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "dc4b31" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})


def green(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "a9d62b" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})


def blue(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "4a418a" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})


def yellow(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "d6e44b" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})


def janne(request):
    payload = '{ "3311": [{ "5850": 1, "5709": 45971, "5710": 37842 }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)

    return JsonResponse({'response_text': result})


def disco(request):
    result = discotime(1, 65500)
    result = discotime(10000, 55500)
    result = discotime(20000, 45500)
    result = discotime(30000, 35500)
    result = discotime(40000, 25500)
    result = discotime(50000, 15500)
    result = discotime(60000, 5500)
    result = discotime(65500, 1500)
    
    return JsonResponse({'response_text': result})


def discotime(first, second):
    first = first
    second = second
    payload = '{ "3311": [{ "5709": {}, "5710": {} }] }'.format(first, second)
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))
    
    result = os.popen(api)
    print(result)
    time.sleep(1)
    
    return result
