'''Custom mixins.'''

class SubmissionMixin:
    '''Interface for models representing submitted content (ie. posts and comments.)'''
    def increment_score(self, amount: int):
        '''Increments fields `score`  and `fire_index` by a specified number.
        This method does not update the model's fields itself- that process
        must be performed separately.
        
        :param: Integer change to fields `score` and `fire_index`. Can be negative.'''
        self.score += amount
        self.fire_index += amount
    def reset_fire_index(self):
        '''Resets the field `fire_index` to 0, but does not update
        the model.
        '''
        self.fire_index  = 0