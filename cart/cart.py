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
        