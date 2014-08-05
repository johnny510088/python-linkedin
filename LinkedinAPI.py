#!/usr/bin/env python
from linkedin import linkedin
import os
import json
import ast

application = linkedin.LinkedInApplication(token="AQXqwtUO9-JwJTq6821zNPAIFvAjg3_pqHyOjp9hFYpbRx9aP1MIyxV_VyAxBt_T-LO840381ZIA3Aysxx7vvb7o5QO3_1w8VQbea_wrBmrQaJ7W3_DPC9Xi41X03464B87XMMDhdYaiuF6vV0M8KaHj_WzW6owpaozfClbMAxkzGAjjYSw")

#Get the data now!!
#member_id='snwLFsJSK1'
#member_id='tJ0koKfP1L'
#member_id='9f6TJB4L4q'
member_id='mZY4xXt8EZ'
#member_id='dJgVi_-eG6'
#member_id='4CoXkm47Fi'#Edith Torres

path="/home/johnny/Documents/tmp/"
ID_list = []

#Function Definition
def writeFileWithCheck(member_id,content):
	if os.path.isfile(path+member_id+'.txt'):
		print("Already have the file")
	else:
		f=open(path+member_id+'.txt','w')
		f.write(content)
		f.close()

def writeFile(member_id,content):
	fw = open(path+member_id+'.txt','w')
	fw.write(content)
	fw.close()
	return

def readFile(member_id):
	fr = open(path+member_id+'.txt', 'r')
	tmpStr = fr.read()
	fr.close()
	return tmpStr

def findRecursively(target_member_id):
	print "In findRecursively funx , target_member_id = ",target_member_id
	try:
		writeFile(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])))
		try:
			#Read the file and transfer "python object" type into "dictionary" type
			file_content = readFile(target_member_id)
			jsonDict = ast.literal_eval(file_content)
#print "type(jsonDict) = ",type(jsonDict)
#print "target member id  = " ,target_member_id
			#Write myself profile into .csv
			#Get friends' ID and do the Recursively  
			#(1)Get ID from <network> <updates> <values> <#> <updateContent> <person> <id>
			IsRepeat = "FALSE"
			for i in range(jsonDict['network']['updates']['_count']):
				if jsonDict['network']['updates']['values'][i]['updateContent'].has_key('person') and jsonDict['network']['updates']['values'][i]['updateContent']['person']['id']!="private":
					print "-------------ID_list disctionary-----------"
					for index in range(len(ID_list)):
						print "ID_list[%d] = %s " % (index ,ID_list[index])
					print "-------------------------------------------"
					for index in range(len(ID_list)):
						if ID_list[index] == jsonDict['network']['updates']['values'][i]['updateContent']['person']['id']:
							print "In the if "
							IsRepeat = "TRUE"
							break
					if IsRepeat == "FALSE":
						ID_list.append(jsonDict['network']['updates']['values'][i]['updateContent']['person']['id'])
						findRecursively(jsonDict['network']['updates']['values'][i]['updateContent']['person']['id'])

			#(2)Get ID from <relationToViewer> <connections> <values> <person> <id>
			
			
#			print "Network count = jsonDict['network']['updates']['_count']"
#			print "Network 0 = ",jsonDict['network']['updates']['values'][0]['updateContent']['person']['id']
#			print "Network 1 = ",jsonDict['network']['updates']['values'][1]['updateContent']['person']['id']
			

		except (ValueError, KeyError, TypeError) as error:
			print "At the Inter Exception , member id = ",target_member_id
			print "Error : ",error
	except Exception as e: #Don't do any thing here
		print "At the Outer Exception , member id = ",target_member_id
		print "Error :",e
		return
	return

findRecursively(member_id)
print "At the End of the program"





#print("------------------Get profile by Basic selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations']))	
#print("------------------Get profile by All selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks']))
#writeFileWithCheck(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer'])))

