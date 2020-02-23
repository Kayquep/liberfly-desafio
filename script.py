import numpy as np
import pandas as pd

data = pd.read_csv('customers.csv')
data['birthdate'] = pd.to_datetime(data.birthdate)
data['birthdate'] = data['birthdate'].dt.strftime('%d/%m/%Y')
data['domain'] = "https://" + data["domain"].map(str)
data['full_name'] = np.nan
data['full_name'] = data["first_name"].map(str)+" "+ data["last_name"].map(str)
data = data[['id', 'first_name', 'last_name','full_name','email', 'gender', 'phone', 'birthdate', 'domain']]
data['phone'] = data['phone'].str.replace('\W', '')
data['phone']= data['phone'].astype(str).apply(lambda x: '('+x[:2]+')'+x[2:6]+'-'+x[6:10])
data.to_csv('customers_updated.csv', index = None)