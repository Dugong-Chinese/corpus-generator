import json
import csv
import traceback


def json2csv(json_file_handle, csv_file_handle):
    """Simply converts the words item into a csv for easier viewing"""
    json_file_handle.seek(0)
    _json = json_file_handle.read()
    try:
        data = json.loads(_json)
        csv_file_handle.seek(0)
        csv_file_handle.truncate()
        w = csv.writer(csv_file_handle, delimiter=',',
                       quotechar='"', quoting=csv.QUOTE_MINIMAL)
        w.writerow(data['words'][0].keys())
        for word in data['words']:
            w.writerow(word.values())

    except:
        traceback.print_exc()
