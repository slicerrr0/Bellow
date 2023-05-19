'''Classes for dealing with user analytics.'''
from account.models import CustomUser
from post.models import Post
from post.mixins import SubmissionMixin
from community.models import Community

class Interaction(SubmissionMixin):
    '''When a user clicks on a post or upvotes a post or comment, 
    this data is recorded and relayed to the server, where it is bundled
    into a subclass of `Interaction` for further processing.
    '''
    def __init__(self, user: CustomUser, *args, **kwargs) -> None:
        self.user = user

class PostVisitation(Interaction):
    '''User clicks on, or 'visits', a post.'''
    def __init__(self, user: CustomUser, post: Post) -> None:
        super().__init__(user)
        self.post = post
        self.community = super().get_attribute_from_submission(self.post, 'community')
        self.post_author = super().get_attribute_from_submission(self.post, 'author')