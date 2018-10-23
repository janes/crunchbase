import requests
import json


yugeArray= []
class Company:
    def __init__(self, name, founded, short_description, min_employees, max_employees, email, phone, alias, homepage, country, region, zip1, street1, street2, homepage2, facebook, twitter, linkedin, firstname, lastname, born, bio, api_url):
        self.name = name
        self.founded = founded
        self.short_description = short_description
        self.min_employees = min_employees
        self.max_employees = max_employees
        self.email = email
        self.phone = phone
        self.alias = alias
        self.homepage = homepage
        self.country = country
        self.region = region
        self.zip1 = zip1
        self.street1 = street1
        self.street2 = street2
        self.homepage2 = homepage2
        self.facebook = facebook
        self.twitter = twitter
        self.linkedin = linkedin
        self.firstname = firstname
        self.lastname = lastname
        self.born = born
        self.bio = bio
        self.api_url = api_url

with open("cleanedCompanyNames1.txt", 'r') as names:
    newArr = []
    for line in names:
        newArr.append(line)
    i = 0
    while i < len(newArr):
        newArr[i] = newArr[i][:-1]
        i += 1
        

i = 0
while i < len(newArr):
    url = "https://api.crunchbase.com/v3.1/organizations/" + newArr[i] + "?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
    response = requests.get(url)
    data = response.json()

    newComp = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    if len(data) != 1:
        hqUrl = "https://api.crunchbase.com/v3.1/organizations/" + newArr[i] + "/offices?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
        hqResponse = requests.get(hqUrl)
        hqData = hqResponse.json()

        webUrl = "https://api.crunchbase.com/v3.1/organizations/" + newArr[i] + "/websites?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
        webResponse = requests.get(webUrl)
        webData = webResponse.json()

        foundUrl = "https://api.crunchbase.com/v3.1/organizations/" + newArr[i] + "/founders?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
        foundResponse = requests.get(foundUrl)
        foundData = foundResponse.json()

        newComp[0] = data["data"]['properties']['name']
        newComp[1] = data["data"]['properties']['founded_on']
        if data["data"]['properties']['short_description'] != None:
            newComp[2] = data["data"]['properties']['short_description'].encode('utf-8')
        newComp[3] = data["data"]['properties']['num_employees_min']
        newComp[4] = data["data"]['properties']['num_employees_max']
        newComp[5] = data["data"]['properties']['contact_email']
        newComp[6] = data["data"]['properties']['phone_number']
        newComp[7] = data["data"]['properties']['also_known_as']
        newComp[8] = data["data"]['properties']['homepage_url']

        if hqData['data']['paging']['total_items'] != 0:
            newComp[9] = hqData['data']['items'][0]['properties']['country']
            newComp[10] = hqData['data']['items'][0]['properties']['region']
            newComp[11] = hqData['data']['items'][0]['properties']['postal_code']
            if hqData['data']['items'][0]['properties']['street_1'] != None:
                newComp[12] = hqData['data']['items'][0]['properties']['street_1'].encode('utf-8')
            newComp[13] = hqData['data']['items'][0]['properties']['street_2']

        z = 0
        while z < len(webData['data']['items']):
            if z == 0:
                newComp[14] = webData['data']['items'][z]['properties']['url']
            if z == 1:
                newComp[15] = webData['data']['items'][z]['properties']['url']
            if z == 2:
                newComp[16] = webData['data']['items'][z]['properties']['url']
            if z == 3:
                newComp[17] = webData['data']['items'][z]['properties']['url']
            z += 1

        x = 0
        while x < len(foundData['data']['items']):
            newComp[18] = foundData['data']['items'][x]['properties']['first_name']
            newComp[19] =  foundData['data']['items'][x]['properties']['last_name']
            newComp[20] =  foundData['data']['items'][x]['properties']['born_on']
            newComp[21] =  foundData['data']['items'][x]['properties']['bio']
            newComp[22] =  foundData['data']['items'][x]['properties']['api_url']
            x += 1

    yugeArray.append(newComp)

    fileName = 'newSaveCrunchbaseScrape' + str(i/200) + '.txt'
    print fileName
    if i == len(newArr) - 1 or i%200 == 0:
        with open('newSaveCrunchbaseScrape.txt', 'w') as f:
            for item in yugeArray:
                f.write("%s\n" % item)

    i += 1





