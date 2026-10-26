import csv

# with open('oil_spill_master.csv', encoding='utf-8-sig') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# values = []

# for row in rows:
#     raw = row.get('estimatedquantity').strip()
#     if raw == "":
#         continue
#     values.append(float(raw))
      
# print("Largest Value:", max(values))
# print("Smallest Value:", min(values))
# print("Valid Count:", len(values))

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw =="":
            continue
        values.append(float(raw))  

    return{
        "smallest":min(values),
        "largest":max(values),
        "count":len(values)
           
               
    }
        
result = inspect_column("oil_spill_master.csv","estimatedquantity" )
print(result)

result = inspect_column("oil_spill_master.csv","quantityrecovered")
print(result)