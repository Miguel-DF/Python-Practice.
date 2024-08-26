# dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA":"Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

#print(dir(capitals))
#print((help(capitals)))

#print(capitals.get("India"))

# check if japan is exist

if capitals.get("Japan"):
    print("That capitals exist")
else:
    print("That capitals doesn't exist")

#capitals.update({"Germany":"Berlin"})
#capitals.update({"USA":"Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()
print(capitals)

for key in capitals.keys():
    print(key)


for key, value in capitals.items():
    print(f"{key}:{value}")