# raccoongang.com
Raccoon Gang corporate site

To make syncdb from scratch you have to comment

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',

and


    url(r'^', include('cms.urls')),

in urls.py, make migration and uncomment them after that.
