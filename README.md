# README #
CFImporter helps competitive coders to import their Codeforces submissions' source-codes and categorize them based on problem tags.

## Developed by:
Swapnil Saxena, Ashish Chauhan and Ayush Awasthi. 

Everyone is welcome to introduce changes, add features, fix bugs and to distribute the project without any consent from the creator.  

## What is this repository for?

### Summary: 

#### Codeforces Importer

While solving problems on Online Judges people often lose track of their progress based on problem-categories.
Searching and importing source codes is cumbersome and time-consuming.
This small python script fetches their submission history along with their source codes and well categorizes them based on their tags. 
It also generates a HTML page that contain links to problems categorised according to their tags, along with links to local clone and actual Codeforces submissions made by the user.

## Usage  

Usage: <code>  python cfimport.py [-i, --ignore] {handle} {directory_path} </code> 

Example : 

<code> python cfimport.py dragonslayerx C:\\\\Users\\\\dragonslayerx\\\\Desktop\\\\log </code>

<code> python cfimport.py --ignore dragonslayerx C:\\\\Users\\\\dragonslayerx\\\\Desktop\\\\log </code>

Note: use python 2.7

Go to the mentioned directory and open classiied_problems.html. Imported submissions resides in the same directory.

### Version:  1.0

Initial version includes categorization of problems, fetching local copy of Codeforces submissions and generating HTML page providing appropiate links.

## Latest Releases?  

Download the latest version from here: https://github.com/dragonslayerx/CodeforcesImporter/releases

## How to Install?

Open the installed source in terminal and type

<code> python setup.py install </code> 

## External Dependencies

requests library (http://docs.python-requests.org/en/master/)

template engine (http://jinja.pocoo.org)

lxml (http://lxml.de)

You can download the prebuilt lxml library from here: https://pypi.python.org/pypi/lxml/3.5.0#downloads

## Special Thanks

We would like to thank Mike Mirzayanov for providing Codeforces API that helped us making this tool.

### How does it look like? ###

Generated template opened in browser showing user statistics

![Alt text](/./screenshots/screenshot1.PNG?raw=true "ScreenShot1")
 
Generated template opened in browser providing links to submissions along with their problem links

![Alt text](/./screenshots/screenshot2.PNG?raw=true "ScreenShot2")

* Introduce changes, add features, fix bugs and send a pull request to contribute. 

### Who do I talk to?
#### For any queries contact at:

* Ashish Chauhan (me.ashishchauhan@gmail.com), Swapnil Saxena (swapnilsaxena@live.in), Ayush Awasthi(ayushawasthi04@gmail.com)
