import function
import json
import sys

print("Process Start")

data = json.loads(sys.argv[1])
a = data["a"]
b = data["b"]

print("a는", a)
print("b는", b)
print("합은", function.add(a,b))

print("py-image-sample2 Process Complete")