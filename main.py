# Starting the app from here
import inspect

import justpy as jp

from webapp import page
from webapp.home import HomePage
from webapp.about import AboutPage
from webapp.dictionary import DictionaryPage

from definition import Definition


imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)


jp.justpy(port=8001)
