#!/usr/bin/env python
from subprocess import Popen    
import os
from threading import Thread
from time import sleep
import datetime



'''TODO :

##       - Offline site packages zip extract (if no internet connection)
##       - Transform the entire terminal interface to a GUI form using tk or wx
##       - Rewrite script in python3
         - After rewritten in 3, utilize yip for pip package search

'''
print "*********************************************************************"
print "-------====Snake In Da Bawks ver 1.0.1 - By QuantamKawts====---------"
print "*********************************************************************"
print "A terminal based wizard to help python developers quickly develop"
print" independant project enviornments and install categorized groups of popular pip packages by modules"
print" called a 'Bawks'"


def getvirtualenv(): 
    thread = Thread(group=None, target=lambda:os.system("pip install virtualenv"))
    thread.run() 
    if thread.is_alive():
        print "Almost!"
    else:
        print "Done!!!"           

def allbawks():
    thread1a = Thread(group=None, target=lambda:os.system("pip install -r webbawks.txt"))
    thread1a.run()
    if thread1a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread1b = Thread(group=None, target=lambda:os.system("pip install -r databawks.txt"))
        thread1b.run()
        if thread1b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"

            thread1c = Thread(group=None, target=lambda:os.system("pip install -r aibawks.txt"))
            thread1c.run()
            if thread1c.is_alive():
                print "Almost!"

def removebawks():
    thread1a = Thread(group=None, target=lambda:os.system("pip uninstall -r webbawks.txt -y"))
    thread1a.run()
    if thread1a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread1b = Thread(group=None, target=lambda:os.system("pip uninstall -r databawks.txt -y"))
        thread1b.run()
        if thread1b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"

            thread1c = Thread(group=None, target=lambda:os.system("pip uninstall -r aibawks.txt -y"))
            thread1c.run()
            if thread1c.is_alive():
                print "Almost!"
            else:
                print "Done!!!"

def getProjectName():

    print "Please Enter the name of your project"
    ootbprojname = raw_input()
    thread2h = Thread(group=None, target=lambda:Popen(["virtualenv", ootbprojname]))
    thread2h.run()
    if thread2h.is_alive():
        print "Almost!"
    else:
        print "Please wait a few seconds while your project is being built..."
    sleep(20) # it takes this long to build the enviornment 

    os.chdir(ootbprojname)
    print "You are now in the root of:" +ootbprojname 
    print os.getcwd()
    os.chdir("scripts")
    print "You are now in the scripts directory of your project"
    print os.getcwd()

def makerequiredfiles():

    file = open("webbawks.txt","w")
    file.write("flask \r\n")
    file.write("django \r\n")
    file.write("bottle \r\n")
    file.write("web2py \r\n")
    file.write("requests \r\n")
    file.write("pyramid \r\n")
    file.write("pelican \r\n")
    file.close()

    file = open("databawks.txt","w")
    file.write("numpy \r\n")
    file.write("pandas \r\n")
    file.write("scrapy \r\n")
    file.write("selenium \r\n")
    file.write("beautifulsoup \r\n")
    file.write("bokeh \r\n")
    file.write("matplotlib \r\n")
    file.write("arrow \r\n")
    file.write("dask \r\n")
    file.write("pygal \r\n")
    file.write("csvkit \r\n")
    file.write("sqlalchemy \r\n")
    file.close()

    file = open("aibawks.txt", "w")
    file.write("easyai \r\n")
    file.write("pybrain \r\n")
    file.write("pattern \r\n")
    file.write("aima \r\n")
    file.write("simpleai \r\n")
    file.write("scikit-learn \r\n")
    file.write("neurolab \r\n")
    file.write("quepy \r\n")
    file.close()

def whatsindabawks():
    installedbawkes = open("InstalledBawksesReport.txt", "a")
    installedbawkes.write("---All the packages installed from SnakeInDaBawks--- \r\n")
    installedbawkes.write(datetime.datetime.now().ctime())
    installedbawkes.close()   
    
def pipPackageMenu():
    menu = {}
    menu['1']= "Install Web Bawks"
    menu['2']= "Install Data Bawks"
    menu['3']= "Install AI Bawks"
    menu['4']= "Install All 1,2,3"
    menu['5']= "Remove All Bawks 1,2,3"
    menu['6']="View installed packages from SnakeInDaBawks"
    menu['7']="Exit"    
    while True: 
        options=menu.keys()
        options.sort()
        print "Please choose what packages you want to install "
        print "Packages will be installed within the project (lib/site-packages)"
        print " [1] [Web Framework Bawks] - Contains flask, django, bottle, web2py, requests, pelican, pyramid,"
        print " ----------------------------------------------------------------------------------------------"
        print " [2] [Data programming Bawks] - Contains numpy, pandas, scrapy, selenium, beautifulsoup, bokeh, matplotlib, arrow, dask, pygal, csvkit, sqlalchemy"
        print " ----------------------------------------------------------------------------------------------"
        print " [3] [Artifical Intelligence Bawks] Contains - easyai, pybrain, pattern, aima, simpleai, scikit-learn, neurolab, quepy"
        print " ----------------------------------------------------------------------------------------------"
        print " [4] [ALL Bawkses 1,2,3]"
        print " ----------------------------------------------------------------------------------------------"
        print " [5] [Remove all Bawkses 1,2,3]"
        print " ----------------------------------------------------------------------------------------------"
        print " [6] [View all installed packages and version info]"  
        print " ----------------------------------------------------------------------------------------------"  
        print " [7] [EXIT]"  
        selection=raw_input("Please Select a option:")

        if selection =='1': 
            thread1a = Thread(group=None, target=lambda:os.system("pip install -r webbawks.txt"))
            thread1a.run()
            if thread1a.is_alive():
                print "Almost!"
            else:
                print "Done!!!"

        elif selection == '2': 
            thread2a = Thread(group=None, target=lambda:os.system("pip install -r databawks.txt"))
            thread2a.run()
            if thread2a.is_alive():
                print "Almost!"
            else:
                print "Done!!!"

        elif selection == '3':
            thread3a = Thread(group=None, target=lambda:os.system("pip install -r aibawks.txt"))
            thread3a.run()
            if thread3a.is_alive():
                print "Almost!"
            else:
                print "Done!!!"

        elif selection == '4': 
            print"Getting all from 1,2,3 bawkses"
            allbawks()

        elif selection == '5': 
            print "Remove all from 1,2,3 bawkses"
            removebawks()

        elif selection == '6':
            os.system("pip freeze installedbawks.txt")
            os.system("pip freeze installedbawks.txt > InstalledBawksesFile.txt" )
            whatsindabawks()

        elif selection == '7': 
            break            
        else: 
            print "Invalid Option Selected! Are you Drunk?"            

getvirtualenv()
getProjectName() #comment out this line if you want to install the lib packages globally
makerequiredfiles()
pipPackageMenu()

