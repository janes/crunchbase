
import requests
import csv
import sys
reload(sys)

sys.setdefaultencoding('utf8')

url13 = "https://api.crunchbase.com/v3.1/" + '/organizations/facebook/funding_rounds/' + "?user_key=188fa1875a4cf6c62d23c98e9afb01ed"
response123 = requests.get(url13)
fundingData = response123.json()

numberOfFunding = fundingData['data']['paging']['total_items'] - 1
i123 = 0
while (i123 < numberOfFunding):
    print(fundingData['data']['items'][i123]['relationships']['investments'][0]['type'])

    print(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['type'])
    try:
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['investor_type'])
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['founded_on'])
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['short_description'])
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['total_funding_usd'])
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['relationships']['investors']['properties']['number_of_investments'])


        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['money_invested_usd'])
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['announced_on'])
        print(fundingData['data']['items'][i123]['relationships']['investments'][0]['properties']['is_lead_investor'])
    except:
        print(1)
    print(fundingData['data']['items'][i123]['type'])

    print(fundingData['data']['items'][i123]['properties']['series'])
    print(fundingData['data']['items'][i123]['properties']['rank'])
    print(fundingData['data']['items'][i123]['properties']['pre_money_valuation'])
    print(fundingData['data']['items'][i123]['properties']['money_raised_usd'])
    print(fundingData['data']['items'][i123]['properties']['pre_money_valuation_usd'])
    print(fundingData['data']['items'][i123]['properties']['money_raised'])
    print(fundingData['data']['items'][i123]['properties']['updated_at'])
    print(fundingData['data']['items'][i123]['properties']['target_money_raised_usd'])
    print(fundingData['data']['items'][i123]['properties']['announced_on'])
    i123 += 1
