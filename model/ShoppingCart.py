class ShoppingCart:

    def __init__(self) -> None:
        #list of products
        self.__products = [] 
    def __str__(self) -> str:
        """Returns a string representation of the shopping cart."""
        return f"ShoppingCart: {', '.join(self.products) if self.products else 'No products'}"
        
    # ********** property products - (only getter) ***********
    @property
    def products(self) -> list[str]:
        """ The products property. """
        return self.__products
    
    def add_product(self, new_product: str) -> None:
        self.products.append(new_product)

    def remove_product(self, removing_product: str) -> None:
        if removing_product in self.products:
            self.products.remove(removing_product)   
        else:
            print(f"{removing_product} not found in the shopping cart.") 
    def __add__(self, other: 'ShoppingCart') -> 'ShoppingCart':
        """Combines two shopping carts into a new one."""
        new_cart = ShoppingCart()
        new_cart.__products = self.products + other.products
        return new_cart

    def __iadd__(self, other: 'ShoppingCart') -> 'ShoppingCart':
        """Adds the products of another cart to this one in place."""
        self.__products += other.products
        return self     


     


