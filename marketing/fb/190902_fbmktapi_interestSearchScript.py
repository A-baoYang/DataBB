from facebook_business.api import FacebookAdsApi
from facebookads.adobjects.targetingsearch import TargetingSearch

app_id = '<YOUR_APP_ID>'
app_secret = '<YOUR_APP_SECRET>'
access_token = '<YOUR_ACCESS_TOKEN>'
api = FacebookAdsApi.init(app_id, app_secret, access_token)


def interestSearchAll(query):
    types = ['adinterest', 'adeducationschool', 'adeducationmajor', 'adworkemployer', 'adworkposition']
    ta_names = []
    
    for q in (query):
        print('---- ', q, ' ----')
        for t in types:
            print('>>>', t)
            params = {
                'q': q,
                'type': t,
                'limit': 10000,
                'locale': 'zh_TW'
            }

            resp = TargetingSearch.search(
                params=params,
                api=api
            )

            for item in resp:
                trad_cn = item['name'].encode('unicode_escape').decode('unicode_escape')
                try:
                    if item['audience_size']:
                        print(trad_cn, ': ', item['audience_size'])
                        if q in trad_cn:
                            ta_names.append((trad_cn, item['audience_size']))

                    elif item['coverage']:
                        print(trad_cn, ': ', item['coverage'])
                        if q in trad_cn:
                            ta_names.append((trad_cn, item['coverage']))

                except:
                    pass


                try:
                    if item['disambiguation_category']:
                        print('disambiguation_category: ', item['disambiguation_category'].encode('unicode_escape').decode('unicode_escape'))
                except:
                    pass

                try:
                    if item['path']:
                        for index, path in enumerate(item['path']):
                            print('path_', index, ': ', path.encode('unicode_escape').decode('unicode_escape'))
                except:
                    pass


    return ta_names
