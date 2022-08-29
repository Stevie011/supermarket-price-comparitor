checkers_price_list = {
    "Albany Brown Bread": 19.99, 
    "Clover Milk 2l": 25.99, 
    "Doritos Sweet Chilli 145g": 21.99,
    "Tuna Tin": 16.99,
    "Strawberries 250g": 26.99,
    "Baked Beans Tin": 14.99,
    "Five Star chocolate 48.5g": 11.99,
    "White hamburger rolls 6": 12.99,
    "Lettuce Head": 9.99,
    "Button Mushrooms 250g": 19.99,
    "Spaghetti 500g": 19.99
}

woolworths_price_list = {
    "Albany Brown Bread": 21.99, 
    "Clover Milk 2l": 27.99, 
    "Doritos Sweet Chilli 145g": 19.99,
    "Tuna Tin": 18.99,
    "Strawberries 250g": 28.99,
    "Baked Beans Tin": 12.99,
    "Five Star chocolate 48.5g": 13.99,
    "White hamburger rolls 6": 14.99,
    "Lettuce Head": 7.99,
    "Button Mushrooms 250g": 21.99,
    "Spaghetti 500g": 19.99
}

# get items, add to list
# if item not in price list, alert user and ask for item again
# if user inputs x, it then calcs which is cheapest

# print(checkers_price_list.keys())

myList = []
while True:
    word = input("Enter a Word (Type 'q' to quit): ")
    if word == 'q':
        break
    elif word not in checkers_price_list.keys():
        print("word not in price list")
        pass
    else:
        myList.append(word)
    
    print(myList)

#print("total list : ", myList)

checkers_total, woolworths_total= 0,0

for i in myList:
    checkers_total += checkers_price_list[i]
    woolworths_total += woolworths_price_list[i]

checkers_total = round(checkers_total, 2)
woolworths_total = round(woolworths_total, 2)


if checkers_total < woolworths_total:
    print(f"Checkers is the cheapest. There your shop will cost {checkers_total} compared to the total at Woolworths which would've been {woolworths_total}")
elif checkers_total > woolworths_total:
    print(f"Woolworths is the cheapest. There your shop will cost {woolworths_total} compared to the total at Checkers which would've been {checkers_total}")

else:
    print("They both cost the same!")


# print("Checkers total is : ", round(checkers_total, 2))
# print("woolies total : ", round(woolworths_total, 2))

# def main():
    
#     new_list = parse()


# def parse():
#     myList = []


#     #while True:
#     word = input("Enter a Word (Type 'q' to quit): ")
#     if word == 'q':
#         break
#     myList.append(word)
#     return myList



# ...


# if __name__ == "__main__":
#     main()


# for k,v in checkers_price_list.items():
#     print(k)


