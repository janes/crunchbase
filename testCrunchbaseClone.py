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
i = 1400
while i < len(newArr):
    try:
        url = "https://api.crunchbase.com/v3.1/" + newArr[i] + "?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
        response = requests.get(url)
        data = response.json()
    except:
        print("initial request")

    newComp = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    newFound = []
    newFund = []

    if len(data) != 1:
        try:
            hqUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/offices?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            hqResponse = requests.get(hqUrl)
            hqData = hqResponse.json()
        except:
            print(1)
        try:
            webUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/websites?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            webResponse = requests.get(webUrl)
            webData = webResponse.json()
        except:
            print(1)
        try:
            foundUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/founders?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            foundResponse = requests.get(foundUrl)
            foundData = foundResponse.json()
        except:
            print(1)
        try:
            catUrl = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/categories?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            catResponse = requests.get(catUrl)
            catData = catResponse.json()
        except:
            print(1)
        try:
            print(newArr[i])
            url13 = "https://api.crunchbase.com/v3.1/" + newArr[i] + "/funding_rounds?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
            response123 = requests.get(url13)
            fundingData = response123.json()
        except:
            print("funding query")
        try:
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
        except:
            print("basic data")
        try:
            if hqData['data']['paging']['total_items'] != 0:
                newComp[9] = hqData['data']['items'][0]['properties']['country']
                newComp[10] = hqData['data']['items'][0]['properties']['region']
                newComp[11] = hqData['data']['items'][0]['properties']['postal_code']
                if hqData['data']['items'][0]['properties']['street_1'] != None:
                    newComp[12] = hqData['data']['items'][0]['properties']['street_1'].encode('utf-8')
                newComp[13] = hqData['data']['items'][0]['properties']['street_2']
        except:
            print("hq data")
        try:
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
        except:
            print("web urls")
        try:
            x = 0
            
            while x < len(foundData['data']['items']):
                newFound = ["","","","","",""]
                newFound[0]= (data["data"]['uuid'])
                newFound[1]= (foundData['data']['items'][x]['properties']['first_name'])
                newFound[2]= (foundData['data']['items'][x]['properties']['last_name'])
                newFound[3]= (foundData['data']['items'][x]['properties']['born_on'])
                newFound[4]= (foundData['data']['items'][x]['properties']['bio'])
                newFound[5]= (foundData['data']['items'][x]['properties']['api_url'])
                founderArray.append(newFound)
                x += 1
            j = 0
            while j < len(catData['data']['items']):
                newComp.append(catData['data']['items'][j]['properties']['name'])
                j += 1
            if (fundingData['data']['paging']['total_items'] != 0):
                numberOfFunding = fundingData['data']['paging']['total_items'] - 1
                i123 = 0
                while (i123 < numberOfFunding):
                    newFund = ["","","","","","","","","","","","","","","","","","",""]
                    newFund.append(data["data"]['uuid'])
                    newFund[0] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['type'])

                    newFund[1] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['type'])
                    try:
                        newFund[2] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['investor_type'])
                        newFund[3] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['founded_on'])
                        newFund[4] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['short_description'])
                        newFund[5] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['total_funding_usd'])
                        newFund[6] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['number_of_investments'])

                        newFund[7] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['money_invested_usd'])
                        newFund[8] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['announced_on'])
                        newFund[9] = (fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['is_lead_investor'])
                    except:
                        print("in funding")

                    newFund[10] = (fundingData['data']['items'][i123]['properties']['series'])
                    newFund[11] = (fundingData['data']['items'][i123]['properties']['rank'])
                    newFund[12] = (fundingData['data']['items'][i123]['properties']['pre_money_valuation'])
                    newFund[13] = (fundingData['data']['items'][i123]['properties']['money_raised_usd'])
                    newFund[14] = (fundingData['data']['items'][i123]['properties']['pre_money_valuation_usd'])
                    newFund[15] = (fundingData['data']['items'][i123]['properties']['money_raised'])
                    newFund[16] = (fundingData['data']['items'][i123]['properties']['updated_at'])
                    newFund[17] = (fundingData['data']['items'][i123]['properties']['target_money_raised_usd'])
                    newFund[18] = (fundingData['data']['items'][i123]['properties']['announced_on'])
                    fundingArray.append(newFund)
                    i123 += 1
        except:
            print("funding prob")
        


    yugeArray.append(newComp)
    


    if i == len(newArr) - 1 or i%200 == 0:
        fileName = 'newSaveFullCrunchbaseScrape' + str(((i)/200)+7) + '.csv'
        with open(fileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(yugeArray)
        fileName1 = 'newSaveFullCrunchbaseScrapeFounders' + str(((i)/200)+7) + '.csv'
        with open(fileName1, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(founderArray)
        fileName2 = 'newSaveFullCrunchbaseScrapeFunding' + str(((i)/200)+7) + '.csv'
        with open(fileName2, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(fundingArray)
    i += 1

