import pandas as pd

df = pd.read_csv("newSaveFullCrunchbaseScrapeFinal.csv")
facebook_column = df.facebook #you can also use df['column_name']
twitter_column = df.twitter 
link_column = df.linkedin
print(facebook_column[0])
print(twitter_column[0])
print(link_column[12])

maxlen = 0
if (len(facebook_column) > len(twitter_column) and len(facebook_column) > len(link_column)):
    maxlen = len(facebook_column)

if (len(twitter_column) > len(facebook_column) and len(twitter_column) > len(link_column)):
    maxlen = len(twitter_column)

if (len(link_column) > len(twitter_column) and len(link_column) > len(facebook_column)):
    maxlen = len(link_column)

i = 0
maxlen = 6222
t = type(12.0)
newFB = []
newT = []
newLI = []

while (i < maxlen):
    faceTemp = ""
    twitTemp = ""
    linkTemp = ""

    if (type(facebook_column[i]) != t):
        if ("facebook" in facebook_column[i]):
            faceTemp = facebook_column[i]

    if (type(twitter_column[i]) != t):
        if ("facebook" in twitter_column[i]):
            faceTemp = twitter_column[i]
    if (type(link_column[i]) != t):
        if ("facebook" in link_column[i]):
            faceTemp = link_column[i]

    if (type(twitter_column[i]) != t):
        if ("twitter" in twitter_column[i]):
            twitTemp = twitter_column[i]

    if (type(facebook_column[i]) != t):
        if ("twitter" in facebook_column[i]):
            twitTemp = facebook_column[i]
    if (type(link_column[i]) != t):
        if ("twitter" in link_column[i]):
            twitTemp = link_column[i]

    if (type(link_column[i]) != t):
        if ("linkedin" in link_column[i]):
            linkTemp = link_column[i]
        
    if (type(facebook_column[i]) != t):
        if ("linkedin" in facebook_column[i]):
            linkTemp = facebook_column[i]
    if (type(twitter_column[i]) != t):
        if ("linkedin" in twitter_column[i]):
            linkTemp = twitter_column[i]

        
    newFB.append(faceTemp)
    newT.append(twitTemp)
    newLI.append(linkTemp)

    i = i + 1


d = {'facebook': newFB, 'twitter': newT, 'linkedin': newLI}
df = pd.DataFrame(data=d)
df.to_csv("pandasExport.csv", encoding='utf-8', index=False)