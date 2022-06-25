

import requests
from pprint import pprint
import datetime 
from collections import Counter

class DisplayData: 
    def __init__(self, attendeeCount, attendees, name, startDate):
        self.attendeeCount = attendeeCount
        self.attendees = attendees
        self.name = name 
        self.startDate = startDate

    def __repr__(self):
        return f"{self.name}"

class Person: 
    def __init__(self, firstname, lastname, email, country, availability, start_days): 
        self.firstname = firstname
        self.lastname =lastname
        self.email = email
        self.country = country
        self.availability = availability
        self.start_days = start_days

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
                # This is a list of datetime objects and calls function which shows its date. Datetime sucks.
                availability = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in partner["availableDates"]],
                start_days = []
            )
            
            delta = datetime.timedelta(days=1)
            for index, days in enumerate(p.availability[:-1]):
                if p.availability[index + 1] - p.availability[index] == delta:
                    p.start_days.append(p.availability[index])
            else: 
                pass
           
            for k in self.address_book.keys(): 
                if k == p.country:
                    self.address_book[k].append(p)

    def find_common_start_dates(self):
        self.start_days_by_country = { 
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
        
        for country, person in self.address_book.items():
            for person in self.address_book[country]:
                self.start_days_by_country[country].extend(person.start_days)

        self.start_day_list = []
        for country, dates in self.start_days_by_country.items(): 
            display_start_day = max(Counter(self.start_days_by_country[country]), key=Counter(self.start_days_by_country[country]).get)
            self.start_day_list.append((country, display_start_day))

        self.all_countries = []
        for country, persons_list in self.address_book.items(): 
            display_start_date= None
            display_attendees = []
            for person in persons_list:
                for tup in self.start_day_list: 
                    if person.country == tup[0]: 
                        display_start_date = str(tup[1])
                        if tup[1] in person.start_days:
                            if person.email not in display_attendees:
                                display_attendees.append(person.email)
            d = DisplayData(

                attendeeCount = len(display_attendees),
                attendees = display_attendees,
                name = country,
                startDate = display_start_date
            )
            self.all_countries.append(d)


trial_1 = Conference_Org()
trial_1.find_common_start_dates()
payload = {"data": [d.__dict__ for d in trial_1.all_countries]}


url = "https://ct-mock-tech-assessment.herokuapp.com/"
x = requests.post(url, json = payload)
print(x.text)














