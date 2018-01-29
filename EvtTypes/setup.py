#!/usr/bin/python
import os
import time

########################################################################################
## Check if MadGraph is installed
########################################################################################

if not os.path.isdir("MG5"):
	
	from tempfile import mkstemp
	from shutil import move, copytree
	
	os.system("wget 'https://launchpad.net/mg5amcnlo/2.0/2.6.x/+download/MG5_aMC_v2.6.1.tar.gz'")
	os.system('tar zxvf MG5_aMC_v2.6.1.tar.gz')
	os.system('rm MG5_aMC_v2.6.1.tar.gz')
	os.system('mv MG5_aMC_v2_6_1 MG5')
	currentdir = os.getcwd()
	os.chdir(currentdir+"/MG5/input")
	
	def replace(file_path, pattern, subst):
		#Create temp file
		fh, abs_path = mkstemp()
		with os.fdopen(fh,'w') as new_file:
			with open(file_path) as old_file:
				for line in old_file:
					new_file.write(line.replace(pattern, subst))
		#Remove original file
		os.remove(file_path)
		#Move new file
		move(abs_path, file_path)

	replace("mg5_configuration.txt", "# automatic_html_opening = True", "automatic_html_opening = False")
	os.chdir(currentdir)
	copytree("lowscaleseesaw_UFO","MG5/models/lowscaleseesaw_UFO")
	
	time.sleep(1)
	
	replace("rhn.py", "mg5 = ''", "mg5 = {}/MG5/bin/mg5_aMC".format( currentdir))
	
	time.sleep(1)
	
		