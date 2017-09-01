#!/usr/bin/env python
from subprocess import Popen    
import os
from threading import Thread
from time import sleep

'''TODO : - Logging - Log export of the installed packages (perhaps to a txt file and include date and time)
##       - Offline site packages zip extract (if no internet connection)
##       - Transform the entire terminal interface to a GUI form using tk or wx
##       - Rewrite script in python3
         - After rewritten in 3, utilize yip for pip package search
     
'''
print "*********************************************************************"
print "-------====Snake In Da Bawks ver 0.2.0 - By QuantamKawts====---------"
print "*********************************************************************"
print "A terminal based wizard to help python programmers quickly develop"
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
    thread1a = Thread(group=None, target=lambda:os.system("pip install webbawks.txt"))
    thread1a.run()
    if thread1a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread1b = Thread(group=None, target=lambda:os.system("pip install databawks.txt"))
        thread1b.run()
        if thread1b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"

            thread1c = Thread(group=None, target=lambda:os.system("pip install aibawks.txt"))
            thread1c.run()
            if thread1c.is_alive():
                print "Almost!"
        
def removebawks():
    thread1a = Thread(group=None, target=lambda:os.system("pip uninstall -y webbawks.txt"))
    thread1a.run()
    if thread1a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread1b = Thread(group=None, target=lambda:os.system("pip uninstall -y databawks.txt"))
        thread1b.run()
        if thread1b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"

            thread1c = Thread(group=None, target=lambda:os.system("pip uninstall -y aibawks.txt"))
            thread1c.run()
            if thread1c.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
           
def getProjectName():
    #ootbprojname = MyBawksProject - decided not to hardcode project name
    print "Please Enter the name of your project"
    ootbprojname = raw_input()
    thread2h = Thread(group=None, target=lambda:Popen(["virtualenv", ootbprojname]))
    thread2h.run()
    if thread2h.is_alive():
            print "Almost!"
    else:
            print "Please wait a few seconds while your project is being built..."
    sleep(30) # it takes this long to build the enviornment 
    
    os.chdir(ootbprojname)
    print "You are now in the root of:" +ootbprojname 
    print os.getcwd()
    os.chdir("scripts")
    print "You are now in the scripts directory of your project"
    print os.getcwd()
    
def pipPackageMenu():
    menu = {}
    menu['1']= "Install Web Bawks"
    menu['2']= "Install Data Bawks"
    menu['3']= "Install AI Bawks"
    menu['4']= "Install All 1,2,3"
    menu['5']= "Remove All Bawks 1,2,3"
    menu['6']="Exit"
    while True: 
        options=menu.keys()
        options.sort()
        print "Please choose what packages you want to install "
        print "Packages will be installed within the project (lib/site-packages)"
        print " [1] [Web Framework Bawks] - Contains flask, django, bottle, web2py, requests, selenium"
        print "-----------------------------------------------------------------------------------------"
        print " [2] [Data programming Bawks] - Contains numpy, pandas, scrapy, beautifulsoup, bokeh, matplotlib, opencv, arrow, dask, pygal, csvkit, sqlalchemy"
        print "-----------------------------------------------------------------------------------------"
        print " [3] [Artifical Intelligence Bawks] Contains - easyai, pybrain, pattern, aima, simpleai, scikit-learn, neurolab, quepy"
        print "-----------------------------------------------------------------------------------------"
        print " [4] [ALL Bawkses 1,2,3]"
        print "-----------------------------------------------------------------------------------------"
        print " [5] [Remove all Bawkses 1,2,3]"
        print "-----------------------------------------------------------------------------------------"
        print " [6] [EXIT]"         
        selection=raw_input("Please Select a Bawks:")
       
        if selection =='1': 
                thread1a = Thread(group=None, target=lambda:os.system("pip install webbawks.txt"))
                thread1a.run()
                if thread1a.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"

        elif selection == '2': 
            thread2a = Thread(group=None, target=lambda:os.system("pip install databawks.txt"))
            thread2a.run()
            if thread2a.is_alive():
                print "Almost!"
            else:
                print "Done!!!"

        elif selection == '3':
            thread3a = Thread(group=None, target=lambda:os.system("pip install aibawks.txt"))
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
            break            
        else: 
            print "Invalid Option Selected! Are you Drunk?"

getvirtualenv()
getProjectName() #comment out this line if you want to install the lib packages globally
pipPackageMenu()
