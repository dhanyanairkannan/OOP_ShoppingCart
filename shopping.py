# Creating the Product class which stores information on the product name, price, quantity, EAN and branc
class Product:
  def __init__(self, name, price, quantity, EAN, brand):
    self.__name =name

    # Performing validations of the input data
    try: 
    	self.__price = float(price)
    except ValueError:
    	print('Price must be a numerical value.')
    try: 
    	self.__quantity = int(quantity)
    except ValueError:
    	print('Quantity must be an integer.')
    try: 
    	self.__EAN = EAN
    	assert len(EAN) == 13
    	assert int(EAN)
    except ValueError:
    	print('EAN identifier must be a 13-digit number.')
    self.__brand=brand
  
  def get_name(self):
    return self.__name

  def get_EAN(self):
    return self.__EAN_identifier
  
  def get_quantity(self):
    return self.__quantity

  def get_price(self):
    return self.__price

  def set_quantity(self,quantity):
    self.__quantity=quantity

  def get_brand(self):
    return self.__brand
  
  def to_json(self):
    r = {
    		'name': self.__name,
    		'price': self.__price,
    		'quantity': self.__quantity,
    		'EAN': self.__EAN,
    		'brand': self.__brand
	}
    return r

   def __str__(self):
   # Returning a strong representation of the product
   return('{} - {}x {} {}, ${}'.format(self.__EAN, self.__quantity, self.__brand, self.__name, round( self.__quantity*self.__price,2)))


# Creating the Clothing subclass of Product with the addition of size and material attributes
class Clothing(Product):
  def __init__(self,name,price,quantity,EAN,brand,size,material):
    super().__init__(name,price, quantity, EAN,brand)
    self.__size=size
    self.__material=material

  def get_size(self):
  	return self.__size

  def get_material(self):
  	return self.__material

  def to_json(self):
  	r = {
    		'name': self.__name,
    		'price': self.__price,
    		'quantity': self.__quantity,
    		'EAN': self.__EAN,
    		'brand': self.__brand,
   		'size': self.__size,
    		'material': self.__material
	}
    	return r

# Creating the Food subclass of Product with the addition of expiry date, boolean value of whether the item is gluten free, and a boolean value of whether the item is suitable for vegans attributes
class Food(Product):
  def __init__(self,name,price,quantity,EAN,brand,expiry_date,gluten_free,suitable_for_vegans):
    super().__init__(name, price, quantity, EAN, brand)
    self.__expiry_date=expiry_date
    self.__gluten_free=gluten_free
    self.suitable_for_vegans=suitable_for_vegans

  def get_expiry_date(self):
  	return self.__expiry_date

  def get_gluten_free(self):
  	return self.__gluten_free
	# True if the food item is gluten free, False otherwise.

  def get_suitable_for_vegans(self):
  	return self.__suitable_for_vegans
	# True if the food item is suitable for vegans, False otherwise.

  def to_json(self):
  	r = {
    		'name': self.__name,
    		'price': self.__price,
    		'quantity': self.__quantity,
    		'EAN': self.__EAN,
    		'brand': self.__brand,
   		'expiry_date': self.__expiry_date,
    		'gluten_free': self.__gluten_free,
    		'suitable_for_vegans': self.__suitable_for_vegans
   	}
    	return r

# Creating the Food subclass of Product with the addition of the attributes for the author and the year the book was published 
class Books(Product):
  def __init__(self,name,price,quantity,EAN,brand,author,year_published):
    super().__init__(name, price, quantity, EAN, brand)
    self.__author=author
    self.__year_published=year_published

  def get_author(self):
  	return self.__author

  def get_year_published(self):
  	return self.__year_published

  def to_json(self):
  	r = {
    		'name': self.__name,
    		'price': self.__price,
    		'quantity': self.__quantity,
    		'EAN': self.__EAN,
    		'brand': self.__brand,
   		'author': self.__author,
    		'year_published': self.__year_published
   	}
    	return r



# The Shopping System
class ShoppingCart:
  def __init__(self):
      self.__items=[]

  def getProducts(self):
  	return self.__items

  def addProduct(self,p):
    # Adding a Product, p
	existing_item=False
  	for item in self.__items:
    		if p.get_EAN() == item.get_EAN():
			item.set_quantity(item.get_quantity() + p.get_quantity())
			existing_item=True      
	if not existing_item:
		self.__items.append(p)
	return True
 
  def removeProduct(self,p):
	to_remove = None
	for item in self.__items:
		if p.get_EAN() == item.get_EAN():
			if item.get_quantity() - p.get_quantity() >0:
				item.set_quantity(item.get_quantity()-p.get_quantity())
			else:
				to_remove=item
	if not to_remove:
		return False
	else:
		self.__items.remove(to_remove)
		return True


  
  def changeProductQuantity(self,p_EAN,q):
    #To change quantity of product p, using its EAN identifier to quantity q
	for item in self.__items:
		if p_EAN == item.get_EAN():
			item.set_quantity(q)

  def is_product_in_cart(self, p_EAN):
	for item in self.__items:
		if p_EAN == product.get_EAN():
			return True
	return False


  def showSummary(self):
	print("This is the total of the expenses:")
	total = 0
	for item in self.__items:
		print(item)
		total+=item.get_price()*item.get_quantity()
	print('Total: ${}'.format(round(total,2)))



# Doing Some Shopping
help_tuple=(
   '[A] - Add a new product to the cart',
   '[R] - Remove a product from the cart',
   '[S] - Print a summary of the cart',
   '[Q] - Change the quantity of a product',
   '[E] - Export a JSON version of the cart',
   '[C] - Cancel the current operation',
   '[T] - Terminate the program',
   '[H] - List the supported commands'
)


print('The program has started.')
print('Insert your next command (H for help):')
terminated = False
cart=ShoppingCart()

while not terminated:
  c = input("Type your next command:")

  if c=="T":
	break

  elif c=="H":
  	print("The program supports the following commands:")
  	for keyword in help_tuple:
  		print("\t"+keyword)

  elif c=="C":
	print("There is no operation to cancel at the moment.")

  elif c=="S":
	cart.showSummary()

  elif c=="E":
	print([p.__dict__ for p in cart.getProducts()])

  elif c=="R":
	while True:
		ean=input("What is the EAN identifier of the product you want to remove? ")
		try:
			asset is_valid_EAN(ean)
		except ValueError:
			print("The EAN code is a 13-digit number.")
			continue
		break
	if cart.is_product_in_cart(p_EAN=ean):
		cart.removeProduct(ean)
		print("Item is removed from the cart successfully.")
	else:
		print("No such item in cart to remove.")
	
  elif c=="Q":
    product_name=input("What is the name of the product you want to change quantities? ")
    product_quantity=input("What is the new quantity?:")
    for key in in_cart:
      if product_name==in_cart[key][0]:
        item_name=in_cart[key]
        try:
          product_quantity=int(product_quantity)
        except:
          product_quantity=input("Please insert quantity as numbers. Insert the new quantity: ")
      in_cart.changeProductQuantity(item_name,product_quantity)
    else:
      print("{} is not in the cart.".format(product_name))

  elif c=="A":
    print("Adding a new product:")
    product_type=str(input("Insert its type: "))
    while product_type not in ('Clothing','Food','Shoes'):
      print("We do not have this product type. Select either Clothing, Food or Books.")
      product_type=str(input("Insert its type: "))

    item_name=str(input("Insert its name: "))
    item_price=input("Insert its price (£): ")
    try:
      item_price=float(item_price)
    except:
      item_price=input("Please insert price as numbers. Insert its price (£): ")
    item_quantity=int(input("Insert its quantity: "))
    item_brand=str(input("Insert its brand: "))
    item_EAN=int(input("Insert its EAN code: "))
    try:
      item_EAN=int(item_EAN)
    except:
      item_EAN=input("Your EAN Identifies has to be 13 digits. Please enter the EAN code again: ")
    while len(str(item_EAN))!=13:
      item_EAN=input("Your EAN Identifies has to be 13 digits. Please enter the EAN code again: ")
    else:
      pass

    if product_type=="Clothing":
      item_size=input("Insert its size: ")
      item_material=str(input("Insert its material: "))
      product_name=Clothing(item_name,item_price,item_quantity,item_EAN,item_brand,item_size,item_material)
      cart.addProduct(product_name)
    elif product_type=="Food":
      expirydate = input('Enter the expiry date in YYYY-MM-DD format: ')
      glutenfree=str(input("Insert Y if its gluten free. Otherwise, insert N: "))
      vegan=str(input("Is this suitable for vegans?: "))
      product_name=Food(item_name,item_price,item_quantity,item_brand,item_EAN,expirydate,glutenfree,vegan)
      cart.addProduct(product_name)
    elif product_type=="Books":
      author=int(input("Author: "))
      year_published=str(input("Year Published: "))
      product_name=Shoes(item_name,item_price,item_quantity,item_brand,item_EAN,shoe_size,shoe_colour)
      cart.addProduct(product_name)

  else:
    print("Command not recognised. Please try again.")

print("Goodbye.")
