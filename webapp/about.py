import justpy as jp

from webapp import page
from webapp import layout

class AboutPage(page.Page):
    '''Represents About page which has a general info about the website 
    and its functionality.
    '''
    path = '/about'

    @classmethod
    def serve(cls, req):

        web_page = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=web_page)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the About page!', classes='text-4xl m2-2')
        jp.Div(a=div, text='There is going to be About text here...', classes='text-lg')
    
        return web_page
