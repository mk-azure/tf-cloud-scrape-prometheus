#!/usr/bin/env python 

import urllib2
import json

auth_token = '<auth token>'
ORG = "<ORG Name>"
WS = "<Workspace Name>"
WS_ID = "<Workspace ID>"

def get_response_json_object(url, auth_token):
    '''
      returns json object with info
    '''
    #auth_token=get_auth_token()
    req=urllib2.Request(url, None, {"Authorization": "Bearer %s" %auth_token})
    response=urllib2.urlopen(req)
    html=response.read()
    json_obj=json.loads(html)
    return json_obj


url = 'https://app.terraform.io/api/v2/account/details' 
response = get_response_json_object(url, auth_token)
print "JSON Pretty Print Output - ACCOUNT" 
print json.dumps(response, indent=2) 
print "\n"

url = 'https://app.terraform.io/api/v2/organizations' 
response = get_response_json_object(url, auth_token)
print "JSON Pretty Print Output - ORGANISATIONS"
print json.dumps(response, indent=2)
print "\n"

url = 'https://app.terraform.io/api/v2/organizations/' + ORG + '/workspaces'
response = get_response_json_object(url, auth_token)
print "JSON Pretty Print Output - WORKSPACES"
print json.dumps(response, indent=2)

url = 'https://app.terraform.io/api/v2/organizations/' + ORG + '/workspaces/' + WS
response = get_response_json_object(url, auth_token)
print "JSON Pretty Print Output - WORKSPACES"
print json.dumps(response, indent=2)
