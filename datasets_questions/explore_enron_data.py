#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# 1
print len(enron_data)

# 2
print len(enron_data["SKILLING JEFFREY K"])

# 3
pois = [x for x, y in enron_data.items() if y['poi']]
print 'Number of POI\'s: {0}'.format(len(pois))

# 4
print sum(1 for line in open('../final_project/poi_names.txt'))


# 5
print enron_data['PRENTICE JAMES']['total_stock_value']

# 6
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

# 7
print enron_data['SKILLING JEFFREY K']['exercised_stock_options'] 

# 8
names = ['SKILLING JEFFREY K', 'FASTOW ANDREW S', 'LAY KENNETH L']
names_payments = {name:enron_data[name]['total_payments'] for name in names}
print sorted(names_payments.items(), key=lambda x: x[1], reverse=True)


# 9
df = pd.DataFrame(enron_data)
print 'Has salary data: {0}'.format(sum(df.loc['salary',:] != 'NaN'))
print 'Has email: {0}'.format(sum(df.loc['email_address',:] != 'NaN'))




isnan = sum(df.loc['total_payments',:]=='NaN')
_,cols = df.shape
print 'total_payments == \'NaN\': {0} people = {1:.2f}%'.format(isnan, 100.*isnan/cols)