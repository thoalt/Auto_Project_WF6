import time
from requests.auth import HTTPBasicAuth
import requests
import json
import sys
automationID = sys.argv[1]
print(automationID)
postExe = "http://localhost:8080/rest/zapi/latest/automation/job/execute/" + str(automationID)
getStatus = "http://localhost:8080/rest/zapi/latest/automation/job/status/" + str(automationID)
auth = HTTPBasicAuth('thoalt', 'A@1and1is3')
res = requests.post(postExe, auth=auth)

res_dict = json.loads(res.text)
print(res_dict)
# # time.sleep(5)
# # y = requests.get(getStatus)
#
# print(y)