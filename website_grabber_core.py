# Maintainer: PH
# Version: 1.0.0 
# Filename: website_grabber_core.py

import urllib2
import time
import os

def webGrab():
    url = http://localhost:8000/pages/homepage?id=
    extension = ['1001','1002']
    for each_id in extension:
        idProcess(each_id, url)
        
def idProcess(each_id, url):
    try:
        filename=each_id
        if(each_id==""):
            filename="website"+str(time.time()).split(".")[0]
        response = urllib2.urlopen(url+str(each_id))
        webContent = response.read()
        if not os.path.exists('pages'):
            os.makedirs('pages')
        f = open('pages/'+str(filename)+'.html', 'w')
        f.write(webContent)
        f.close
    except urllib2.HTTPError as ex:
        print(ex)
    except Exception as ex:
        print("Error: "+str(filename)+" unable to be processed!")
        print("Error Msg: "+str(ex))
    