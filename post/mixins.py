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
    def get_attribute_from_submission(self, submission: object, attr_name: str):
        '''Returns a specified attribute value for a submission.
        This method may be used to access what Community a post belongs to
        or what user made a comment.

        The existence of parameter `submission` within the database should be verified
        prior to the invocation of this method.
        
        :param submission: Submission.
        
        :param attr_name: Specifies what field name to index `submission` for.
        '''
        return submission.__getattribute__(attr_name)