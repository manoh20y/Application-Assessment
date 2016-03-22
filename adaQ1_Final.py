import csv
file_handle = open('SE.csv')

data = csv.reader(file_handle)

i = 0
for element in data:
    if i > 5: break
    print element
    i += 1

result = []#list of entries in WA state, that were not about storms, in counties that dont have names starting with a vowel.

for row in data:
    if row[8] == 'WASHINGTON' and row[15][0] not in ['A','E','I','O','U']: #row[8] is State name column and row[15][0] is starting letter of county name.
        result.append(row)
print len(result) #211 WA storm event entries.

county_events = []

for event in result:
    if event[13] in ['C']:
        county_events.append(event)
print len(county_events) #50 county storm events registered.

county_names = []

for name in county_events:
    county_names.append(name[15])
print county_names
print len(county_names) # 50- check to makes sure it matches county_events

unique_counties = []

for name in county_names:
    if name not in unique_counties:
        unique_counties.append(name)
print len(unique_counties) #21 discrete counties
print unique_counties

zone_events = []

for r in result:
    if r[13] in 'Z':
        zone_events.append(r)
print len(zone_events) #161 zone events registered

zone_names = []

for zone_event in zone_events:
    zone_names.append(zone_event[15])
print len(zone_names) #161 names
print zone_names[:5]

unique_zones = []

for zone in zone_names:
    if zone not in unique_zones:
        unique_zones.append(zone)
print unique_zones[:5]
print len(unique_zones) #32 unique zones
# 18 counties were storm free in 2007 in WA State.
#To find absolute number of storm hit counties, we need to access a database that correlates zones to counties.
# Here "storm free" means counties that had no events registered in the Storm Events Database in 2007.
#The distinction between actual storm weather and other registered weather (like Wildfires/Drought) is not made.
# All events registered are considered "storms".
