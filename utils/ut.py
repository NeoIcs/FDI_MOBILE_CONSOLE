import csv
import json

class Utils():
    def __init__(self):
        pass

    @staticmethod
    def get_json_file(json_file =None):
        data = 'load data fail'
        with open('./FDI_MOBILE_CONSOLE/utils/index.json') as f:
             data = json.load(f)

        return data