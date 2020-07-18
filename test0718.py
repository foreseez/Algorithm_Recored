import  csv
with open("test.csv",'a',encoding="utf8") as f :
    writer = csv.DictWriter(f,fieldnames=["name",'age'])
    writer.writeheader()
    name = ["tom","bobb",'sisiya']
    age = [12,23,43]
    
    result = []
    for i in  range(3):
        res = {"name":name[i],
              "age":age[i]
              }
        result.append(res)
    print(result)

    writer.writerows(result)

