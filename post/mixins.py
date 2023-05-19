'''Custom mixins.'''

class SubmissionMixin:
    '''Interface for models representing submitted content (ie. posts and comments.)'''
    def calculate_score(self):
        return self.upvotes.count() - self.downvotes.count()
    def reset_fire_index(self):
        '''Resets the field `fire_index` to 0, but does not update
        the model.
        '''
        self.fire_index = 0