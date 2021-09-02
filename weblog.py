import re

#string = '172.16.110.71 172.16.100.21 TCosey [06/May/2020:10:22:21 -0400] "GET /confluence/rest/ui/1.0/content/6194434/labels?_=1588774941735 HTTP/1.1" 200 39 22 "http://devops-njkids/confluence/pages/resumedraft.action?draftId=6193909&draftShareId=cb27bffc-0251-46bc-bc1e-3f290e0b7b17&" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"'
string = '172.16.110.71 172.16.100.21 TCosey [06/May/2020:10:22:21 -0400] "GET /confluence/rest/ui/1.0/content/6194434/labels?_=1588774941735 HTTP/1.1" 200 39 22'

pattern = '^(.*?) (.*?) (.*?) (\[.*\]) (\".*\"?) (.*?) (.*?) (.*)'

match = re.search(pattern, string)

if match:
  print(match.group(1))
  print(match.group(2))
  print(match.group(3))
  print(match.group(4))
  print(match.group(5))
  print(match.group(6))
  print(match.group(7))
  print(match.group(8))

else:
  print("pattern not found")
