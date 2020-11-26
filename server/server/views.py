import os
import time
import json
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()


def hello(request):
    return JsonResponse({'response_text':'hello world!'})


def lights(request, color, brightness):
    print("moi " + color)
    print("jo " + brightness)
    payload = '{ "3311": [{ "5850": 1, "5706": "%s", "5851": %s }] }' % (color, brightness)
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"' .format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": color, "brightness": brightness})


def lightsXY(request, xColor, yColor, brightness):
    payload = '{ "3311": [{ "5850": 1, "5709": %s, "5710": %s, "5851": %s }] }' % (xColor, yColor, brightness)
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"' .format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "XY-Color", "brightness": brightness})


def lighton(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "f5faf6" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"' .format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "f5faf6"})


def lightoff(request):
    payload = '{ "3311": [{ "5850": 0 }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "0", "color": "f5faf6"})


def red(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "dc4b31" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "dc4b31"})


def green(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "a9d62b" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "a9d62b"})


def blue(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "4a418a" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "4a418a"})


def yellow(request):
    payload = '{ "3311": [{ "5850": 1, "5706": "d6e44b" }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "d6e44b"})


def janne(request):
    payload = '{ "3311": [{ "5850": 1, "5709": 45971, "5710": 37842 }] }'
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))

    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "color": "XY-Color"})


def brightness(request, br):
    corbr = (int(br) * 254 / 100)
    print("kirkkaus: " + br + " == " + str(corbr))
    payload = '{ "3311": [{ "5850": 1, "5851": %s }] }' % int(corbr)
    api = 'coap-client -m put -u "{}" -k "{}" -e \'{}\' "coaps://{}:5684/15001/65536"'.format(
        os.getenv('LIGHT_USER'), os.getenv('LIGHT_PASSWORD'), payload, os.getenv('GW_IP'))
    
    result = os.popen(api)
    print(result.read())

    return JsonResponse({"power": "1", "brightness": int(corbr)})
