from django.contrib.syndication.views import Feed
from posts.models import Post 


class LatestPostsFeed(Feed):
    """returns the most recent posts."""

    title = 'Um byte de ideias'
    link = '/feed/'
    description = 'Aprenda programação, explore tecnologias e domine metodologias ágeis. Tutoriais, insights e reflexões para curiosos e apaixonados por tecnologia!'

    def items(self):
        """return the 100 most recent posts."""
        return Post.objects.filter(published=True).order_by('-updated_at')[:100]

    def item_title(self, item):
        """returns the post title."""
        return item.title

    def item_description(self, item):
        """returns the post content."""
        return item.content
    
    def item_pubdate(self, item):
      """returns the post creation date."""
      return item.created_at 

    def item_updateddate(self, item):
        """returns the post update date."""
        return item.updated_at