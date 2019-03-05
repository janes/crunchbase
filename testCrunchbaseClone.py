import requests
import csv
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')


url = "https://api.crunchbase.com/v3.1/organizations"
querystring = {"locations":"North Carolina", "user_key":"188fa1875a4cf6c62d23c98e9afb01ed"}
response = requests.request("GET", url, params=querystring).json()

nextUrl = ""
newArr = []
pages = response['data']['paging']['number_of_pages']
print(pages)

i = 0
while i < pages:
    print(i)
    if i != 0:
        response = requests.get(nextUrl).json()

        
    j = 0
    while j < len(response['data']['items']):
        newArr.append(response['data']['items'][j]['properties']['api_path'])
        j+= 1
    if response['data']['paging']['next_page_url']:
        print(response['data']['paging']['next_page_url'])
        nextUrl = str(response['data']['paging']['next_page_url'].encode('utf-8')) + "&user_key=188fa1875a4cf6c62d23c98e9afb01ed" 

    i += 1

print(len(newArr))

yugeArray= []
founderArray = []
fundingArray = []
i = 0
while i < len(newArr):
    url = "https://api.crunchbase.com/v3.1/" + newArr[i] + "?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
    response = requests.get(url)
    data = response.json()

    newComp = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    newFound = []
    newFund = []

    if len(data) != 1:
        try:
            hqUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/offices?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            hqResponse = requests.get(hqUrl)
            hqData = hqResponse.json()

            webUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/websites?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            webResponse = requests.get(webUrl)
            webData = webResponse.json()

            foundUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/founders?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            foundResponse = requests.get(foundUrl)
            foundData = foundResponse.json()

            catUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/categories?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            catResponse = requests.get(catUrl)
            catData = catResponse.json()
            print(newArr[i])
            url13 = "https://api.crunchbase.com/v3.1/" + newArr[i] + '/funding_rounds/' + "?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            response123 = requests.get(url13)
            fundingData = response123.json()

            newComp[29] = data["data"]['uuid']
            newComp[0] = data["data"]['properties']['name']
            newComp[1] = data["data"]['properties']['founded_on']
            newComp[23] = data["data"]['properties']['is_closed']
            newComp[24] = data["data"]['properties']['closed_on']
            newComp[25] = data["data"]['properties']['stock_exchange']
            newComp[26] = data["data"]['properties']['stock_symbol']
            newComp[27] = data["data"]['properties']['total_funding_usd']
            newComp[28] = data["data"]['properties']['number_of_investments']
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
            newFound.append(data["data"]['uuid'])
            while x < len(foundData['data']['items']):
                newFound.append(foundData['data']['items'][x]['properties']['first_name'])
                newFound.append(foundData['data']['items'][x]['properties']['last_name'])
                newFound.append(foundData['data']['items'][x]['properties']['born_on'])
                newFound.append(foundData['data']['items'][x]['properties']['bio'])
                newFound.append(foundData['data']['items'][x]['properties']['api_url'])
                x += 1
            j = 0
            while j < len(catData['data']['items']):
                newComp.append(catData['data']['items'][j]['properties']['name'])
                j += 1
            newFund.append(data["data"]['uuid'])
            if (fundingData['data']['paging']['total_items'] != 0):
                numberOfFunding = fundingData['data']['paging']['total_items'] - 1
                i123 = 0
                while (i123 < numberOfFunding):

                    newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['type'])

                    newComp.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['type'])
                    try:
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['investor_type'])
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['founded_on'])
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['short_description'])
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['total_funding_usd'])
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['number_of_investments'])

                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['money_invested_usd'])
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['announced_on'])
                        newFund.append(fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['is_lead_investor'])
                    except:
                        print(1)
                    newFund.append(fundingData['data']['items'][i123]['type'])

                    newFund.append(fundingData['data']['items'][i123]['properties']['series'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['rank'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['pre_money_valuation'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['money_raised_usd'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['pre_money_valuation_usd'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['money_raised'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['updated_at'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['target_money_raised_usd'])
                    newFund.append(fundingData['data']['items'][i123]['properties']['announced_on'])
                    i123 += 1
        except:
            print(1)


    yugeArray.append(newComp)
    founderArray.append(newFound)
    fundingArray.append(newFund)


    if i == len(newArr) - 1 or i%200 == 0:
        fileName = 'newSaveFullCrunchbaseScrape' + str((i)/200) + '.csv'
        with open(fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(yugeArray)
        fileName = 'newSaveFullCrunchbaseScrapeFounders' + str((i)/200) + '.csv'
        with open(fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(founderArray)
        fileName = 'newSaveFullCrunchbaseScrapeFunding' + str((i)/200) + '.csv'
        with open(fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(fundingArray)
    i += 1

