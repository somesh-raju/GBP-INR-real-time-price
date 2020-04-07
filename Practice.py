import json
import urllib
from urllib.request import urlopen
import time
import smtplib

# send mail script
'''sender = "somesh.d84@gmail.com"
receivers = ["somesh.d84@gmail.com"]

gmail_uname = 'somesh.d84@gmail.com'
gmail_pwd = 'pwd'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_uname, gmail_pwd)

server.sendmail(sender, receivers, " TEST MAIL")
server.quit()'''

while True:
    try:
        with urlopen("https://fcsapi.com/api/forex/latest?symbol=GBP/INR,INR/GBP"
                         "&period=1h&access_key=S6zMsyRzQxNH8pXPMB2bkpjftjmJZukFZ3MBH0uF5Yb9srEJd3") as response:
            data = response.read()
    except TimeoutError as e:
        print("Timeout error happened - ", e)
    except urllib.error.URLerror as u:
        print("URL error - ", u)
    json_data = json.loads(data.decode('utf-8'))
    #print(json_data['response'][0]['price'])
    #print(json.dumps(json_data, indent=2))

    #print(float(json_data['response'][1]['change']))
    change = float(json_data['response'][1]['change'])
    if change > 1.0:
        print("Change more than 1 -> ", change)
    elif str(change).startswith("+"):
        print("Change +ve -> ", change)
    print("GBP/INR -> ", json_data['response'][0]['price'])
    print("Change (INR/GBP) -> ", change)
    print("Server Time -> ", json_data['info']['server_time'])
    time.sleep(60)

#print(type(json_data))
#print(json.dumps(json_data, indent=2))
#print(json_data['rates'])
#print(json_data['response'][0]['price'])
