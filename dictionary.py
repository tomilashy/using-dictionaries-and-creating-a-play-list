
detail = {"name": "jesutomi", "age": 10}  #use of curly braces

details = dict(
    name="jesutomi", age=10)
print(details)
print(detail)

print("checking for ", detail["name"])
#keys

for x in detail:
	print(x)

for x in detail.keys():
	print(x)

#values
for x in detail:
	print(detail[x])

#or

for x in detail.values():
	print(x)

#item
for x in detail.items():
	print(x)

for k, v in detail.items():
	print(k, ":", v)

for x in detail.items():
	print(x[0], ":", x[1])

x = input("what key are you looking for?")
if x in detail:
	print(detail[x])

news = detail.copy();
print (news);
detail.clear();


print  (details == news);

#fromkey
new_dict={}.fromkeys(["name","age","address"], "unknown")
print(new_dict.get("name"))

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

bakery_stock.pop("toffee cookie"); #remove a paticular item

bakery_stock.popitem(); #removes last item 

new_dict.update(bakery_stock); #adds all of bakery_stock to new_dict

