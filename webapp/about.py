import justpy as jp

class AboutPage:
    '''Represents About page which has a general info about the website 
    and its functionality.
    '''

    path = '/about'

    def serve(self):

        web_page = jp.QuasarPage(tailwind=True)

        div = jp.Div(a=web_page, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='This is the About page!', classes='text-4xl m2-2')
        jp.Div(a=div, text='There is going to be About text here...', classes='text-lg')
    
        return web_page
