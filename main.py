from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
import config
from twilio.rest import Client
from read_data import read_data
import geocoder
from rtree import index

app = FastAPI()

def find_k_nearest_hospitals(hospitals, k, latitude, longitude):
    p = index.Property()
    p.dimension = 2  # Two-dimensional index
    idx = index.Index(properties=p)

    # Build the R-tree index
    for i, hospital in enumerate(hospitals):
        hospital_lat = hospital['lat']
        hospital_lon = hospital['lon']
        idx.insert(i, (hospital_lon, hospital_lat, hospital_lon, hospital_lat), obj=hospital)

    # Perform the k-nearest neighbor search
    nearest_hospitals = list(idx.nearest((longitude, latitude, longitude, latitude), k))

    # Extract the hospitals from the index results
    nearest_hospitals = [hospitals[i] for i in nearest_hospitals]

    return nearest_hospitals

# Mock function to get location details
def get_location_details(latitude: float, longitude: float):

    data = read_data()
    nearest_hospitals = find_k_nearest_hospitals(data, 10, latitude=latitude, longitude=longitude)

    list_of_hospitals = []
    for hospital in nearest_hospitals:
        list_of_hospitals.append({'block_name' : hospital['block_name'], 
                                'taluka_name' : hospital['taluka_name'],
                                'district_name' : hospital['district_name'],
                                'contact' : hospital['contact']
                                })

    return list_of_hospitals

class LocationRequest(BaseModel):
    def location(self):
        g = geocoder.ip('me').latlng
        return (g[0], g[1])
        #return (29.8615080, 77.8939737)

class LocationResponse(BaseModel):
    locations: list[str]

def send_sms(contact):
    client = Client(config.account_sid, config.auth_token)
    # sending message
    message = client.messages.create(body='Hi there! Message from Hospital Project! Happy Learning :)', from_= config.FROM_NUM, to=contact)


@app.get("/get_locations")
async def get_locations(lat:Union[float,None]=None , lon : Union[float,None]=None):
    latitude = 0.0
    longitude = 0.0
    if lat is None or lon is None:
        location = LocationRequest()
        (latitude, longitude) = location.location()
    else:
        latitude = lat
        longitude = lon

    # Call the predefined function to get location details
    location_details = get_location_details(latitude, longitude)
    contact = '+91' + str(location_details[0]['contact'])
    print("Message Sent to the Hospital!!")
    send_sms(contact)
    try:
        print('try running...')
        return location_details
    except:
        print('except running...')
        return location_details
    # return location_details
