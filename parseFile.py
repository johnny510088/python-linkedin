#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from bs4 import BeautifulSoup
import glob
import os

reload(sys)
sys.setdefaultencoding('utf8')
IDPath="/home/johnny/Documents/linkedin/Alice/"
os.chdir(IDPath)

for ID in glob.glob("*_publicProfileUrl.txt"):
	ID = ID.replace('_publicProfileUrl.txt','')
	soup = BeautifulSoup(open(IDPath+ID+"_publicProfileUrl.txt"))#Read the txt file 
	print "-----------------------------------ID-----------------------------------------"
	print "ID = ",ID
	if not isinstance(soup.find("div",{'class':'profile-header'}),type(None)):#First kind of HTML file (Hava the <div> tag with class="profile-header")
		profileCount = len(soup.get_text())
		print "[TEST] ,profileCount = ",profileCount
		
		print "---------------------------Full-Name--------------------------------"
		name =  soup.find("span",{'class':'full-name'}).get_text()#Selce <span> tag with class full-name
		print name
		print name.istitle()# "Johnny Chan".istitle()=true , "johnny chan".istitle()=false ,"Johnny chan".istitle()=false "johnny Chan".istitle()=false
		
		print "---------------------------Connections------------------------------"
		print soup.find("dd",{'class':'overview-connections'}).find("strong").get_text()#Select <dd> tag with class overview-connection and than Select <strong> tag 
		
		print "-------------------------Profile with photo-------------------------"
		if not isinstance(soup.find("div",{'id':'profile-picture'}),type(None)):
			print "Have photo"
			print soup.find("div",{'id':'profile-picture'}).find("img",{'class':'photo'})['src']#Can get the image URL
		else:
			print "No photo"
		
		print "----------------------------Summary---------------------------------"
		summaryCount = 0
		if not isinstance(soup.find("p", {'class': ' description summary'}),type(None)):#if HTML file have class description summary 
			tmpStr = soup.find("p", {'class': ' description summary'}).get_text()#Select the <p> tag with class description summary
			#print "[TEST] ,tmpStr = ",tmpStr
			summaryCount = len(tmpStr)
		print "[TEST] ,summaryCount = ",summaryCount

		print "----------------------------Experience------------------------------"
		exeperienceCount = 0
		if not isinstance(soup.select("div.position.experience.vevent"),type(None)):
			experienceList = soup.select("div.position.experience.vevent")#Selcet all <div> tag with class = position & experience & vevent
			for i in range(len(experienceList)):
				experienceList[i] = experienceList[i].get_text().replace('\n','')
				#print "[TEST]The %d , experienceList = \n %s" % (i,experienceList[i])
				exeperienceCount = exeperienceCount + len(experienceList[i])
		print "[TEST] ,exeperienceCount  = ",exeperienceCount
		
		print "-----------------------Honors and Awards----------------------------"
		honorawardCount = 0
		if not isinstance(soup.find_all("li", {'class': 'honoraward'}),type(None)):
			honorawardList = soup.find_all("li", {'class': 'honoraward'})#Select all <li> tag with class = honoraward
			for i in range(len(honorawardList)):
				honorawardList[i] = honorawardList[i].get_text().replace('\n','')
				#print "[TEST]The %d , honorawardList = \n %s" % (i,honorawardList[i])
				honorawardCount = honorawardCount + len(honorawardList[i])
		print "[TEST] , honorawardCount = ",honorawardCount

		print "-----------------------------Course---------------------------------"
		courseCount = 0
		if not isinstance(soup.find_all("li", {'class': 'course-group'}),type(None)):
			courseList = soup.find_all("li", {'class': 'course-group'})#Select all <li> tag with class = course-group
			for i in range(len(courseList)):
				courseList[i] = courseList[i].get_text().replace('\n','')
				#print "[TEST]The %d , courseList = \n %s" % (i,courseList[i])
				courseCount = courseCount + len(courseList[i])	
		print "[TEST] , courseCount = ",courseCount

	elif not isinstance(soup.find("div",{'id':'top-header'}),type(None)):#Second kind of HTML file (Have the <div> tag with id="top-header")
		print "In Second kind of HTML file"
	
	elif not isinstance(soup.find("span",{'class':'join'}),type(None)):#Third kind of HTML file (Have the <span> tag with class="join")
		print "In Third kind of HTML file"
