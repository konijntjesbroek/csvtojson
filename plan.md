## Project csvtojson
_created by_: Arlo Gittings  
_created on_: 2021-07-20   
_last modified_: 2021-07-20 
### Description
This is a prototype for the workit JSON files. The final goal is to create and
implement a tool that will allow me to display the lines in the existing 
tasks.csv files and create a tasks.json file. Based on this, I should be able 
to generate a class which will hold the data descriptor and methods to 
manipulate the fields.

### Layout
- get\_csv
    - create a variable hold the task list in csv format
    - open file containing csv
    - load the data from the file into the variable
- format\_csv
    - build a data structure to hold the csv data
    - populate instances with data from get\_csv
- format\_json
    - create a variable to hold the task list in json format
    - parse instances of data structure
    - populate variable with records from format\_csv
- write\_json
    - create a file to hold json
    - dump json to file

### Success Factors:
- Phase One:
    - Open a tasks.csv for a specific date.
    - Display the task list
        - Print lines
        - Print fields
        - Separate sub fields
- Phase Two: 
    - Format CSV as a JSON object
        - create base dictionary
        - populate field names
        - populate field contents
    - Display taks in JSON
- Phase Three:
    - Create tasks.json for a specific date.
    - Write out the tasklist to tasks.json
