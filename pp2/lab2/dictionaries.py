#1Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))   
#2Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)
#3Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["colour"] = "red"
print(car)
#4Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
#5Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)