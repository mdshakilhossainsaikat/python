str = "abcdefghijklmnopqrstuvwxyz"

# len() shows the length of the string

print(len(str))

#  .endswith("") 

print(str.endswith("xyz"))
print(str.endswith("xz"))

#  .startswith("")

print(str.startswith("abc"))
print(str.startswith("abd"))

#  capitalize

print(str.capitalize())

#  .lower()

print(str.lower())

#  .upper()

print(str.upper())

#  .title()

intro = "hello world"

print(intro.title())

#  .find("word")

print(intro.find("world"))

#  .replace("word")

print(intro.replace("hello", "die"))