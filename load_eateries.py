import json
# import your db module
import db
from sqlalchemy.orm import sessionmaker
# create a dsn using one of your module's functions
dsn = db.generate_dsn('config.json')
# create a session using one of your module's functions
created_session = db.get_session(dsn)
# loop through your json data, and instantiate a new eatery using your class… and save each eatery into a list
eateries_list = []
with open('DPR_Eateries_001.json', 'r') as fp: 
    data = json.load(fp)
    # print(data)
fp.close()
for key in data: 
    # instantiate a new eatery 
    eatery = db.Eatery()
    for k in key.items(): 
        if k[0] == "name": 
            eatery.name = k[1]
        elif k[0] == "location": 
            eatery.location = k[1]
        elif k[0] == "park_id": 
            eatery.park_id = k[1] 
        elif k[0] == "start_date": 
            eatery.start_date = k[1]
        elif k[0] == "end_date": 
            eatery.end_date = k[1]
        elif k[0] == "description": 
            eatery.description = k[1]
        elif k[0] == "permit_number": 
            eatery.permit_number = k[1]
        elif k[0] == "phone": 
            eatery.phone = k[1]
        elif k[0] == "website": 
            eatery.website = k[1]
        elif k[0] == "type_name": 
            eatery.type_name = k[1]
    # add the instance to the list of instances
    eateries_list.append(eatery)
# use the session method, add_all to add all instances
created_session.add_all(eateries_list)
# make sure to commit afterwards
eateries_list.commit(); 

print(eateries_list)


