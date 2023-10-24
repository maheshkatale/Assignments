"""
2) create a dictionary with pairs
	soap:100    deo:300    perfume:400
  now accept a product name from user (in any case, so you have to handle "ignore case") and display its price.
  Also , if the product is not present in the dictionary display the error message " product not available "
	Note:  you should not get "KeyError:" in the program.
"""

dict={"soap":100,"deo":300,"perfume":400}
product=input("Enter the product: ")
prices=int(input("Enter the prices: "))
if(product==""):
    print("Product is not available")
else:
    dict.update({product:prices})
    print(dict)
