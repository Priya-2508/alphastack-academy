from django.contrib import admin
from django.urls import include, path
from academy.llms import llms_txt
from academy.robots import robots_txt
from academy.sitemaps import StaticViewSitemap
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("academy.urls")),
    path("admin/", admin.site.urls),
        path("robots.txt", robots_txt, name="robots_txt"),
        path(
            "sitemap.xml",
            sitemap,
            {"sitemaps": sitemaps},
            name="sitemap",
        ),
        path("llms.txt", llms_txt, name="llms_txt"),
        path("", include("academy.urls")),
]
