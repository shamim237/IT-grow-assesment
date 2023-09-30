import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["titanic"]
collection = db["data"]

# Function to add a passenger
def add_passenger(data):
    collection.insert_one(data)

# Function to retrieve all passengers
def get_all_passengers():
    return collection.find()

# Function to update a passenger's information
def update_passenger(passenger_id, new_data):
    collection.update_one({"PassengerId": passenger_id}, {"$set": new_data})

# Function to delete a passenger
def delete_passenger(passenger_id):
    collection.delete_one({"PassengerId": passenger_id})

# Adding a few passengers (example data provided)
passenger_1 = {
    "PassengerId": 1,
    "Survived": 0,
    "Pclass": 3,
    "Name": "Jackson Smith",
    "Sex": "male",
    "Age": 50,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": "B/5 21171",
    "Fare": 7.25,
    "Cabin": None,
    "Embarked": "S"
}

passenger_2 = {
    "PassengerId": 2,
    "Survived": 1,
    "Pclass": 1,
    "Name": "Amely Mckenzie",
    "Sex": "female",
    "Age": 38,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": "PD 17599",
    "Fare": 71.2833,
    "Cabin": "C85",
    "Embarked": "C"
}

add_passenger(passenger_1)
add_passenger(passenger_2)

# Getting all passengers
print("All Passengers:")
for passenger in get_all_passengers():
    print(passenger)

# Updating a passenger
update_passenger(1, {"Fare": 8.0})

# Getting all passengers after update
print("\nAll Passengers After Update:")
for passenger in get_all_passengers():
    print(passenger)

# Deleting a passenger
delete_passenger(2)

# Getting all passengers after delete
print("\nAll Passengers After Delete:")
for passenger in get_all_passengers():
    print(passenger)
