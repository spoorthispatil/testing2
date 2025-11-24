import sys
if len(sys.argv)==3:
  script_name=sys.argv[0]
  a=sys.argv[1]
  b=sys.argv[2]
else:
  script_name=sys.argv[0]
  a=20
  b=30
sum=a+b
print("Sum:",sum)
