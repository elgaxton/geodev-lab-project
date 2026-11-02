import csv

def read_rows(filename):
    with open(filename, encoding = "utf-8-sig") as f:
        return(list(csv.DictReader(f)))
    
def clean_values(rows, column):
    values = []
    for row in rows:
        raw = row[column].strip()
        
        if raw == "":
            continue
        values.append(float(raw))
    return values

def summarise(values):
    if len(values) ==0:
        return{
            "count":0,
            "smallest":None,
            "largest":None,
            "average":None
        }
        
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
        "average": sum(values)/len(values)
        
    }
    
# rows = read_rows("oil_spill_master.csv")
# values = clean_values(rows, "estimatedquantity")
# summary = summarise(values)
# print(summary)

def summarise_all(filename, columns):
    rows = read_rows(filename)
    report ={}
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

report = summarise_all("oil_spill_master.csv",["estimatedquantity", "quantityrecovered"] )

for column, stats in report.items():
    print(column, "->", stats)