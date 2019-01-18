import pandas as pd
import csv
import time

ct = time.time()
#
cols = ['device', 'geoNetwork', 'totals', 'trafficSource']
filepath = "/Users/abhaysinghal/Documents/Kaggle/Revenue/train.csv"
train = pd.read_csv(filepath, dtype=str)
#
# fields = {}
#

print("Read file")
print(time.time() - ct)
ct = time.time()

fields = ['browser', 'browserVersion', 'browserSize', 'operatingSystem', 'operatingSystemVersion', 'isMobile',
          'mobileDeviceBranding',
          'mobileDeviceModel', 'mobileInputSelector', 'mobileDeviceInfo', 'mobileDeviceMarketingName', 'flashVersion',
          'language',
          'screenColors', 'screenResolution', 'deviceCategory', 'continent', 'subContinent', 'country', 'region',
          'metro', 'city',
          'cityId', 'networkDomain', 'latitude', 'longitude', 'networkLocation', 'MA', 'IA', 'visits', 'hits',
          'pageviews',
          'bounces', 'newVisits', 'transactionRevenue', 'campaign', 'source', 'medium', 'keyword', 'adwordsClickInfo',
          'isTrueDirect',
          'referralPath', 'slot', 'criteriaParameters', 'gclId', 'adNetworkType', 'isVideoAd']

nrows = train.shape[0]
data = {}

for f in fields:
    data[f] = []
    for i in range(nrows):
        data[f].append(None)

# df = pd.DataFrame(columns=fields, index=range(1, len(train.index)))

print("Made Dataframe")
print(time.time() - ct)
ct = time.time()

for key in cols:
    # f = []
    i = 0
    for row in train[key]:
        row = row.replace('{', '')
        row = row.replace('}', '')
        row = row.replace('"', '')
        line = row.split(',')
        for string in line:
            strings = string.split(':')
            strings[0] = strings[0].replace(' ', '')
            # print(fields.__contains__(string[0]))
            # df.loc[i, string[0]] = string[1]
            if fields.__contains__(strings[0]) and len(strings) > 1:
                data[strings[0]][i] = strings[1]
        if int(i % (nrows/100)) == 0:
            print(int(100*i/nrows))
        i += 1
    print("Done with " + key)
    print(time.time() - ct)
    ct = time.time()
    # if not f.__contains__(string[0]):
    # f.append(string[0])
    # fields[key] = f
#
# with open('fields.txt', 'w+') as file:
#     file.write(str(fields))

df = pd.DataFrame.from_dict(data, orient='index').transpose()
train = train.drop(columns = cols)
df = pd.concat([df, train], axis=1)

print("Concatenated datasets")

df.to_csv('/Users/abhaysinghal/Documents/Kaggle/Revenue/features.csv', index = False)

print(time.time() - ct)

# print(fields)
