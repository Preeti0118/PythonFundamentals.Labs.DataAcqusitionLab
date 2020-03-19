import urllib.request
import urllib.parse
import json
import pickle

file_counter = 0
offset_counter = 1

while file_counter < 39:

    headers = {'token': ''}
    myurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&' + 'offset=' + str(offset_counter)
    request = urllib.request.Request(myurl, headers = headers)
    file_path = './locations_'+str(file_counter)+'.json'
    with urllib.request.urlopen(request) as f:
        data = json.load(f)

        with open(file_path, 'wb') as handler:
            pickle.dump(data, handler)

    file_counter = file_counter + 1
    offset_counter = offset_counter + 1000




#    with open(file_path,'wb') as handler:
#        pickle.dump(f,handler)



#request = urllib.request.Request('https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=24', headers = headers)
#weburl = urllib.request.urlopen(request)

#data = weburl.getcode()
#print(request)
#print(weburl)
#print(weburl.getcode())
#@print(weburl.read)
