import pywhatkit

#pywhatkit.sendwhatmsg_to_group_instantly("KqHxJqfPAqtEMFiakBCTXL", "Message 4")

import requests
import urllib3
import hashlib
import time

try:
    fr = open('hashData.txt','r')
    oldHash = fr.readline().strip('\n')
    fr.close()
except:
    oldHash=""

try:
    fr2 = open('C:/Users/shaun/OneDrive/Desktop/viewgrades/getData.txt','r')
    Lines = fr2.readlines()
    print(Lines)
    type = (Lines[0].strip('\n').split(":"))[1].replace(" ","").lower()
    groupID = Lines[1].strip('\n').split(":")[1].replace(" ","")
    contact = Lines[2].strip('\n').split(":")[1].replace(" ","")
    message = "Auto generated" + Lines[3].strip('\n').split(":")[1]
    fr2.close()
except:
    print("Trouble accessing getData. Check if file is present in same directory as application and in correct format")
    exit()

if(len(oldHash)>0):
    currentHash = oldHash
else:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #response = requests.get("https://www.iitm.ac.in/viewgrades/viewgrades.php",headers={'cookie': 'PHPSESSID=4n6n226lr5jtte2vglq217qu4p'}, verify=False )
    try:
        response = requests.get("https://www.iitm.ac.in/viewgrades/viewgrades.php", verify=False )
    except:
        print("not getting the response")
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    currentHash = hashlib.sha224(response.text.encode("utf-8")).hexdigest()
#print(response.text)
print("LOLOL")
print(currentHash)
fw = open('C:/Users/shaun/OneDrive/Desktop/viewgrades/hashData.txt','w')
fw.write(currentHash)
counter=0
while True:
    time.sleep(5)
    #response = requests.get("https://www.iitm.ac.in/viewgrades/viewgrades.php",headers={'cookie': 'PHPSESSID=4n6n226lr5jtte2vglq217qu4p'}, verify=False )
    try:
        response = requests.get("https://www.iitm.ac.in/viewgrades/viewgrades.php", verify=False )
        newHash = hashlib.sha224(response.text.encode("utf-8")).hexdigest()
        print(newHash)
        if(currentHash == newHash):
            print("no change", type)
            counter+=1
            if(counter%7==0):
                if(type=="g"):
                    pywhatkit.sendwhatmsg_to_group_instantly(groupID, "Auto generated trial msg")
                elif (type=="p"):
                    print("HI")
                    pywhatkit.sendwhatmsg_instantly(contact,"Auto generated trial msg")
                else:
                    print("invalid")
            continue
        else:
            try:
                if(type=="g"):
                    pywhatkit.sendwhatmsg_to_group_instantly(groupID, message)
                elif (type=="p"):
                    pywhatkit.sendwhatmsg_instantly(contact,message)
                else:
                    print("Invalid message type")
            except:
                print("grades changed. But could not send whatsapp msg")
        try:
            fw.write(newHash)
        except:
            print("could not write new hash to file")
    except:
        print("Error getting website data")
    
    



