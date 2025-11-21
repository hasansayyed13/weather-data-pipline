from extract import fetch_data
from transfor import tranform_data
from load import connect_to_db



if __name__ == '__main__':
    city_name = list(map(str.strip,input("Enter the city names into comma sep (eg:Delhi,Mumbai,Valsad):").split(',')))
    data=fetch_data(city_name)
    data=tranform_data(data)
    connect_to_db(data)
