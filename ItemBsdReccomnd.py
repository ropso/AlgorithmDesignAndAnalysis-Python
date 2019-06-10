lis=[["orange","apple","grapes"],
["avacado","chilli","orange"],
["watermillion","banana","orange"],["pineapple","orange","strawberry","grapes"],["watermelon","guavava","kiwi"],["kiwi","apple","tomato"],["mango","chiku","pomograd"],["pomograd","kiwi","chilli","tomamto"],["mango","pomograd","banana"],["pineapple","orange","banana"],["pomograd","kiwi","orange","strawberry"]]

Fruit_dict=dict()
for fruitBucket in lis:
    for fruit in fruitBucket:
        if Fruit_dict.get(fruit) i s not None:
            Fruit_dict[fruit]+=1
        else:
            Fruit_dict[fruit]=1

print(Fruit_dict)