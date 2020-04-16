from random import randint

class Game:
    """ 
    This game chooses a random integer in a given bound and the user tries to guess it.
    
    Attributes:
    n (integer) - the chosen integer
    lower_bound (integer) - the lower bound for n, 0 if not given
    upper_bound (integer) - the upper bound for n, 100 if not given
    attempts - the number of time guesses were made
    
    """
    
    def __init__(self, lower_bound = 0, upper_bound = 100):
        try:
            assert lower_bound < upper_bound, 'lower bound is greater than or equal to upper bound'
        except AssertionError as error:
            raise 
        
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.n = randint(lower_bound, upper_bound)
        self.attempts = 0
        
        
    def make_guess(self, k):
        """
        This methods allows user to make a guess
        
        Input:
        k (integer) - user's guess
        
        Output:
        result (string) - string informing the user of whether the guess is right, higher than actual or lower than actual
        """
        if k != self.n:
            self.attempts = self.attempts + 1
        return 'Your guess is out of bonds' if (k > self.upper_bound or k < self.lower_bound) \
                                            else ('You found it in {0} attempts!'.format(self.attempts) if k == self.n \
                                            else ('Your guess is higher than the mystical number :(' if k > self.n \
                                            else 'Your guess is lower than the mystical number :('))
    
    
    def change_number(self, lower_bound = 0, upper_bound = 100):
        """
        This function changes the random number generated.
        
        Input:
        lower_bound (integer, optional) - sets a new lower bound, if not given uses 0
        upper_bound (integer, optional) - sets a new upper bound, if not given uses 100
        
        Output:
        none
        """
        
        try:
            assert lower_bound < upper_bound, 'lower bound is greater than or equal to upper bound'
        except AssertionError as err:
            raise
            
        self.n = randint(lower_bound, upper_bound)
        
        
    def __repr__(self):
        return 'lower_bound: {0}, upper_bound: {1}, n: {2}'.format(self.lower_bound, self.upper_bound, self.n)