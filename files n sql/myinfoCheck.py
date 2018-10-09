import sys
import json

if len(sys.argv) <= 1:
    print('type one : host, user, passwd, database')
    sys.exit()

info = sys.argv[1]

with open('myinfo.json') as f:
    data = json.load(f)

print(type(data))
print(data[info])