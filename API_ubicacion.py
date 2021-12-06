import requests
import pandas as pd


data=pd.read_csv('/Users/richardgil/Documents/BGSE/Datawarehouse/Final Project/data_finalp/household.csv')

data.head()
def get_info_adress(data):
    #Params:
    #@data: dataframe with the information of latitude and longitude from each family
    base_url='https://nominatim.openstreetmap.org/reverse?'
    status_code_ls=[]
    amenity_ls=[]
    road_ls=[]
    city_ls=[]
    region_ls=[]
    state_ls=[]
    for i in range(0,data.shape[0]):
        print(i)
        params={'format':'json','lat':data['latitud'][i],'lon':data['longitud'][i]}
        result=requests.get(base_url,params=params)
        status_code_ls.append(result.status_code)
        try:
            road_ls.append(result.json()['address']['road'])
        except: 
            road_ls.append(None)
        try:
            city_ls.append(result.json()['address']['city'])
        except:
            city_ls.append(None)
        try:
            region_ls.append(result.json()['address']['region'])
        except: 
            region_ls.append(None)
        try:
            state_ls.append(result.json()['address']['state'])
        except:
            state_ls.append(None)

    contact_data=pd.DataFrame()
    contact_data['longitud']=data['longitud']
    contact_data['latitud']=data['latitud']
    contact_data['status_code']=status_code_ls
    contact_data['road']=road_ls
    contact_data['city']=city_ls
    contact_data['region']=region_ls
    contact_data['state']=state_ls

    return contact_data


contact_info=get_info_adress(data)
contact_info.head()
contact_info.to_csv('/Users/richardgil/Documents/BGSE/Datawarehouse/Final Project/data_finalp/addresses.csv',index=False,sep=',')

