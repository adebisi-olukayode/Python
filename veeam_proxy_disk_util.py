import cfg
import requests
import base64
import json

login = cfg.userv
password = cfg.passv
url = cfg.api
user_password = login + ':' + password
encoded = (base64.b64encode(user_password.encode("ascii")).decode("ascii"))
headers = {"Authorization": "Basic %s" % encoded, "Accept": "application/json"}
r = requests.post(url + '/sessionMngr/?v=latest', headers=headers)
response = r.headers
session = response['X-RestSvcSessionId']
headers = {"X-RestSvcSessionId": session, "Accept": "application/json"}
repo = requests.get(url + 'reports/summary/repository', headers=headers)
repo = repo.text
repo_dict = json.loads(repo)
repo_dict = repo_dict['Periods']
repo_list = ['Secondary', 'Primary']
for i in repo_dict:
    if i['Name'] in repo_list:
        pc_used = ((i['BackupSize']/i['Capacity']) * 100)
        percent_used = "{:.2f}".format(pc_used)
        print(i['Name'], percent_used)
