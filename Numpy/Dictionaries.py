# student={
#     "Name" : "Aarav",
#     "math" : 86,
#     "science" : 91,
#     "english" : 78
# }

# student["math"]=90

# print(student["Name"])
# print(student["english"])
# print(student["math"])


detail={
    "Name":"Piyush Maurya",
    "Language":"Python",
    "Experience":"0 Year",
    "Skill":"NaN"
}

print(detail["Name"])
print(detail["Skill"])


detail["Experience"]="1+ Year"
print(detail["Experience"])

for key,value in detail.items():
    print(key,"=",value)