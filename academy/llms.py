from django.http import HttpResponse


def llms_txt(request):
    base_url = request.build_absolute_uri("/").rstrip("/")

    content = f"""# Academy

> Educational academy offering programming and full-stack development courses.

## Main Pages

- [Home]({base_url}/): Academy home page.
- [About]({base_url}/about/): Information about the academy.
- [Courses]({base_url}/courses/): Available courses.
- [Benefits]({base_url}/benefits/): Benefits of studying with the academy.
- [Events]({base_url}/events/): Academy events.
- [Contact]({base_url}/contact/): Contact information.

## Courses

- [Java Course]({base_url}/courses/java/): Java programming course.
- [Python Course]({base_url}/courses/python/): Python programming course.
- [Python Full Stack]({base_url}/python-full-stack/): Python full-stack development program.

## Site Information

- [XML Sitemap]({base_url}/sitemap.xml): Sitemap containing public pages.
"""

    return HttpResponse(
        content,
        content_type="text/plain; charset=utf-8",
    )