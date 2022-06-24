

import requests
from pprint import pprint


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

        api_link = "https://ct-mock-tech-assessment.herokuapp.com/"
        alldata = requests.get(api_link).json()["partners"]

        for partner in alldata:
            p = Person(
                firstname = partner["firstName"],
                lastname = partner["lastName"],
                email = partner["email"],
                country = partner["country"],
                availability = partner["availableDates"]
            )
            for k in self.address_book.keys(): 
                if k == p.country:
                    self.address_book[k].append(p)

                




