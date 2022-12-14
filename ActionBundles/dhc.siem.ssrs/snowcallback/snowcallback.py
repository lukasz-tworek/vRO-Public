import json
import requests

def handler(context, inputs):

    callbackId = inputs["callbackId"]
    baseUrl = inputs["runbookEndpoint"]
    reqStatus = inputs["requestStatus"]
    serialNo = inputs["serialNumber"]
    userSnow = inputs["user"]
    pwdSnow = inputs["pwd"]
    errorCode = inputs["errorCode"]
    errorMsg = inputs["errorMsg"]
    if (callbackId.find("RITM") >= 0):
        ritmSplit = callbackId.split("RITM")[1]
        ritm = "RITM" + ritmSplit
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    myobj = {"u_callback_instance_id": callbackId, "u_request_item": ritm, "u_status": reqStatus, "u_result": serialNo, "u_resultmessage": "Request sent from vRA using vRO workflow", "u_errorcode": errorCode, "u_errormessage": errorMsg}
    print("Body content: " + str(myobj)) 
    #Execute POST request using variables
    response = requests.post(baseUrl, auth=(userSnow, pwdSnow), headers = headers, data = str(myobj))
    jsonResponse = response.json()
    print('Runbook output: ' + str(jsonResponse))
    return str(jsonResponse)