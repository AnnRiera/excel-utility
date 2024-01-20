import pandas as pd
import re

main_path = '/Users/ana/Downloads'
file_path = '%s/TABLA NOMBRES PRODUCTOS - RAPV 17-07-2023.xlsx' % (main_path)
pd_file = pd.ExcelFile(file_path)
result_path = '%s/result-name-products.xlsx' % (main_path)

def combine_sheets():
    pattern = '^WM'
    
    combined_data = []
    for sheet in pd_file.sheet_names:
        if re.match(pattern, sheet):
            data_frame = pd.read_excel(file_path, sheet_name = sheet)
            combined_data.append(data_frame)
        
    result_file = pd.concat(combined_data, ignore_index = True)
    create_file(result_file)
    
def create_file(file: pd.DataFrame):
    file.to_excel(result_path, index = False)
    print('All sheets were combined to', result_path)

# def remove_duplicates():
#     try:
#         print('Removing duplicate')
        
#         data.drop_duplicates(subset=["Código", "Nombre", "Nacional o Internacional"], keep='first')
#     except Exception as error:
#         log.error("Something went wrong", error)
#         return []
    
def main():
    combine_sheets()
    #remove_duplicates()

main()