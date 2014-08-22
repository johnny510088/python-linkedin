#!/usr/bin/env python
from linkedin import linkedin
from lxml import etree
import os
import json
import ast
import lxml
import urllib
import glob
try:
	import cPickle as pickle  
except:
	import pickle

#Johnny Chan
#application = linkedin.LinkedInApplication(token="AQVlc_gHTXwZVasIJRIgLG6hWefpOkG0HPVW8K7G2pqzyal4uEPGP4UF_7R8VPQVTPRiFw5XAO2NfcL3_UkzAn7Wfn1ybsK9Hh5FQ5YZP0nwww3mt_ew00b8pmvpHYrUOoHxiWqaUWG_KYlfdOThtHebQK_qtNrQEKNLKqAurObQwl4qrHE")
#member_id='yp7a3L09d2'#Johnny Chan
#member_id='snwLFsJSK1'
#member_id='tJ0koKfP1L'

#Edith Torres 
#application = linkedin.LinkedInApplication(token="AQXqwtUO9-JwJTq6821zNPAIFvAjg3_pqHyOjp9hFYpbRx9aP1MIyxV_VyAxBt_T-LO840381ZIA3Aysxx7vvb7o5QO3_1w8VQbea_wrBmrQaJ7W3_DPC9Xi41X03464B87XMMDhdYaiuF6vV0M8KaHj_WzW6owpaozfClbMAxkzGAjjYSw")
#member_id='4CoXkm47Fi'#Edith Torres
#member_id='mZY4xXt8EZ'
#member_id='dJgVi_-eG6'

#Alice Torres
application = linkedin.LinkedInApplication(token="AQXbmnjFvuG_VwENXDDu1k6BOFcGIAkKU3QY37RjDQkoZKqTK6iC_aq7yp7bJ376wq9fDoUrGr5BsQxcIPGnNbq-0RoHlJ1tjszmNdk4kfyBTxWH45uDMxe3-I7wnTJWEo0yySLk0jWk0y3AaC-lotkpX2vTPs7dw8dupSZNBvS9lJAisN4")
member_id='OhlpevQzbi'#Alice Torres

#Path to store the files
IDPath="/home/johnny/Documents/linkedin/Alice/"
recordPath="/home/johnny/Documents/linkedin/Alice/recordfiles/"
#Global Three Main Variable
allID_list = [member_id]
afterProgressID_list = [member_id]
#Tmp Variable
traverseID_list = []

#Function Definition
def writeFile(member_id,content,isPublicProfileUrl):
	if isPublicProfileUrl:
		fw = open(IDPath+member_id+'_publicProfileUrl.txt','w')
	else:
		fw = open(IDPath+member_id+'.txt','w')
	fw.write(content)
	fw.close()
	return

def readFile(member_id):
	fr = open(IDPath+member_id+'.txt', 'r')
	tmpStr = fr.read()
	fr.close()
	return tmpStr

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

#Remove the traverseID_list which have already in the allID_list
def removeRedundantID(traverseID_list,allID_list):
	tmp_list=[]
	for index in range(len(traverseID_list)):
		for index2 in range(len(allID_list)):
			if traverseID_list[index] == allID_list[index2]:
				tmp_list.append(traverseID_list[index])			
	for	index in range(len(tmp_list)):
		traverseID_list.remove(tmp_list[index])
	return traverseID_list

#Search the specefic ID in allID_list and return the next ID after the current specific ID 
def getNextID(target_member_id,allID_list):
	for index in range(len(allID_list)):
		if target_member_id == allID_list[index]:
			return allID_list[index+1]

#Main Recursively function
def findRecursively( target_member_id , afterProgressID_list , allID_list , count):
	print "[TEST CODE]In findRecursively funx , target_member_id = %s ,count = %d " % (target_member_id,count)
	count = count -1
	afterProgressID_list.append(target_member_id)# Add "target member id" in orders
	try:
		writeFile(target_member_id, str(application.get_profile(member_id=target_member_id,selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])),False)
		try:
			#Read the file and transfer "python object" type into "dictionary" type
			file_content = readFile(target_member_id)
			jsonDict = ast.literal_eval(file_content)
			
			#Get friends' ID and do the Recursively  
			traverseID_list = []
			traverseID_list = traverseDictGetAllID(jsonDict,traverseID_list)#Get "New ID list" from the current "target member ID"
			traverseID_list = removeRedundantID(traverseID_list,allID_list)#Remove the IDs which have already been progressed
			
			if len(traverseID_list)!=0:#Get the new ID and insert into allID_list
				for index in range(len(allID_list)):
					if target_member_id == allID_list[index]:
						currentIDindex = index
						allID_list[currentIDindex +1:1]=traverseID_list #Insert traverseID_list into allID_list 
						break
			
			if 'publicProfileUrl' in jsonDict:#Get the publicProfileUrl and store into file 
				publicProfileUrl = jsonDict['publicProfileUrl']
				f = urllib.urlopen(publicProfileUrl)
				ppUrlContent = f.read()
				writeFile(target_member_id,ppUrlContent,True)

		except (ValueError, KeyError, TypeError) as error:
			print "***At the Inter Exception , member id = ",target_member_id
			print "***Error : ",error
	except Exception as error:
		print "***At the Outer Exception , member id = ",target_member_id
		print "***Error :",error
	
	#Get the next ID from target member ID
	if count >= 1 and len(afterProgressID_list)<len(allID_list): #Can call the API
		#Get the next element in the dictionary
		findRecursively( getNextID(target_member_id,allID_list) , afterProgressID_list , allID_list , count)
	else : #Can't call the API ,Print (1)allID_list (2)afterProgressID_list
		print "------------------------------The End-----------------------------------"
		print "[TEST CODE]All ID list = %d /  After process ID list = %d " % (len(allID_list),len(afterProgressID_list))
		#Write to file 1 = allID_list.txt
		with open(recordPath+'allID_list.txt','w') as fw1:
			for s in allID_list:
				fw1.write(s + '\n')
		fw1.close()
		#Write to file 2 = afterProgressID_list.txt
		with open(recordPath+'afterProgressID_list.txt', 'w') as fw2:
			for s in afterProgressID_list:
				fw2.write(s + '\n')
		fw2.close()
		#Write to file 3 = information.txt
		fwinf = open(recordPath+'information.txt','w')
		fwinf.write("All ID list = %d\nAfter process ID list = %d\n" % (len(allID_list),len(afterProgressID_list)))
		fwinf.close()

if os.path.isfile(recordPath+'allID_list.txt'):#Already have the file , read the files and do it continues...
	#Read file 1 = allID_list.txt
	with open(recordPath+'allID_list.txt', 'r') as fr1:
		allID_list = [line.rstrip('\n') for line in fr1]
	fr1.close()
	#Read file 2 = afterProgressID_list.txt
	with open(recordPath+'afterProgressID_list.txt', 'r') as fr2:
		afterProgressID_list = [line.rstrip('\n') for line in fr2]
	fr2.close()
	print "[TEST CODE]All ID list = %d /  After process ID list = %d " % (len(allID_list),len(afterProgressID_list))
	print "--------------------------------START------------------------------------"
	findRecursively( getNextID(afterProgressID_list[-1],allID_list) , afterProgressID_list , allID_list , 500)
else:#Don' have the record file 
	os.makedirs(recordPath)#Create the dictionary of the record file
	#Start from my own profile
	writeFile(member_id, str(application.get_profile(selectors=['first-name','last-name','maiden-name','formatted-name','phonetic-first-name','phonetic-last-name','formatted-phonetic-name','headline','current-status','current-share','shares','relation-to-viewer','connections','picture-url','picture-urls','positions','educations','member-url-resources','api-standard-profile-request','site-standard-profile-request','person-activities','recommendations-given','recommendations-received','network','twitter-accounts','im-accounts','phone-numbers','date-of-birth','main-address','location','industry','industry-id','distance','num-recommenders','current-status-timestamp','last-modified-timestamp','num-connections','summary','specialties','proposal-comments','interests','associations','honors','publications','patents','languages','skills','certifications','honors-awards','test-scores','volunteer','organizations-memberships','courses','projects','api-public-profile-request','site-public-profile-request','public-profile-url','three-current-positions','three-past-positions','bound-account-types','suggestions','primary-twitter-account','mfeed-rss-url','following','group-memberships','job-bookmarks'])),False)
	file_content = readFile(member_id)
	jsonDict = ast.literal_eval(file_content)
	traverseID_list = traverseDictGetAllID(jsonDict,traverseID_list)
	traverseID_list = removeRedundantID(traverseID_list,allID_list)#Remove the IDs which have already been progressed

	#The ID in the traverseID_list will be progressed in the future! Update the list and dictionary
	allID_list = allID_list + traverseID_list #Concatenate the list
	
	#Get the publicProfileUrl and store into file 
	if 'publicProfileUrl' in jsonDict:
		publicProfileUrl = jsonDict['publicProfileUrl']
		f = urllib.urlopen(publicProfileUrl)
		ppUrlContent = f.read()
		writeFile(member_id,ppUrlContent,True)
	findRecursively( getNextID(afterProgressID_list[-1],allID_list) , afterProgressID_list , allID_list , 500)
