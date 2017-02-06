from django.contrib.syndication.views import Feed
from djangocms_blog.models import Post, BlogCategory
from django.utils.feedgenerator import Atom1Feed


class RssLatestPostFeed(Feed):
    """
    View for RSS 2.0.
    """
    title = "Raccoon Gang News feed"
    link = "/blog/"
    description = "Insights and tips on eLearning from Raccoon Gang, trusted online learning provider"

    def items(self):
        return Post.objects.filter(publish=True).order_by('-date_published')[:5]

    def item_title(self, item):
        return item.get_title()

    def item_description(self, item):
        return item.get_description()

    def item_pubdate(self, item):
        return item.date_published

    def item_categories(self, item):
        return BlogCategory.objects.filter(blog_posts=item)


class AtomLatestPostFeed(RssLatestPostFeed):
    """
    View for Atom 1.0.
    """
    feed_type = Atom1Feed
    subtitle = RssLatestPostFeed.description
