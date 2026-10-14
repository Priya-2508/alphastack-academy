from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    protocol = "https"

    def items(self):
        return [
            "academy:home",
            "academy:about",
            "academy:courses",
            "academy:java",
            "academy:python",
            "academy:events",
            "academy:benefits",
            "academy:contact",
            "academy:python_fullstack",
        ]

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        priorities = {
            "academy:home": 1.0,
            "academy:courses": 0.9,
            "academy:python_fullstack": 0.9,
            "academy:java": 0.8,
            "academy:python": 0.8,
            "academy:events": 0.7,
            "academy:benefits": 0.7,
            "academy:about": 0.6,
            "academy:contact": 0.5,
        }

        return priorities.get(item, 0.5)