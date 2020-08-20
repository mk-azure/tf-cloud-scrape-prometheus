#!/bin/bash 

export TOKEN='<auth token>'
ORG="<Org Name>"
WS="<Workspace name>"

echo "ACCOUNT"
curl -s \
  --header "Authorization: Bearer $TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request GET \
  https://app.terraform.io/api/v2/account/details \
  | jq . 

echo  " " 
echo "ORGANISATIONS"
curl -s \
  --header "Authorization: Bearer $TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  --request GET \
  https://app.terraform.io/api/v2/organizations \
  | jq . 

echo  " " 
echo "WORKSPACES"
curl -s \
  --header "Authorization: Bearer $TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  https://app.terraform.io/api/v2/organizations/${ORG}/workspaces \
  | jq . 


echo  " " 
echo "WORKSPACES"
curl -s \
  --header "Authorization: Bearer $TOKEN" \
  --header "Content-Type: application/vnd.api+json" \
  https://app.terraform.io/api/v2/organizations/${ORG}/workspaces/${WS} \
  | jq . 
