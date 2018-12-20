# -*- coding: utf-8 -*-

from bd_interaction import *

file = ('tables.txt')
bd = bd_interaction('good-coffee-near-you.cgcnnlvq1rjd.us-east-1.rds.amazonaws.com',
                               'barista', 'good0afternoon', 'good-coffee-near-you', 1, file)

from googleplaces import GooglePlaces, types, lang
google_places = GooglePlaces('AIzaSyAjyUT_utIGfYkUNsbwwUQAjOZidif-DGk')

#search_ways = {'coffee':'en', 'кофе с собой':'ru', 'кофейня':'ru', 'кофе':'ru'}
#city = {'ru':'Санкт-Петербург, Россия', 'en':'Saint-Petersburg, Russia'}
#for key in search_ways:
#    query_result = google_places.nearby_search(
#        location=city[search_ways[key]], keyword=key, language=search_ways[key],
#        radius=20000, types=['cafe'])
#    if query_result.has_attributions:
#        print(query_result.html_attributions)
#    for place in query_result.places:
#        # Returned places from a query are place summaries.
#        print(place.name, place.geo_location, place.place_id)
#        # The following method has to make a further API call.
#        place.get_details()
#        # Referencing any of the attributes below, prior to making a call to
#        # get_details() will raise a googleplaces.GooglePlacesAttributeError.
#        print(place.details)# A dict matching the JSON response from Google.
#        print(place.local_phone_number)
#        print(place.international_phone_number)
#        print(place.website)
#        print(place.url)
#    # Are there any additional pages of results?
#    if query_result.has_next_page_token:
#        print("query_result_next_page = ", google_places.nearby_search(
#            pagetoken=query_result.next_page_token))

def data_processing(query_result, i=0):
    for place in query_result.places:
        place.get_details()
        coffee_house_id = place.place_id
        for coffee_id in range(1,4):
            bd.tables['coffee_house_menu'].insert(colomns=['coffee_house_id', 'coffee_id',
                                                           'total_rating', 'rating_count'],
                                                  values=[coffee_house_id, coffee_id, place.rating, 100])
        #+coffee_house_address
        address_id = bd.tables['coffee_house_address'].query("SELECT LAST_INSERT_ID();")
        bd.tables['address'].insert(colomns=['address_id','adress', 'latitude', 'longitude'],
                                    values=[address_id, place.formatted_address,
                                            place.geo_location['lan'], place.geo_location['lng']])#!!! 
        for day, time in place.opening_hours.open:
            opening, closing = [t+'00' for t in time.split('-')]
            bd.tables['working_time'].insert(colomns=['coffee_house_id', 'day_of_week',
                                                     'opening_hour', 'closing_hour'],
                                            values=[coffee_house_id, day, opening, closing])
        bd.tables['coffee_house'].insert(colomns=['coffee_house_id', 'name', 'address_id',
                                                 'website', 'has_food_to_go'],
                                        values=[coffee_house_id, place.name, address_id
                                                place.website, any(place.website))
    if query_result.has_next_page_token:
        data_processing(google_places.nearby_search(pagetoken=query_result.next_page_token), i)
        
        
query_result = google_places.nearby_search(
        location='Санкт-Петербург, Россия', keyword='кофе с собой', 
        language='ru', radius=20000, types=['cafe'])

data_processing(query_result)


