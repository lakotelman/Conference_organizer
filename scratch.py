

#*** Getting to the Availability Lists  
# Loop through the attributes of each person in each country to find the lists of available dates 
    # address_book --> country --> person objects in the list --> start_days
#TODO Code to redesign for this task

#*** Finding and storing the Date-Pairs (maybe populating attendees as well?) 
#  Date-Pairs-By-Country: { 
#            "United States": {(date-pair): [person objects who have this availability]
#                              (date-pair): [person objects who have this availability]}
#           "United Kingdom": {(date-pair): [person objects who have this availability]
#                              (date-pair): [person objects who have this availability]}
#                           }
#Alternatively we could set the consecutive dates as another attribute within the Person Class-Object
# From these lists we construct a dictionary of date-pairs in the lists (organized by country)
    # UK --> {opt1: [], opt: []} (We would need to make sure these tuples for the date-pairs are not added multiple times)
# I wonder if there is a way to add the person to the list at the same time as constructing the key and value? 

#*** Picking the right date-pair for each country and constructing the Post Request
# Compare the lengths of the lists to determine which date pair contains the most partners in each country
# Construct a dictionary from this information with start date, country, and attendees emails
# Do something to check it with the API?

{"data" : [ { "attendeeCount": 1,
            "attendees": [
                "email",
            ],
            "name": "country",
            "startDate": "string date",
}



]
}