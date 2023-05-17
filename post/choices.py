'''Selectable options for the `choices` kwarg in the 
`django.db.models.Model.CharField` constructor.
'''

class FlairColors:
    '''Contains all selectable flair colors.'''
    # Define all selectable color choices
    red, blue, green, yellow, orange = 'Red', 'Blue', 'Green', 'Yellow', 'Orange'
    purple, black, brown = 'Purple', 'Black', 'Brown'

    # Create dictionary mapping choices to their field representations
    colors = {
        red: 'Red',
        blue: 'Blue',
        green: 'Green',
        orange: 'Orange',
        yellow: 'Yellow',
        purple: 'Purple',
        black: 'Black',
        brown: 'Brown',
    }

    # Initialize empty choice sequence
    choices = tuple()

    @staticmethod
    def create_choices() -> tuple[tuple]:
        '''Iterates through all key-value pairs in 
        class attribute `FlairColors.colors` to produce
        a properly formatted sequence of tuples pairing
        together choices and their field representations.
        '''
        for value, repr in FlairColors.colors.items():
            FlairColors.choices += (value, repr)
        return FlairColors.choices