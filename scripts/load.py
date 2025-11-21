
import mysql.connector as mysql
from transfor import tranform_data

def connect_to_db():
    (city,longitude,latitude,temperature,min_temp,max_temp, humidity, pressure, wind_speed,
     weather_description, date)=tranform_data()
    try:
        db=mysql.connect(host='localhost',
                         user='root',
                         password='1234',
                         database='Weather_Data')
        print(f'Successfully connected to database')
    except Error as e:
        print(f"Connection Failed !! {e}")

    cursor=db.cursor()

    # DESIGN TABLES

    city_table=f"""CREATE TABLE IF NOT EXISTS CITY(city_id int auto_increment PRIMARY KEY,
            city_name varchar(255) NOT NULL UNIQUE,
            longitude FLOAT NOT NULL,
             latitude FLOAT NOT NULL);"""
    cursor.execute(city_table)


    weather_table=f""" CREATE TABLE IF NOT EXISTS WeatherType(weather_type_id int auto_increment PRIMARY KEY,
                                                              discription varchar(255) NOT NULL UNIQUE);"""
    cursor.execute(weather_table)

    weather = f""" CREATE TABLE  IF NOT EXISTS Weather (
       weather_id INT AUTO_INCREMENT PRIMARY KEY,
       city_id INT NOT NULL,
       weather_type_id INT NOT NULL,
       date DATE NOT NULL,
       temp_min FLOAT,
       temp_max FLOAT,
       temp_avg FLOAT,
       humidity FLOAT,
       pressure FLOAT,
       wind_speed FLOAT,
       FOREIGN KEY (city_id) REFERENCES City(city_id),
       FOREIGN KEY (weather_type_id) REFERENCES WeatherType(weather_type_id));"""

    cursor.execute(weather)
    db.commit()


    #LOAD
    ins_city_table = """ INSERT IGNORE INTO CITY(city_name,longitude,latitude)Values ( %s,%s, %s)"""
    c_data = (city, longitude, latitude)
    cursor.execute(ins_city_table, c_data)
    db.commit()

    q = f"""SELECT CITY_ID FROM CITY WHERE CITY_NAME= %s LIMIT 1;"""
    cursor.execute(q, (city,))
    city_id = cursor.fetchone()[0]


    inst_weather_type = """ INSERT IGNORE INTO WeatherType (discription) Values (%s)"""
    cursor.execute(inst_weather_type, (weather_description,))
    db.commit()

    w = """SELECT Weather_type_id from WeatherType WHERE discription=%s LIMIT 1;"""
    cursor.execute(w, (weather_description,))
    weather_type_id = cursor.fetchone()[0]




    inst_weather="""INSERT INTO WEATHER(city_id,weather_type_id,date,temp_min, temp_max,temp_avg,humidity,pressure,wind_speed)
                     VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    temp_avg=(min_temp+max_temp)/2
    wd=(city_id,weather_type_id,date,min_temp,max_temp,temp_avg, humidity, pressure, wind_speed)
    cursor.execute(inst_weather,wd)
    db.commit()



