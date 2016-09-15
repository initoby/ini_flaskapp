from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from geopy.geocoders import Nominatim
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def yelp_lookup(address,search_term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )

    client = Client(auth)

    params = {
        'term': search_term,
        'lang': 'en',
        'limit': 3
    }

    response = client.search(address, **params)
    
    businesses= []

    for business in response.businesses:
        # print(business.name, business.rating, business.phone)
        businesses.append({"business": business.name,  
            "phone": business.display_phone,
            "address": business.location.display_address
        })

    return businesses

#businesses = get_businesses('New York City', 'food')

#print(businesses)

