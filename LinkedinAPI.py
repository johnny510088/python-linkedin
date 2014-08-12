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

#Path to store the files
path="/home/johnny/Documents/linkedin/johnny/"
#Global Three Main Variable
allID_list = []
afterProgressID_list = []
allID_dict = dict()
#Tmp Variable
traverseID_list = []

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

def printDict(d, indent):
	for key, value in d.iteritems():
		print '\t' * indent + str(key)
		if isinstance(value, dict):
			printDict(value, indent+1)
		else:
			print '\t' * (indent+1) + str(value)

def printDictToFile(d, indent,f):
	for key, value in d.iteritems():
		f.write('\t' * indent + str(key))
		if isinstance(value, dict):
			printDictToFile(value, indent+1)
		else:
			f.write( '\t' * (indent+1) + str(value))

#Traverse the whole Dictionary and get the value's whose key is equal to "id"
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
				if isinstance(v,unicode):#user id's type are 'unicode' not 'int' and with len = 10
					if len(v) == 10:
						IsRepeat = "FALSE"
						for index in range(len(traverseID_list)):
							if traverseID_list[index] == v:#If already have an ID in list, we don't have to add it. 
								IsRepeat = "TRUE"
								break
						if IsRepeat == "FALSE":
							traverseID_list.append(v)
	return traverseID_list #Return the id list after traverseID

#Remove the ID which have already in the allID_list
def removeRedundantID(traverseID_list,allID_list):
	tmp_list=[]
	for index in range(len(traverseID_list)):
		for index2 in range(len(allID_list)):
			if traverseID_list[index] == allID_list[index2]:
				tmp_list.append(traverseID_list[index])			
	for	index in range(len(tmp_list)):
		traverseID_list.remove(tmp_list[index])
	return traverseID_list

#Return the path(type = list) of specific "key" from the dictionary 
def findKeyPath(d,key):
	for k,v in d.items():
		if isinstance(v,type(None)):
			if k == key:
				return [k]
		else:
			p = findKeyPath(v,key)
			if p:
				return [k] + p

#Set the Value in the Dictionary by mapList
def setInDict(dataDict, mapList, value):
	getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

#Get the Value in the Dictionary by mapList 
def getFromDict(dataDict, mapList):
	return reduce(lambda d, k: d[k], mapList, dataDict)


#Main Recursively function
def findRecursively( target_member_id , afterProgressID_list , allID_list , allID_dict , count):
	print "[TEST CODE]In findRecursively funx , target_member_id = ",target_member_id
	count = count -1
	afterProgressID_list.append(target_member_id)# Add "target member id" in orders
	try:
		writeFile(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])))
		try:
			#Read the file and transfer "python object" type into "dictionary" type
			file_content = readFile(target_member_id)
			jsonDict = ast.literal_eval(file_content)
			
			#Get friends' ID and do the Recursively  
			traverseID_list = []
			traverseID_list = traverseDictGetAllID(jsonDict,traverseID_list)#Get "New ID list" from the current "target member ID"
			traverseID_list = removeRedundantID(traverseID_list,allID_list)#Remove the IDs which have already been progressed
		
			IDPathInDict = findKeyPath(allID_dict,target_member_id)
			if len(traverseID_list)==0:
				setInDict(allID_dict,IDPathInDict,"No more ID list")
			else:	
				#The ID in the traverseID_list will be progressed in the future! Update the list and dictionary
				tmp_dict = dict()
				tmp_dict = tmp_dict.fromkeys(traverseID_list)		
				setInDict(allID_dict, IDPathInDict, tmp_dict)#Insert tmp_dict into allID_dict by the path od ID
				allID_list = allID_list + traverseID_list #Concatenate the list
			


			#Get the next ID from target member ID
			if count >= 0 : #Can call the API
				if isinstance(getFromDict(allID_list, IDPathInDict),dict):
					#Get the first element in the dictionary
					findRecursively( getFromDict(allID_list, IDPathInDict).keys()[0] , afterProgressID_list , allID_list , allID_dict , count)
				else:
					print "here"
					#Get the next element in the dictionary
					
			else : #Can't call the API ,Print (1)allID_list (2)allID_dict (3)afterProgressID_list
				print "At the End of the program, All ID list = %d / after process ID list = %d" % (len(allID_list),len(afterProgressID_list))
				fw = open('allID_dict.txt','w')
				printDictToFile(allID_dict,0,fw)
				fw.close()
		except (ValueError, KeyError, TypeError) as error:
			print "At the Inter Exception , member id = ",target_member_id
			print "Error : ",error
	except Exception as error:
		print "At the Outer Exception , member id = ",target_member_id
		print "Error :",error
	return allID_list

print "In the first of program"
#Start from my own profile
writeFile(member_id, str(application.get_profile(selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])))
file_content = readFile(member_id)
jsonDict = ast.literal_eval(file_content)

traverseID_list = traverseDictGetAllID(jsonDict,traverseID_list)
traverseID_list = removeRedundantID(traverseID_list,allID_list)#Remove the IDs which have already been progressed
print "[TEST Code]The return value = ",traverseID_list

#The ID in the traverseID_list will be progressed in the future! Update the list and dictionary
tmp_dict = dict()
tmp_dict = tmp_dict.fromkeys(traverseID_list)		
allID_dict[member_id]=tmp_dict
allID_list = allID_list + traverseID_list #Concatenate the list
print "------------------------------- allID_dict --------------------------------"
printDict(allID_dict,0)
#findRecursively( allID_dict[member_id].keys()[0] , afterProgressID_list , allID_list , allID_dict , 0)
	
