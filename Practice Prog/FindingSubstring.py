#find position of substring

s="Today is a great day to learn something new" \
   "Every day may not be good. But there is something good in every day."

subs="day"
found=False
pos=-1
length=len(s)
while True:
    pos=s.find(subs,pos+1,length)
    if pos==-1:
        break
    print("Found the sub-string at position",pos)
    Found=True
if Found==False:
     print("Sub-String not found")
