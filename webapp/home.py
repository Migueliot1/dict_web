import justpy as jp

from webapp import page
from webapp import layout

class HomePage(page.Page):
    '''Represents Home page of the website.'''
    
    path = '/'

    @classmethod
    def serve(cls, req):

        web_page = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=web_page)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page!', classes='text-4xl m2-2')
        jp.Div(a=div, text='There is going to be some text here...', classes='text-lg')

        return web_page
    