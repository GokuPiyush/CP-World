import requests
from urllib.parse import urlencode
import json
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim


def get_users():
    print("Fetching data from Codeforces...")
    method = "user.ratedList"
    endpoint = f"https://codeforces.com/api/{method}"
    params = {'activeOnly': True}
    url = f"{endpoint}?{urlencode(params)}"
    
    try: 
        res = requests.get(url)
        if res.status_code in range(200, 299):
            data = res.json()['result']
            print('Finished fetching..')
            return data
    except:
            print("Oops! Error occured while fetching data from codeforces..")
    return []

def build(ranks, file='data.json'):
    data = get_users()
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    
    with open(file) as data:
        programmers = json.load(data)
        if len(programmers) == 0:
            print('Nothing to Geocode..')
            return
        li = []
        print('...Geocoding started...')
        for programmer in programmers:
            if programmer['rank'] not in ranks:
                continue
            city, country = programmer.get('country'), programmer.get('city')
            address = ((city + ", ") if city is not None else "") + (country if country is not None else "")
            if address != "":
                print('Geocoding' + ' ' + programmer['handle'] + ' ' + 'address..')
                try:
                    geolocator = Nominatim(user_agent="http")
                    location = geolocator.geocode(address)
                    li.append({
                        **programmer,
                        'location': { 'latitude': location.latitude, 'longitude': location.longitude }
                    })
                except:
                    print(f"Oops! Error occured while fetching {programmer['handle']} location..")
        with open(file, 'w') as f:
            f.write(json.dumps(li, indent = 4))
        print('...Geocoding finished...')
    plot(ranks, file)

def plot(ranks, file='./data_extracts/data.json'):
    color = {
        'legendary grandmaster': 'r',
        'international grandmaster': 'r',
        'grandmaster': 'r',
        'international master': 'y',
        'master': 'y',
        'candidate master': 'm',
        'expert': 'b',
        'specialist': 'c',
        'pupil': 'g',
        'newbie': 'w'
    }
    programmers = []
    with open(file) as data:
        programmers = json.load(data)
        # print(len(programmers))
    if len(programmers) == 0:
        print("Nothing to plot..")
        return

    m = Basemap(projection='robin',lon_0=0,resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    # m.drawstates()

    print('Plotting data...')
    for programmer in programmers:
        if programmer['rank'] not in ranks:
            continue
        x, y = m(programmer['location']['longitude'], programmer['location']['latitude'])
        m.plot(x,y, color=color[programmer['rank']], marker='x', label=programmer['rank'])
        
    print('Plotting finished...')
    plt.title("Competitive Programming World!")
    # plt.legend()
    plt.show()

while(True):
    command = input("Input command: ").lower()
    if command == 'exit':
        break
    initials = {
        'lg': 'legendary grandmaster', 
        'ig': 'international grandmaster', 
        'g': 'grandmaster', 
        'im': 'international master', 
        'm': 'master', 
        'cm': 'candidate master', 
        'e': 'expert', 
        's': 'specialist', 
        'p': 'pupil', 
        'n': 'newbie'
    }
    if len(command.split()) >= 2:
        command, *ranks = command.split()
        if(command == 'build' or command == 'plot'):
            li = []
            for rank in ranks:
                if rank in initials:
                    li.append(initials[rank])
                else:
                    print("Rank initials didn't match..")
                    break
            else:
                eval(command+'(li)')
        else:
            print('Bad parameters!')
    else:
        print('Bad parameters!')
