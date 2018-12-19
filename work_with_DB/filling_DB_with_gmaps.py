# -*- coding: utf-8 -*-

from bd_interaction import *

file = ('tables.txt')
bd = bd_interaction('good-coffee-near-you.cgcnnlvq1rjd.us-east-1.rds.amazonaws.com',
                               'barista', 'good0afternoon', 'CoffeHouses', 1, file)

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
        CoffeeHouseId = place.place_id
        bd.tables['TotalRating'].insert(colomns=['CoffeeHouseId', 'TotalRating', 'RatingCount'],
                                        values=[CoffeeHouseId, place.rating, 100])
        bd.tables['Address'].insert(colomns=['CoffeeHouseId', 'Address', 'Latitude', 'Longitude'],
                                    values=[CoffeeHouseId, place.formatted_address,
                                            place.geo_location['lan'], place.geo_location['lng']])
        AddressId = bd.tables['Address'].query("SELECT LAST_INSERT_ID();")
        for day, time in place.opening_hours.open:
            opening, closing = [t+'00' for t in time.split('-')]
            bd.tables['WorkingTime'].insert(colomns=['CoffeeHouseId', 'DayOfWeek',
                                                     'OpeningHour', 'ClosingHour'],
                                            values=[CoffeeHouseId, day, opening, closing])
        bd.tables['CoffeeHouse'].insert(colomns=['CoffeeHouseId', 'Name', 'AddressId',
                                                 'Website', 'HasFoodToGo'],
                                        values=[CoffeeHouseId, place.name, AddressId
                                                place.geo_location['lan'],
                                                place.geo_location['lng']])
    if query_result.has_next_page_token:
        data_processing(google_places.nearby_search(pagetoken=query_result.next_page_token), i)
        
        
query_result = google_places.nearby_search(
        location='Санкт-Петербург, Россия', keyword='кофе с собой', 
        language='ru', radius=3200, types=['cafe'])

data_processing(query_result)


