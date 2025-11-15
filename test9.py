import json

emp = '{"id": "9", "name": "Nitin", "dept": "Finance"}'
emp_dict = json.loads(emp)

#print(emp_dict)
#print(emp_dict['name'])

f = open('data.json',)
data = json.load(f)

for i in data['emp_details']:
    print(i)
f.close()

emp = {
  "id": "4",
  "name": "Sunil",
  "department": "HR"
}

json_obj = json.dumps(emp, indent=4)
#print(json_obj)


data = {
    "name": "Sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("sample.json", "w") as outfile:
    json.dump(data, outfile)
    
emp = '{"id":"9", "name": "Nitin", "department":"Finance"}'
emp_d = json.loads(emp)

print(json.dumps(emp_d, indent=4, sort_keys=True))