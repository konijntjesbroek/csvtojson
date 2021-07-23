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
def get_header(h):
    return [f.strip() for f in h.split(',')]

def fieldify(h, r):
    ''' fieldify:
            separated csv records according to a record
        expects:
            h:  list; a list containing the csv field names
            r:  str; a valid csv record
        returns:
            d:  dict: a dictionary of fields
    '''
    d = {}
    curr = ''
    quoted = False
    q_char = ''
    f = 0
    for c in r:
        if quoted:
            if c == q_char:
                quoted = False
            else:
                curr += c
        elif c == '"' or c == "'":
            quoted = True
            q_char = c
        elif c == ',':
            d[h[f]] = curr.strip()
            curr = ''
            f += 1
        else:
            curr += c
    d[h[f]] = curr.strip() # got to make sure you get that last record
    return d

def main():
    base_dir = '/data/data/com.termux/files/home/docs/dailies'
    csv_tasks = 'tasks.csv'
    csv_fqn = build_file_name(base_dir, csv_tasks)
    
    records = get_csv(csv_fqn)
    json_var={}
    csv_fields = get_header(records[0])
    for record in records[1:]: 
        fields = fieldify(csv_fields, record)
        for field in fields:
            print(f'{field}:\n\t{fields[field]}')

if __name__ == '__main__':
    main()
