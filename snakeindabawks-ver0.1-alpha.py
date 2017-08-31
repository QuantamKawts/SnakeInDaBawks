import tkMessageBox
from subprocess import Popen    
import os
from threading import Thread
from time import sleep

'''TODO : - Logging - Log export of the installed packages (perhaps to a txt file and include date and time)
##       - offline site packages zip extract (if no internet connection)
##       - In the menu, add an option to let choose the name of the pip package they want via user input
##       - Transform the entire terminal interface to a GUI form using tk or wx
'''
print "*********************************************************************"
print "-------====Snake In Da Bawks ver 0.1.0 - By QuantamKawts====---------"
print "*********************************************************************"
print " A terminal based wizard to help python programmers quickly develop"
print" independant project enviornments and install categorized groups of pip packages by modules"
print "called 'Bawks'"


def getvirtualenv(): 
    thread = Thread(group=None, target=lambda:os.system("pip install virtualenv"))
    thread.run() 
    if thread.is_alive():
        print "Almost!"
    else:
        print "Done!!!"           
        
def allbawks():
    #web bawks
    thread1a = Thread(group=None, target=lambda:os.system("pip  install flask"))
    thread1a.run()
    if thread1a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread1b = Thread(group=None, target=lambda:os.system("pip  install django"))
        thread1b.run()
        if thread1b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"

            thread1c = Thread(group=None, target=lambda:os.system("pip  install bottle"))
            thread1c.run()
            if thread1c.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
                thread1d = Thread(group=None, target=lambda:os.system("pip  install web2py"))
                thread1d.run()
                if thread1d.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"
                    thread1e = Thread(group=None, target=lambda:os.system("pip install requests"))
                    thread1e.run()
                    if thread1e.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!"
                        thread1f = Thread(group=None, target=lambda:os.system("pip install selenium"))
                        thread1f.run()
                        if thread1f.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"

    #data programming bawks
    thread2a = Thread(group=None, target=lambda:os.system("pip  install numpy"))
    thread2a.run()
    if thread2a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"

        thread2b = Thread(group=None, target=lambda:os.system("pip  install pandas"))
        thread2b.run()
        if thread2b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"
            thread2c = Thread(group=None, target=lambda:os.system("pip  install scrapy"))
            thread2c.run()
            if thread2c.is_alive():
                print "Almost!"
            else:
                print 'Done!!!'

                thread2d = Thread(group=None, target=lambda:os.system("pip  install beautifulsoup"))
                thread2d.run()
                if thread2d.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"    

                    thread2e = Thread(group=None, target=lambda:os.system("pip  install bokeh"))
                    thread2e.run()
                    if thread2e.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!" 

                        thread2f = Thread(group=None, target=lambda:os.system("pip  install matplotlib"))
                        thread2f.run()
                        if thread2f.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"

                            thread2g = Thread(group=None, target=lambda:os.system("pip  install opencv"))
                            thread2g.run()
                            if thread2g.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!"   

                                thread2h = Thread(group=None, target=lambda:os.system("pip  install arrow"))
                                thread2h.run()
                                if thread2h.is_alive():
                                    print "Almost!"
                                else:
                                    print "Done!!!"  

                                    thread2i = Thread(group=None, target=lambda:os.system("pip  install dask"))
                                    thread2i.run()
                                    if thread2i.is_alive():
                                        print "Almost!"
                                    else:
                                        print "Done!!!"      
    
                                        thread2j = Thread(group=None, target=lambda:os.system("pip install pygal"))
                                        thread2j.run()
                                        if thread2j.is_alive():
                                            print "Almost!"
                                        else:
                                            print "Done!!!"  
        
                                            thread2k = Thread(group=None, target=lambda:os.system("pip install csvkit"))
                                            thread2k.run()
                                            if thread2k.is_alive():
                                                print "Almost!"
                                            else:
                                                print "Done!!!" 
                                                thread2l = Thread(group=None, target=lambda:os.system("pip install sqlalchemy"))
                                                thread2l.run()
                                                if thread2i.is_alive():
                                                    print "Almost!"
                                                else:
                                                    print "Done!!!"                                                   
    #ai bawks
    thread3a = Thread(group=None, target=lambda:os.system("pip  install easyai"))
    thread3a.run()
    if thread3a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread3b = Thread(group=None, target=lambda:os.system("pip  install pybrain"))
        thread3b.run()
        if thread3b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"
            thread3c = Thread(group=None, target=lambda:os.system("pip  install pattern"))
            thread3c.run()
            if thread3c.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
                thread3d = Thread(group=None, target=lambda:os.system("pip  install aima"))
                thread3d.run()
                if thread3d.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"

                    thread3e = Thread(group=None, target=lambda:os.system("pip  install simpleai"))
                    thread3e.run()
                    if thread3e.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!"

                        thread3f = Thread(group=None, target=lambda:os.system("pip  install scikit-learn"))
                        thread3f.run()
                        if thread3f.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"   

                            thread3g = Thread(group=None, target=lambda:os.system("pip  install neurolab"))
                            thread3g.run()
                            if thread3g.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!"  

                                thread3h = Thread(group=None, target=lambda:os.system("pip  install quepy"))
                                thread3h.run()
                                if thread3h.is_alive():
                                    print "Almost!"
                                else:
                                    print "Done!!!"       

def removebawks():
    thread1a = Thread(group=None, target=lambda:os.system("pip  uninstall -y flask"))
    thread1a.run()
    if thread1a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread1b = Thread(group=None, target=lambda:os.system("pip  uninstall  -y django"))
        thread1b.run()
        if thread1b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"

            thread1c = Thread(group=None, target=lambda:os.system("pip uninstall -y bottle"))
            thread1c.run()
            if thread1c.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
                thread1d = Thread(group=None, target=lambda:os.system("pip uninstall -y web2py"))
                thread1d.run()
                if thread1d.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"
                    thread1e = Thread(group=None, target=lambda:os.system("pip  uninstall -y requests"))
                    thread1e.run()
                    if thread1e.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!"
                        thread1f = Thread(group=None, target=lambda:os.system("pip uninstall -y selenium"))
                        thread1f.run()
                        if thread1f.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"                        

    thread2a = Thread(group=None, target=lambda:os.system("pip uninstall -y numpy"))
    thread2a.run()
    if thread2a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"

        thread2b = Thread(group=None, target=lambda:os.system("pip  uninstall -y pandas"))
        thread2b.run()
        if thread2b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"
            thread2c = Thread(group=None, target=lambda:os.system("pip  uninstall  -y scrapy"))
            thread2c.run()
            if thread2c.is_alive():
                print "Almost!"
            else:
                print 'Done!!!'

                thread2d = Thread(group=None, target=lambda:os.system("pip uninstall -y beautifulsoup"))
                thread2d.run()
                if thread2d.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"    

                    thread2e = Thread(group=None, target=lambda:os.system("pip  uninstall -y bokeh"))
                    thread2e.run()
                    if thread2e.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!" 

                        thread2f = Thread(group=None, target=lambda:os.system("pip uninstall -y matplotlib"))
                        thread2f.run()
                        if thread2f.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"

                            thread2g = Thread(group=None, target=lambda:os.system("pip uninstall -y opencv"))
                            thread2g.run()
                            if thread2g.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!"   

                                thread2h = Thread(group=None, target=lambda:os.system("pip uninstall -y arrow"))
                                thread2h.run()
                                if thread2h.is_alive():
                                    print "Almost!"
                                else:
                                    print "Done!!!"  

                                    thread2i = Thread(group=None, target=lambda:os.system("pip uninstall -y dask"))
                                    thread2i.run()
                                    if thread2i.is_alive():
                                        print "Almost!"
                                    else:
                                        print "Done!!!"
                                        thread2j = Thread(group=None, target=lambda:os.system("pip uninstall -y pygal"))
                                        thread2j.run()
                                        if thread2j.is_alive():
                                            print "Almost!"
                                        else:
                                            print "Done!!!"  
        
                                            thread2k = Thread(group=None, target=lambda:os.system("pip uninstall -y csvkit"))
                                            thread2k.run()
                                            if thread2k.is_alive():
                                                print "Almost!"
                                            else:
                                                print "Done!!!" 
                                                thread2l = Thread(group=None, target=lambda:os.system("pip uninstall -y sqlalchemy"))
                                                thread2l.run()
                                                if thread2l.is_alive():
                                                    print "Almost!"
                                                else:
                                                    print "Done!!!"                                        

    thread3a = Thread(group=None, target=lambda:os.system("pip uninstall -y easyai"))
    thread3a.run()
    if thread3a.is_alive():
        print "Almost!"
    else:
        print "Done!!!"
        thread3b = Thread(group=None, target=lambda:os.system("pip  uninstall -y pybrain"))
        thread3b.run()
        if thread3b.is_alive():
            print "Almost!"
        else:
            print "Done!!!"
            thread3c = Thread(group=None, target=lambda:os.system("pip  uninstall  -y pattern"))
            thread3c.run()
            if thread3c.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
                thread3d = Thread(group=None, target=lambda:os.system("pip  uninstall -y aima"))
                thread3d.run()
                if thread3d.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"

                    thread3e = Thread(group=None, target=lambda:os.system("pip  uninstall -y simpleai"))
                    thread3e.run()
                    if thread3e.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!"

                        thread3f = Thread(group=None, target=lambda:os.system("pip  uninstall  -y scikit-learn"))
                        thread3f.run()
                        if thread3f.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"   

                            thread3g = Thread(group=None, target=lambda:os.system("pip  uninstall -y neurolab"))
                            thread3g.run()
                            if thread3g.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!"  

                                thread3h = Thread(group=None, target=lambda:os.system("pip  uninstall -y quepy"))
                                thread3h.run()
                                if thread3h.is_alive():
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
            print "Please wait around a few seconds while your project is being built..."
    sleep(35) # it takes this long to build the enviornment 
    
    os.chdir(ootbprojname)
    print "You are now in the root of:" +ootbprojname 
    print os.getcwd()
    os.chdir("scripts")
    print "You are now in the scripts directory of your project"
    print os.getcwd()
    
def pipPackageMenu():
    menu = {}
    menu['1']= "Install Web Package"
    menu['2']= "Install Data Box"
    menu['3']= "Install AI Box"
    menu['4']= "ALL boxes"
    menu['5']= "Remove all Boxes"
    menu['6']="Exit"
    while True: 
        options=menu.keys()
        options.sort()
        print "Please choose what packages you want to install"
        print " [1] Web Framework Bawks - Contains flask, django, bottle, web2py, requests, selenium"
        print " [2] Data programming Bawks - Contains numpy, pandas, scrapy, beautifulsoup, bokeh, matplotlib, opencv, arrow, dask, pygal, csvkit, sqlalchemy"
        print " [3] Artifical Intelligence Bawks - easyai, pybrain, pattern, aima, simpleai, scikit-learn, neurolab, quepy"
        print " [4] ALL Bawkses 1,2,3"
        print " [5] Remove all Bawkses 1,2,3"
        #print "[6] Packages Available" pip search *
        #print "[7] Out of da bawks - Let you choose your own Package name"
        print " [6] EXIT"         
        selection=raw_input("Please Select a Bawks:")
       
        if selection =='1': 
                thread1a = Thread(group=None, target=lambda:os.system("pip install flask"))
                thread1a.run()
                if thread1a.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"
                    thread1b = Thread(group=None, target=lambda:os.system("pip install django"))
                    thread1b.run()
                    if thread1b.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!"
                        
                        thread1c = Thread(group=None, target=lambda:os.system("pip install bottle"))
                        thread1c.run()
                        if thread1c.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"
                            thread1d = Thread(group=None, target=lambda:os.system("pip  install web2py"))
                            thread1d.run()
                            if thread1d.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!"
                                thread1e = Thread(group=None, target=lambda:os.system("pip  install requests"))
                                thread1e.run()
                                if thread1e.is_alive():
                                    print "Almost!"
                                else:
                                    print "Done!!!"
                                    thread1f = Thread(group=None, target=lambda:os.system("pip  install selenium"))
                                    thread1f.run()
                                    if thread1f.is_alive():
                                        print "Almost!"
                                    else:
                                        print "Done!!!"                                          

        elif selection == '2': 
            thread2a = Thread(group=None, target=lambda:os.system("pip  install numpy"))
            thread2a.run()
            if thread2a.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
                
                thread2b = Thread(group=None, target=lambda:os.system("pip  install pandas"))
                thread2b.run()
                if thread2b.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"
                    thread2c = Thread(group=None, target=lambda:os.system("pip  install scrapy"))
                    thread2c.run()
                    if thread2c.is_alive():
                        print "Almost!"
                    else:
                        print 'Done!!!'
                        
                        thread2d = Thread(group=None, target=lambda:os.system("pip install beautifulsoup"))
                        thread2d.run()
                        if thread2d.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"    
                            
                            thread2e = Thread(group=None, target=lambda:os.system("pip install bokeh"))
                            thread2e.run()
                            if thread2e.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!" 
                                
                                thread2f = Thread(group=None, target=lambda:os.system("pip  install matplotlib"))
                                thread2f.run()
                                if thread2f.is_alive():
                                    print "Almost!"
                                else:
                                    print "Done!!!"
                                    
                                    thread2g = Thread(group=None, target=lambda:os.system("pip  install opencv"))
                                    thread2g.run()
                                    if thread2g.is_alive():
                                        print "Almost!"
                                    else:
                                        print "Done!!!"   
                                        
                                        thread2h = Thread(group=None, target=lambda:os.system("pip  install arrow"))
                                        thread2h.run()
                                        if thread2h.is_alive():
                                            print "Almost!"
                                        else:
                                            print "Done!!!"  
                                            
                                            thread2i = Thread(group=None, target=lambda:os.system("pip  install dask"))
                                            thread2i.run()
                                            if thread2i.is_alive():
                                                print "Almost!"
                                            else:
                                                print "Done!!!"
                                                
                                                thread2j = Thread(group=None, target=lambda:os.system("pip install  pygal"))
                                                thread2j.run()
                                                if thread2j.is_alive():
                                                    print "Almost!"
                                                else:
                                                    print "Done!!!"  
                
                                                    thread2k = Thread(group=None, target=lambda:os.system("pip install csvkit"))
                                                    thread2k.run()
                                                    if thread2k.is_alive():
                                                        print "Almost!"
                                                    else:
                                                        print "Done!!!" 
                                                        thread2l = Thread(group=None, target=lambda:os.system("pip install sqlalchemy"))
                                                        thread2l.run()
                                                        if thread2l.is_alive():
                                                            print "Almost!"
                                                        else:
                                                            print "Done!!!"                                                 
                                                                
                
        elif selection == '3':
            thread3a = Thread(group=None, target=lambda:os.system("pip  install easyai"))
            thread3a.run()
            if thread3a.is_alive():
                print "Almost!"
            else:
                print "Done!!!"
                
                thread3b = Thread(group=None, target=lambda:os.system("pip  install pybrain"))
                thread3b.run()
                if thread3b.is_alive():
                    print "Almost!"
                else:
                    print "Done!!!"
                    thread3c = Thread(group=None, target=lambda:os.system("pip  install pattern"))
                    thread3c.run()
                    if thread3c.is_alive():
                        print "Almost!"
                    else:
                        print "Done!!!"
                        thread3d = Thread(group=None, target=lambda:os.system("pip  install aima"))
                        thread3d.run()
                        if thread3d.is_alive():
                            print "Almost!"
                        else:
                            print "Done!!!"
                            
                            thread3e = Thread(group=None, target=lambda:os.system("pip  install simpleai"))
                            thread3e.run()
                            if thread2e.is_alive():
                                print "Almost!"
                            else:
                                print "Done!!!"
                                
                                thread3f = Thread(group=None, target=lambda:os.system("pip  install scikit-learn"))
                                thread3f.run()
                                if thread3f.is_alive():
                                    print "Almost!"
                                else:
                                    print "Done!!!"   
                                    
                                    thread3g= Thread(group=None, target=lambda:os.system("pip  install neurolab"))
                                    thread3g.run()
                                    if thread3g.is_alive():
                                        print "Almost!"
                                    else:
                                        print "Done!!!"  
                                        
                                        thread3h = Thread(group=None, target=lambda:os.system("pip  install quepy"))
                                        thread3h.run()
                                        if thread3h.is_alive():
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
