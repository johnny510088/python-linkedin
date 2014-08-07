#!/usr/bin/env python
from linkedin import linkedin
import os
import json
import ast

#Johnny Chan
application = linkedin.LinkedInApplication(token="AQVlc_gHTXwZVasIJRIgLG6hWefpOkG0HPVW8K7G2pqzyal4uEPGP4UF_7R8VPQVTPRiFw5XAO2NfcL3_UkzAn7Wfn1ybsK9Hh5FQ5YZP0nwww3mt_ew00b8pmvpHYrUOoHxiWqaUWG_KYlfdOThtHebQK_qtNrQEKNLKqAurObQwl4qrHE")
member_id='yp7a3L09d2'#Johnny Chan
#member_id='snwLFsJSK1'
#member_id='tJ0koKfP1L'

#Edith Torres 
#application = linkedin.LinkedInApplication(token="AQXqwtUO9-JwJTq6821zNPAIFvAjg3_pqHyOjp9hFYpbRx9aP1MIyxV_VyAxBt_T-LO840381ZIA3Aysxx7vvb7o5QO3_1w8VQbea_wrBmrQaJ7W3_DPC9Xi41X03464B87XMMDhdYaiuF6vV0M8KaHj_WzW6owpaozfClbMAxkzGAjjYSw")
#member_id='4CoXkm47Fi'#Edith Torres
#member_id='mZY4xXt8EZ'
#member_id='dJgVi_-eG6'

path="/home/johnny/Documents/linkedin/johnny/"
traverseID_list = []
allID_list = []

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

def traverseDictGetAllID(d,traverseID_list):
	for k, v in d.iteritems():
		if isinstance(v, dict):#if type(v)=dict
			traverseID_list=traverseDictGetAllID(v,traverseID_list)
		elif isinstance(v,list):#If type(v)=list
			for index in range(len(v)):
				if isinstance(v[index],dict):
					traverseID_list=traverseDictGetAllID(v[index],traverseID_list)
		else:
			if k == unicode("id") :
				if isinstance(v,unicode):#user id's type are 'unicode' not 'int' and     with len = 10
					if len(v) == 10:
						IsRepeat = "FALSE"
						for index in range(len(traverseID_list)):
							if traverseID_list[index] == v:#If already have an ID in     list, we don't have to add it. 
								IsRepeat = "TRUE"
								break
						if IsRepeat == "FALSE":
							traverseID_list.append(v)
#print "{0} : {1}".format(k, v)
	return traverseID_list


def findRecursively(target_member_id,allID_list):
	print "In findRecursively funx , target_member_id = ",target_member_id
	try:
		writeFile(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])))
		try:
			#Read the file and transfer "python object" type into "dictionary" type
			file_content = readFile(target_member_id)
			jsonDict = ast.literal_eval(file_content)
			#Write myself profile into .csv
			
			#Get friends' ID and do the Recursively  
			traverseID_list = []
			traverseID_list = traverseDictGetAllID(jsonDict,traverseID_list)
			
			for index in range(len(traverseID_list)):
				IsRepeat="FALSE"
				for index2 in range(len(allID_list)):
					if traverseID_list[index] == allID_list[index2]:
						IsRepeat="TRUE"
						break
				if IsRepeat == "FALSE":
					allID_list.append(traverseID_list[index])
					for i in range(len(allID_list)):
						print "allIDlist[%d] = %s" % (i,allID_list[i])
					allID_list=findRecursively(traverseID_list[index],allID_list)
			
				
			#If there new ID and store into allID_list
			"""
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
							IsRepeat = "TRUE"
							break
 				if IsRepeat == "FALSE":
						ID_list.append(jsonDict['network']['updates']['values'][i]['updateContent']['person']['id'])
						findRecursively(jsonDict['network']['updates']['values'][i]['updateContent']['person']['id'])
			#(2)Get ID from <relationToViewer> <connections> <values> <person> <id>
			IsRepeat = "FALSE"
			for i in range(jsonDict['relationToViewer']['connections']['_total']):
				if jsonDict['relationToViewer']['connections']['values'][i]['person']['id']!="private":
					for index in range(len(ID_list)):
						if ID_list[index] == jsonDict['relationToViewer']['connections']['values'][i]['person']['id']:
							IsRepeat = "TRUE"
							break
					if IsRepeat == "FALSE":
						ID_list.append(jsonDict['relationToViewer']['connections']['values'][i]['person']['id'])
						findRecursively(jsonDict['relationToViewer']['connections']['values'][i]['person']['id'])
			"""


#			print "Network count = jsonDict['network']['updates']['_count']"
#			print "Network 0 = ",jsonDict['network']['updates']['values'][0]['updateContent']['person']['id']
#			print "Network 1 = ",jsonDict['network']['updates']['values'][1]['updateContent']['person']['id']
			
			

		except (ValueError, KeyError, TypeError) as error:
			print "At the Inter Exception , member id = ",target_member_id
			print "Error : ",error
	except Exception as error: #Don't do any thing here
		print "At the Outer Exception , member id = ",target_member_id
		print "Error :",error
	return allID_list


#Start from my own profile
writeFile(member_id, str(application.get_profile(selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])))
file_content = readFile(member_id)
jsonDict = ast.literal_eval(file_content)
traverseID_list=traverseDictGetAllID(jsonDict,traverseID_list)
print "The return value = ",traverseID_list

for index in range(len(traverseID_list)):
	IsRepeat="FALSE"
	for index2 in range(len(allID_list)):
		if traverseID_list[index] == allID_list[index2]:
			IsRepeat="TRUE"
			break
	if IsRepeat == "FALSE":
		allID_list.append(traverseID_list[index])
		allID_list=findRecursively(traverseID_list[index],allID_list)

print "At the End of the program, total number of ID = ",len(allID_list)





#print("------------------Get profile by Basic selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations']))	
#print("------------------Get profile by All selectors------------------")
#print("%s" % application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks']))
#writeFileWithCheck(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer'])))

