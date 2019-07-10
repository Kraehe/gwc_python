womenInTech = ["Giovanna Rodriguez", "Sara Resnick", "Ada Lovelace", "Carol Shaw", "Madison Maxey", "Kim Swift", "Miral Kotb"]
 # A short list of women in tech

for num in womenInTech:
    print(num)

print("––––––––")

for i in range(len(womenInTech)):
    print(womenInTech[i])

print("––––––––")

print('Giovanna Rodriguez' in womenInTech)
# 'in' checks to see if the string before 'in' is in the the list after

print("\"Wow!\"")

print("––––––––")

woman = "Gia"
print(len(woman))
# outputs the length of "Gia"
print("ia" in woman)
# checks to see if the characters "ia" are indeed in the variable's string and outputs True/False
print(woman[1])
# outputs the second character in the string in woman
print(woman[0]+woman[2])
# concatenates the first and third characters in the string in woman

print("––––––––")

for letter in woman:
    print(woman)


print(womenInTech[1:5])
# prints the value of woman for the number of characters in "Gia" which is 3
