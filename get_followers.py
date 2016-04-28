import httplib
import urllib
import sys

username = sys.argv[1]

if len(sys.argv) > 2:
  page = sys.argv[2]
else:
  page = 0


conn = httplib.HTTPSConnection("medium.com")
headers = {"Accept": "application/json"}
params = urllib.urlencode({"listType": "followers", "page": page})
conn.request("GET", "/@{}/follow-list".format(username), params, headers)
res = conn.getresponse()

body = res.read()
split_payload = body.split("])}while(1);</x>")[1]
print split_payload
