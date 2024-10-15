class Cart():
    # initialise class
    def __init__(self, request):
        # creat the session
        self.session =  request.session
        
        # Get the current session key if it exists
        cart = self.session.get('session_key')
        # let's call it 'session_key'
        # if the 'session_key' exist in the session -> get it: assign it to the variable 'cart'
        
        # if the user in new -> no session key. Create one!
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {} 
            # ex {'book'}...
        
        # -- > make sure cart is available on all pages on the site    
        self.cart = cart
        # + context-processors    
    
    def add(self, product):
        product_id = str(product.id)
        
        # Logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]={
                'name': str(product.name),
                'price': str(product.price),
                'description': str(product.Description),
                }
            # update the cart in the session
        
        # apply sessiob modification
        self.session.modified = True
    
    # get the length of the product quantity on the cart    
    def __len__(self):
        return len(self.cart)