import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

main_html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Main Page</title>
    </head>
    <body>
        <h1>Welcome to my first site</h1>
        <ul>
            <li><a href="/">Main</a></li>
            <li><a href="/about">About</a></li>
        </ul>      
    </body>
    </html>
"""

about_html = """
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About me</title>
    </head>
    <body>
        <h1>About me</h1>
        <ul>
            <li><a href="/">Main</a></li>
            <li><a href="/about">About</a></li>
        </ul>
    </body>
    </html>
"""


def index(request):
    logger.info("Main page accessed")
    return HttpResponse(main_html)


def about(request):
    logger.info("About me accessed")
    return HttpResponse(about_html)