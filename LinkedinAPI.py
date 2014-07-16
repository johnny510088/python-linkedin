#!/usr/bin/env python
from linkedin import linkedin
application = linkedin.LinkedInApplication(token="AQWfZmj7eHDppV7llZUm2tuKhoLYIX3Jkm3lgegjt7kqGIW0DNvYkzsw9Y08XydQHTHSkJCGK-vKuQNS8DAEAwRRhjwIuWHf0jgTMle7aEw-lSP6-v6x1tm2xkqDNljcnC0QKlQWoAoyLNCXl06R9rGpBtVkVDOL8nbDFa8ZW4xvOqTtiag")
#Get the data now!!

print("------------------Get profile by id------------------")
print("%s" % application.get_profile(member_id='tJ0koKfP1L'))

print("------------------Get profile by Basic selectors------------------")
print("%s" % application.get_profile(member_id='tJ0koKfP1L',selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations']))	

print("------------------Get profile by network selectors------------------")
print("%s" % application.get_profile(member_id='tJ0koKfP1L',selectors=['network']))	

print("------------------Get Connections------------------")
print("%s" % application.get_connections())
