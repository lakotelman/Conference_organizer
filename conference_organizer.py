

import requests
from pprint import pprint
import datetime 


class Person: 
    def __init__(self, firstname, lastname, email, country, availability): 
        self.firstname = firstname
        self.lastname =lastname
        self.email = email
        self.country = country
        self.availability = availability

    def __repr__(self): 
        return f"{self.firstname} {self.lastname}"

class Conference_Org(): 
    def __init__(self): 
        self.address_book = { 
            "United States":[],
            "Ireland": [],
            "Spain": [], 
            "Mexico":[], 
            "Canada": [],
            "Singapore": [], 
            "Japan": [], 
            "United Kingdom": [], 
            "France": []
        }
#Date math is majority of work. Once dates are extracted, store those as another attriubute for the consecutive availability dates. 
#Example Person_A and Person_B are both available on June1-June2 those attributes would be comparable 
#Using counter you could determine how many people have the attribute for each date-pair. 

        api_link = "https://ct-mock-tech-assessment.herokuapp.com/"
        alldata = requests.get(api_link).json()["partners"]

        for partner in alldata:
            p = Person(
                firstname = partner["firstName"],
                lastname = partner["lastName"],
                email = partner["email"],
                country = partner["country"],
                # This is a list of datetime objects and calls function which shows its date. Datetime sucks.
                availability = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in partner["availableDates"]]
            )
            for k in self.address_book.keys(): 
                if k == p.country:
                    self.address_book[k].append(p)



#*** Getting to the Availability Lists  
# Loop through the attributes of each person in each country to find the lists of available dates 
    # address_book --> country --> person objects in the list --> availability list
#TODO Code to redesign for this task
# delta = datetime.timedelta(days=1)

# for index, days in enumerate(person2[:-1]):
#     if person2[index + 1] - person2[index] == delta:
#         tups[person1[index], person1[index+1]] = []
#         tups[person1[index], person1[index+1].append(person1)
#     else: 
#         pass

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
