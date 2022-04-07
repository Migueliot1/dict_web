import justpy as jp

class HomePage:
    '''Represents Home page of the website.'''
    
    path = '/home'

    def serve(self):

        web_page = jp.QuasarPage(tailwind=True)

        div = jp.Div(a=web_page, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the Home page!', classes='text-4xl m2-2')
        jp.Div(a=div, text='There is going to be some text here...', classes='text-lg')

        return web_page
