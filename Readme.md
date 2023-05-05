# json2csv

A generic approach to convert JSON files to CSV.
The CSV headers (column names) are determined by the path through the JSON structure to find this specific value. [JSONPath](https://goessner.net/articles/JsonPath/) dot-notation is used.

It is assumed rows of the target CSV are JSON objects in a top level list. Other structures will yield a single row.

## Usage

### convert a single file
`./json2csv.py my_data.json`
The CSV file will be created as `my_data.csv` next to `my_data.json`

### convert a single file with a destination
`./json2csv.py my_data.json -o /path/to/somewhere/else/export.csv`
The CSV file will be created as `/path/to/somewhere/else/export.csv`

### convert many files
`./json2csv.py my_data.json subdir/other_data.json`
The CSV files will be created next to each source file, with the basename of the JSON file and a `.csv` extension

`./json2csv.py files/*.json`

### convert many files with destinations
`./json2csv.py my_data.json subdir/other_data.json n.json -o /export/my_data.csv /private/logs.csv n.csv`

`./json2csv.py JSON... -o CSV...`
The two lists JSON and CSV must have the same amount of entries. JSON file `n` will be converted to CSV file `n`, JSON `n+1` to CSV `n+1`, …

## Development

### Run Tests 
`pytest`
