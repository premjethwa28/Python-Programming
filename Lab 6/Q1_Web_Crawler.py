"""
Created on Sat Jul 28 15:30:53 2022

@author: Prem Atul Jethwa
UTA Id : 1001861810
"""

from urllib.request import urlopen
import re 

def main():
    url1 = 'file:///C:\\Users\\premj\\Downloads\\Lab6_Webpage.html' 
    url2 = 'http://e-mailid.blogspot.com/'

    document1 = urlopen(url1).read().decode()
    document2 = urlopen(url2).read().decode()

    emailListsHtml = emails(document1)  #call emails function
    emailListsUrl = emails(document2)   #call emails function

    print(emailListsHtml)
    print(emailListsUrl)

def emails(document1):
   
    regex = '[\w\.]+@[\w\.]+'     #regular expression
    getEmail = re.findall(regex, document1)
    
    uniqueEmail = []
   
    for x in getEmail:
        if x not in uniqueEmail:
           uniqueEmail.append(x) 
    
    return uniqueEmail

if __name__ == '__main__':
    main()              #call main function