#!/usr/bin/python3
''' === --- === --- === --- === --- === --- === --- === --- === --- === --- === 
csvtojson
=== --- === --- === --- === --- === --- === --- === --- === --- === --- === --- 
    created by: Arlo Gittings
    creted on: 2021-07-22
    last modified: 2021-07-22
    description:
        Tool to convert csv files into json format
=== --- === --- === --- === --- === --- === --- === --- === --- === --- === '''
from datetime import datetime as dt

def build_file_name(base, file):
    ''' build_file_name():
        description:
            genererate a file based on a base directory, file, using the
            date.
        expects:
            base:   str; the directory containing dated hierarchy
            file:   str; the uniform filename
        returns:
            fqn:    str; fully qualified path to file

    '''
    date = '/'.join(input('Date to open (YYYY-MM-DD, leave blank to use today): ').strip().split('-'))
    
    if date == '':
        date = dt.today().strftime('%Y/%m/%d')
    
    fqn = f'{base}/{date}/{file}'
    
    return fqn


        
def get_csv(csv):
    ''' get_csv:
        expects:
            csv:    str; name of csv file
        returns:
            records:    list; a list of all records in csv
    === --- === --- === --- === --- === --- === --- === --- === --- === --- ''' 
    records = []
    
    with open(csv, 'r') as fh:
        for record in fh:
            records.append(record)
    
    return records

def main():
    base_dir = '/data/data/com.termux/files/home/docs/dailies'
    csv_tasks = 'tasks.csv'
    csv_fqn = build_file_name(base_dir, csv_tasks)
    
    print(csv_fqn)
    
    records = get_csv(csv_fqn)
    json_var={}
    
    print(records, json_var)

if __name__ == '__main__':
    main()
