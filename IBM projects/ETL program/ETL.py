import glob 
import pandas as pd 
import xml.etree.ElementTree as ET 
from datetime import datetime 
log_file = "log_file.txt" 
target_file = "transformed_data.csv" 
 
def extract_from_csv(csv_file):
    data=pd.read_csv(csv_file)
    return data

def extract_from_json(json_file):
    data=pd.read_json(json_file,lines=True)
    return data

def extract_from_xml(xml_file):
    data_frame=pd.DataFrame(columns=['name','height','weight'])
    parsed=ET.parse(xml_file)
    root=parsed.getroot()
    for i in root:
        name=i.find("name").text
        height=float(i.find("height").text)
        weight=float(i.find("weight").text)
        data=pd.concat([data_frame,pd.DataFrame([{'name':name,'height':height,'weight':weight}])],ignore_index=True)
    return data
def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight'])  

    for i in glob.glob('*.csv'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(i))], ignore_index=True) 
    for i in glob.glob('*.json'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(i))], ignore_index=True) 
    for i in glob.glob('*.xml'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(i))], ignore_index=True)    
    return extracted_data
def transform(data):
    data['height']=round(data.height*0.0254,2)
    data['weight']=round(data.weight* 0.45359237,2)
    return data

def load(target_file,transformed_data):
    transformed_data.to_csv(target_file)
 
def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open(log_file,"a") as f: 
      f.write(timestamp + ',' + message + '\n') 
    
# Log the initialization of the ETL process 
log("ETL Job Started") 
  
# Log the beginning of the Extraction process 
log("Extract phase Started") 
extracted_data = extract() 
  
# Log the completion of the Extraction process 
log("Extract phase Ended") 
  
# Log the beginning of the Transformation process 
log("Transform phase Started") 
transformed_data = transform(extracted_data) 
print("Transformed Data") 
print(transformed_data) 
  
# Log the completion of the Transformation process 
log("Transform phase Ended") 
  
# Log the beginning of the Loading process 
log("Load phase Started") 
load(target_file,transformed_data) 
  
# Log the completion of the Loading process 
log("Load phase Ended") 
  
# Log the completion of the ETL process 
log("ETL Job Ended") 