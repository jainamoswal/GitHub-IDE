import os
import requests
import json
import sys
import traceback
import io

with open(os.getenv('GITHUB_EVENT_PATH'), 'r') as jsonfile:
  raw_data = json.load(jsonfile)

cmd = raw_data['comment']['body']
ocmd = "".join(f"{l}\n" for l in cmd.split("\n"))

admins = []
for each in raw_data['issue']['assignees']:
    admins.append(each['login'])

old_stderr = sys.stderr
old_stdout = sys.stdout
redirected_output = sys.stdout = io.StringIO()
redirected_error = sys.stderr = io.StringIO()
stdout, stderr, exc = None, None, None

url = raw_data['issue']['comments_url']
token = os.getenv('token')

whoareyou = raw_data['sender']['login']

if whoareyou in admins:
    try:
        exec(ocmd)
    except Exception as e:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    if exc:
        evaluation = f"```\n{exc}```"
    elif stderr:
        evaluation = f"```\n{stderr}```"
    elif stdout:
        evaluation = f"```\n{stdout}```"
    else:
        evaluation = "**Success**"
    final_output = "**▩ Command ▩**\n{}\n --- \n**▧ Output ▨**\n{}\n".format(f"```\n{ocmd}```", evaluation)

else:
    final_output = f'**@{whoareyou}** _you are not allowed to access the IDE, for gaining access. ask admins to assign you._'
    
final_output = final_output + f"> _**This is reply to [this]({raw_data['comment']['html_url']}) comment.**_"
data = {"body": final_output}
headers = {'Authorization': f'token {token}'}
requests.post(url, data=json.dumps(data), headers=headers)
