import re
import pandas as pd
from config import config

pd_file = pd.ExcelFile(config.SOURCE_FILE)

def combine_sheets():
    combined_data = []
    for sheet in pd_file.sheet_names:
        if re.match(config.REGEX_PATTERN, sheet):
            data_frame = pd.read_excel(config.SOURCE_FILE, sheet_name = sheet, usecols='A:C')
            combined_data.append(data_frame)
        
    result_file = pd.concat(combined_data, ignore_index = True)
    create_file(result_file)

def create_file(file: pd.DataFrame):
    file.to_excel(config.TARGET_FILE, index = False)
    print('All sheets were combined to', config.TARGET_FILE)

def remove_duplicates():
    try:
        data = pd.read_excel(config.TARGET_FILE)
        data.drop_duplicates(keep="first", inplace=True)
        print('All duplicate rows were removed.')
    except Exception as error:
        print("Something went wrong", error)
        return []
    
def main():
    combine_sheets()
    remove_duplicates()

main()