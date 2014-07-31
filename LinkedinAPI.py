#!/usr/bin/env python
from linkedin import linkedin
import os

application = linkedin.LinkedInApplication(token="AQWfZmj7eHDppV7llZUm2tuKhoLYIX3Jkm3lgegjt7kqGIW0DNvYkzsw9Y08XydQHTHSkJCGK-vKuQNS8DAEAwRRhjwIuWHf0jgTMle7aEw-lSP6-v6x1tm2xkqDNljcnC0QKlQWoAoyLNCXl06R9rGpBtVkVDOL8nbDFa8ZW4xvOqTtiag")
#Get the data now!!

target_member_id='tJ0koKfP1L'
path="/home/johnny/Documents/tmp/"
def storeFile(member_id,content):
	if os.path.isfile(path+member_id+'.txt'):
		print("Already have the file")
	else:
		f=open(path+member_id+'.txt','w')
		f.write(content)
		f.close()


def storeFileForce(member_id,content):
	f=open(path+member_id+'.txt','w')
	f.write(content)
	f.close()

#print("------------------Get profile by Basic selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations']))	
#print("------------------Get profile by network selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['network']))	
print("------------------Get Connections------------------")
print("%s" % application.get_connections())
#print("------------------Get profile by All selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks']))
storeFileForce(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])))
