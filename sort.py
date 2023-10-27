import os
import shutil
from datetime import datetime

SOURCE_DIRECTORY = '/Users/damientanneau/Desktop/test'

def get_year_month(filename):
    modification_time = os.path.getmtime(filename)
    modification_date = datetime.fromtimestamp(modification_time)
    year = modification_date.year
    month = str(modification_date.month)
    return year, month


for root, _, files in os.walk(SOURCE_DIRECTORY):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path):
            year, month = get_year_month(file_path)
            target_folder = os.path.join(SOURCE_DIRECTORY, f"{year}_{month.zfill(2)}")
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, os.path.join(target_folder, file))
