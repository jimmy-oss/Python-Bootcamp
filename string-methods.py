# ---Strings ---
# 1- Len() it tells us how many characters we have
address = "Kenya"
print(len(address))

# 2- [] Notation used to access a certain character on a string
print(address[0])
print(address[4])
print(address[-2])

# 3- [] Notation can also be used at the bracket to extract specific numbers on a string
print(address[0:3])
print(address[-3:-1])
print(address[0:])
print(address[:-1])
print(address[:])

# 4- Concatenation
country = "Kenya"
city = "Nairobi"
full_city = city + "," + country
print(full_city)

# 5- Upper
print(address.upper())

# 6- Lower
print(city.lower())

# 7- Title The first letter of the strings becomes capital
print(full_city.title())
 
