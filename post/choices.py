'''Selectable options for the `choices` kwarg in the 
`django.db.models.Model.CharField` constructor.
'''

class BaseChoice:
    '''Base class for defining finite series of selectable field choices.
    
    Extend this class to create choices for specific models.
    '''
    # Create empty class attributes that will be overriden in subclasses
    choices = dict()
    paired_choices = tuple()
    
    def create_choices(self) -> tuple[tuple]:
        '''Iterates through all key-value pairs in 
        class attribute `BaseChoice.choices` to produce
        a properly formatted sequence of tuples pairing
        together choices and their field representations.
        '''
        for value, repr in self.choices.items():
            self.paired_choices += (value, repr)
        return self.paired_choices

class FlairColors(BaseChoice):
    '''Contains all selectable flair colors.'''
    # Define all selectable color choices
    red, blue, green, yellow, orange = 'Red', 'Blue', 'Green', 'Yellow', 'Orange'
    purple, black, brown = 'Purple', 'Black', 'Brown'

    # Create dictionary mapping choices to their field representations
    choices = {
        red: 'Red',
        blue: 'Blue',
        green: 'Green',
        orange: 'Orange',
        yellow: 'Yellow',
        purple: 'Purple',
        black: 'Black',
        brown: 'Brown',
    }
