# SnakeInDaBawks
A terminal based wizard to help python developers quickly develop independent project environments and install categorized groups of pip packages by categorized modules called "Bawks"

# What does it do exactly?
3 things to be exact:
1. Installs and sets up a virtual enviornment for your python projects
2. Groups common pip packages by category into a "Bawks" that will install popular pip packages related to it
3. When the packages are installed/uninstalled, its placed in the "Lib/site-packages" directory within the project, not globally

# What do these "Bawks" contain?
3 "Bawks" to choose from:
- [Web Framework Bawks] - installs : flask, django, bottle, web2py, requests, selenium"

- [Data Programming Bawks] - Installs : Contains numpy, pandas, scrapy, beautifulsoup, bokeh, matplotlib, opencv, arrow, dask, pygal, csvkit, sqlalchemy

- [Artifical Intelligence Bawks] Installs :easyai, pybrain, pattern, aima, simpleai, scikit-learn, neurolab, quepy

# Why use the word "Bawks"?
 Because it sounds like 'box' and a box contains many things
 
# Instructions
Step 1. Run the snakeindabox.py file :  COMMAND  $ python snakeindabox.py 
Step 2.Virtualenv will be installed globally (if it is not installed already)
Step 3.Enter a project name for your virtualenviornment (name of the project folder you want ex. MyBawksProject)
Step 4. Allow the virtualenv to create your project (just a few seconds)
Step 5. Afterwards menu will appear listing the types of bawks you can install. Enter the number of the bawks option you want to install
  Option 1 - Web Framework Bawks
  Option 2 - Data Programming Bawks
  Option 3 - Artifical Intellgenece Bawks
  Option 4 - Install all of them (install 1,2,3 )
  Option 5 - Remove all of them (uninstall 1,2,3)
  Option 6 - Quit the program
  

