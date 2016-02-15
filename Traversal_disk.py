#file:Traversal_disk.py
#encoding=utf-8
import os
def travelTree(currentPath,count):
	f=open('out88.txt','a')
	if not os.path.exists(currentPath):
		return
	if os.path.isfile(currentPath):

             
		#fileName=os.path.basename(currentPath)
		fileName=os.path.basename(currentPath)
		print '\t'*count +'|~~'+ fileName
	elif os.path.isdir(currentPath):
		print '\t'*count +'|~~'+ currentPath
		pathList=os.listdir(currentPath)
		for eachPath in pathList:
			travelTree(currentPath + '/'+ eachPath,count +1)
			f.write(currentPath+'/'+ eachPath+'\n')
	f.close()
c=raw_input("Please input the disk you want travel(Not C):")
travelTree(c,1)
