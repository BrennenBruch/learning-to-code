guests = ["andy", "bob", "carl", "dave"]
print(guests)

guests.append("bill")
print(guests)

guests.pop()
print(guests)

for guest in guests:
    print(f"{guest.title()} is here!")

guests_dict = {"name": "andy", "age": 20, "job": "cook",
               "name": "bob", "age": 22, "job": "officer",
               "name": "carl", "age": 30, "job": "writer",}

for guest in guests_dict:
   print(f"{guests_dict["name"]} is here! they are {guests_dict["age"]}! and they are a {guests_dict["job"]}!")