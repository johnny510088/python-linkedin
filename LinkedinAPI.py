#!/usr/bin/env python
from linkedin import linkedin

API_KEY = '{Please input api key}'
API_SECRET = '{Please input api secret}'
REDIRECT_URL = '{Please input redirect url}'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, REDIRECT_URL,linkedin.PERMISSIONS.enums.values())
print("Check the URL on browser and retun the \'authorization code\' \n%s"% authentication.authorization_url )
authorizationCode = raw_input('Pleace input authorization_code:\n')
authentication.authorization_code=authorizationCode

application = linkedin.LinkedInApplication(authentication)
application = linkedin.LinkedInApplication(token=authentication.get_access_token())

target_member_id = '{Please input the ID}'
print("------------------Get profile by member id------------------")
print("%s" % application.get_profile(member_id=target_member_id))

print("------------------Get profile by member id with selectors------------------")
print("%s" %application.get_profile(member_id=target_member_id,selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections']))
