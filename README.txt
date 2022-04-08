Object-oriented Programming (OOP) 

The goal is to develop a simple eCommerce system, which uses the create, read, update and delete (CRUD) operations. For the eCommerce system, the program has to allow the user to:
(1) Add products;
(2) Remove products;
(3) Show a summary of their shopping session;
(4) Export the cart in JSON format

Each product has the following attributes: Name, price, quantity, EAN identifier and brand. By applying the concepts of inheritance, the types of products are developed as subclasses of the Product class, with the Product class acting as the superclass. The use of inheritance here allows the possibility of creating a new class that reuses the data members and methods of an existing class, such as the name, price, quantity, EAN identifier and brand that exists in the Product class. The 3 subclasses of the class Product are Clothing, Food, and Books. Each subclass has different attributes relating to its product type. For example, the Clothing class has size and material attributes. The Food class requires information on the expiry date and so on. As the Product class offers a to_json() method that returns the JSON representation of the product, each subclass of Product will override the to_json() method of the superclass, by applying the polymorphism concept in OOP.

Next, we create the shopping system with its CRUD operations. The ShoppingCart class will provide the methods to add a product, remove a product, display the contents of the cart and change the quantities of a product.

Finally, we have to create the environment for our users to do the actual shopping. The script will prompt users to type in commands in a while loop, which only terminates when the user indicates so. The following commands are as follows and stored in a tuple (This data is stored in a tuple as the commands are immutable, it processes faster than lists, consumes less memory and the elements can be accessed better).

1. A - allows the user to add a product to the cart (see the example in Listing 2);
2. R - allows the user to remove an existing product from the shopping chart (see Listing 3);
3. S - the script prints out a summary of the cart, along the lines of the example in Listing 4;
4. Q - the user can change the quantity of a product already present in the cart;
5. E - the script generates a summary of the cart as JSON, printed to the console. The JSON output is an array of JSON products (see the example in Listing 5);
6. C - at any moment, allows the user to interrupt the shopping session. The program will print out the following message: “The current operation is cancelled”. Then, the user should be able to continue with a new command.
7. T - the script terminates (exiting the while loop);
8. H - a request for help from the user. The commands that the program recognises are printed
out to the console (see in Listing 6);
Any other command will print out a message saying that the command was not recognised.
