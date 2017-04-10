# pip install requests

import urllib

import requests

PhoneNumber = "91XXXXXXXXXX"

Message = "my sms"



values = {

          'PhoneNumber' : PhoneNumber,

          'Message' : Message,

          }



url = "your api end points"
#example url = "https://xxxxxxxxx.execute-api.ap-southeast-1.amazonaws.com/dev/sms"

postdata = urllib.urlencode(values)



req = requests.get(url, postdata)



print req