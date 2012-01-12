#!/usr/bin/python

#this tool will update and install some packages on new system.
#
#charlown@gmail.com
#

import os,sys,re,platform,operator,tarfile,xml.dom.minidom
from xml.etree import ElementTree


def installPackages():

	xmlTree = xml.etree.ElementTree.parse("install.xml")
	for category in ['system','media','develop']:
		List =  xmlTree.find(category).getchildren()
		for elem in List:
			os.system('sudo apt-get install ' + elem.text + ' -y')
		
def upgradeSystem():
	os.system('sudo apt-get upgrade')

if __name__ == '__main__':
	upgradeSystem()
	installPackages()
