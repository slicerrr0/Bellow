'''Custom mixins.'''

class SubmissionMixin:
    '''Interface for models representing submitted content (ie. posts and comments.)'''
    def increment_score(self, amount=1):
        '''Increments fields `score`  and `fire_index` by a specified number.
        This method does not update the model's fields itself- that process
        must be performed separately.
        
        :param amount: Integer change to fields `score` and `fire_index`. 
        Defaults to 1 (can also be negative).
        '''
        assert type(amount) == int
        self.score += amount
        self.fire_index += amount
    def reset_fire_index(self):
        '''Resets the field `fire_index` to 0, but does not update
        the model.
        '''
        self.fire_index  = 0