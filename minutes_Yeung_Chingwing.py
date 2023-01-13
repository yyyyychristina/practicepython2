"""
Program: minutes_lastname_firstname.py


Compute the number of minutes in a year.

Useful facts:
   1 year = 365 days (we ignore leap years)
   1 day = 24 hours
   1 hour = 60 minutes

"""
#input
years = int(input('years:'))


#output
days = years * 365
print('days:', days)

hours = days * 24
print('hours:', hours)

no_of_minutes_in_a_year = hours * 60
print('no of minutes in a year:', no_of_minutes_in_a_year)
