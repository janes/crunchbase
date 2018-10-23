import requests
import json
import csv

yugeArray= []

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

    newComp = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

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

        catUrl = "https://api.crunchbase.com/v3.1/organizations/" + newArr[i] + "/categories?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
        catResponse = requests.get(catUrl)
        catData = catResponse.json()

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
        j = 0
        while j < len(catData['data']['items']):
            newComp[23 + j] = catData['data']['items'][j]['properties']['name']
            j += 1

    yugeArray.append(newComp)

    if i == len(newArr) - 1 or i%200 == 0:
        fileName = 'newSaveCrunchbaseScrape' + str(i/200) + '.csv'
        with open(fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(yugeArray)
    i += 1
