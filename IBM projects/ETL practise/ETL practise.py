import pandas as pd
from datetime import datetime
import glob
import xml.etree.ElementTree as ET 
target_file="target_file.csv"
log_file="log_file.txt"
def extract_from_csv(csv_file):
    data=pd.read_csv(csv_file)
    return data

def extract_from_json(json_file):
    data=pd.read_json(json_file,lines=True)
    return data

def extract_from_xml(xml_file):
    dataframe=pd.DataFrame(columns=['car_model','year_of_manufacture','price','fuel'])
    parsed=ET.parse(xml_file)
    root=parsed.getroot()
    for i in root:
        car_model=i.find("car_model").text
        year_of_manufacture=int(i.find("year_of_manufacture").text)
        price=float(i.find("price").text)
        fuel=i.find("fuel").text
        data=pd.concat([dataframe,pd.DataFrame([{'car_model':car_model,'year_of_manufacture':year_of_manufacture,'price':price,'fuel':fuel}])],ignore_index=True)
    return data   
def extract():
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price','fuel'])  

    for i in glob.glob('*.csv'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(i))], ignore_index=True) 
    for i in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(i))], ignore_index=True) 
    for i in glob.glob('*.xml'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(i))], ignore_index=True)    
    return extracted_data

def transform(extracted_data):
    extracted_data['price']=round(extracted_data.price,2)
    return extracted_data

def load(extracted_data,target_file):
    extracted_data.to_csv(target_file)
    
def log_process(message):
    time_format="%y-%m-%d-%H-%M-%S"
    now=datetime.now()
    time_stapm=now.strftime(time_format)
    with open(log_file,"a") as log:
        log.write(time_stapm +" : " +message +"\n")
        
log_process("ETL process started")

log_process("extract proces started")
extract()
log_process("extract proces ended")

log_process("transform proces started")
extracted_data=extract()
transform(extracted_data)
log_process("transform proces ended")

transformed=transform(extracted_data)
print(transformed)

log_process("load process started")
load(extracted_data,target_file)
log_process("load process ended")

log_process("ETL process ended")