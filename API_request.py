cert_file_path = "cert.pem"
key_file_path = "key.pem"
url = "https://sandbox.api.visa.com/globalatmlocator/v1/localatms/geocodesinquiry"
###############

place = "Bengaluru"

import requests
import json
import time
import random

payload = {
   "wsRequestHeaderV2":{
      "requestTs":"2021-07-09T09:11:41.000Z",
      "requestMessageId":"ICE01-001",
      "userBid":"10000108",
      "correlationId":"909420141104053819418",
      "applicationId":"GEOCODE",
      "userId":"CDISIUserID"
   },
   "requestData":{
      "distanceUnit":"mi",
      "distance":"20",
      "options":{
         "fetchATMOwnerData":"Y",
         "findFilters":[
            {
               "filterValue":1,
               "filterName":"CHIP_ENABLED"
            },
            {
               "filterValue":"B",
               "filterName":"ACCESS_HOURS"
            }
         ],
         "range":{
            "count":99,
            "start":0
         },
         "sort":{
            "primary":"distance",
            "direction":"asc"
         },
         "useFirstAmbiguous":1
      },
      "location":{
         "placeName":place
      },
      "metaDataOptions":0
   }
}

headers = {
	'Content-Type': 'application/json',
	'Authorization': 'Basic UTlON1pTTVdZQzIxTFRXRjJHQVEyMUl6b0Fzb1lSNTBnOS1RZ2MwbTlieW81eXV2bzpCdjBqeThwM1ZyNDl5aUk0OTZCeXd6MXBNYzBUeFF3eUZ2M3lFUVc='
}

cert = (cert_file_path, key_file_path)
response = requests.request("POST", url, headers=headers, data = json.dumps(payload),cert=cert, auth=('WJYMESEHY96TT7OHQTXA212eIqY9udrJxaqki-z1FdoVOf64w', 'vj4JK614G'))

responseText=response.text.encode('utf8')
responseJSON = json.loads(responseText)

json_formatted_str = json.dumps(responseJSON, indent=4)
print(json_formatted_str)

# addr = responseJSON['responseData'][0]['MatchedLocations']
# for i in addr:
# 	print(i['Location']['Address'])


