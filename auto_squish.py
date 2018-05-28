#!/usr/bin/python
from subprocess import Popen, PIPE, STDOUT
import os
import sys
import subprocess
import shlex
import optparse
import glob


options=list()
op = list()

def install_rpm():
        print("installing existing RPMS...")
	cmd="cd /usr/g/ctuser/SquishRPM/ && ls"
        p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	for line in p.stdout:
        	line = line.rstrip()
        	cmd_install="sudo rpm -ivh /usr/g/ctuser/SquishRPM/"+line+""
		p=Popen(cmd_install,shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
		for line in p.stdout:
                	line = line.rstrip()
			print(line)
        cmds='cd /usr/g/ctuser && startSQUISH && cd /usr/g/ctuser/Squish'
	p=Popen(cmds, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        return True



def parse_arguments(prog_args):
	global op
    	global options
	usage = "usage: %prog [options] arg1 arg2"
	op = optparse.OptionParser(usage=usage,conflict_handler="resolve")
	op.add_option("-s", "--Scout", help="Scout", action="store_true", dest="Scout")
        op.add_option("-a", "--Axial",  help="Axial", action="store_true", dest="Axial")
        op.add_option("-c", "--Cine",  help="Cine", action="store_true", dest="Cine")
        op.add_option("-h", "--Helical", help="Helical",action="store_true", dest="Helical")
	options, arguments = op.parse_args(prog_args)


parse_arguments(sys.argv[1:])
install_rpm()

if options.Scout:
	subprocess.Popen('cd Squish && sh start_test.sh -g --tdf -u -d /usr/g/ctuser/Squish_Results/ -b Scout_scan_testing  Scout.tdf',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
	print("Scout_scan_mode Done")
	print("Displaying Summary...")
	list_of_files = glob.glob('/usr/g/ctuser/Squish_Results/*')
	latest_file = max(list_of_files, key=os.path.getctime)
	f=open(""+latest_file+"/Scout_scan_testing/Scout/Scout_1/run_tdf/curoLog.txt")
	first=f.readline().split(' ')
        line = f.readlines()[-1].split(' ')
        print("Scout tests Passed:"+ line[8])
       	print("Scout tests Failed:"+ line[11])
	print("Scout Start time:"+first[0])
	print("Scout End time:"+line[0])




if options.Axial:
        subprocess.Popen('cd Squish && sh start_test.sh -g --tdf -u -d /usr/g/ctuser/Squish_Results/ -b Axial_scan_testing  Axial.tdf',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
	print("Axial_scan_mode Done")
	print("Displaying Summary...")
	list_of_files = glob.glob('/usr/g/ctuser/Squish_Results/*')
	latest_file = max(list_of_files, key=os.path.getctime)
	f=open(""+latest_file+"/Axial_scan_testing/Axial/Axial_1/run_tdf/curoLog.txt")
	first=f.readline().split(' ')
        line = f.readlines()[-1].split(' ')
        print("Axial tests Passed:"+ line[8])
       	print("Axial tests Failed:"+ line[11])
	print("Axial Start time:"+first[0])
	print("Axial End time:"+line[0])





if options.Cine:
        subprocess.Popen('cd Squish && sh start_test.sh -g --tdf -u -d /usr/g/ctuser/Squish_Results/ -b Cine_scan_testing  Cine.tdf',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
	print("Cine_scan_mode Done")
	print("Displaying Summary...")
	list_of_files = glob.glob('/usr/g/ctuser/Squish_Results/*')
	latest_file = max(list_of_files, key=os.path.getctime)
	f=open(""+latest_file+"/Cine_scan_testing/Cine/Cine_1/run_tdf/curoLog.txt")
	first=f.readline().split(' ')
	line = f.readlines()[-1].split(' ')
        print("Cine tests Passed:"+ line[8])
        print("Cine tests Failed:"+ line[11])
	print("Cine Start time:"+first[0])
	print("Cine End time:"+line[0])




if options.Helical:
        subprocess.Popen('cd Squish && sh start_test.sh -g --tdf -u -d /usr/g/ctuser/Squish_Results/ -b Helical_scan_testing  Helical.tdf',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
	print("Helical_scan_mode Done")
	print("Displaying Summary...")
	list_of_files = glob.glob('/usr/g/ctuser/Squish_Results/*')
	latest_file = max(list_of_files, key=os.path.getctime)
 	f=open(""+latest_file+"/Helical_scan_testing/Helical/Helical_1/run_tdf/curoLog.txt")
	first=f.readline().split(' ')
        line = f.readlines()[-1].split(' ')
        print("Helical tests Passed:"+ line[8])
        print("Helical tests Failed:"+ line[11])
	print("Helical Start time:"+first[0])
	print("Helical End time:"+line[0])


subprocess.Popen('cd /usr/g/ctuser && stopSQUISH',shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT).communicate()
print("Squish Stopped")




