import justpy as jp

class DictionaryPage:
    '''Represents page which gvies a dictionary term for a word 
    user inputs in.
    '''

    path = '/dictionary'

    @classmethod
    def serve(cls, req):

        web_page = jp.QuasarPage(tailwind=True)

        div = jp.Div(a=web_page, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')
        jp.Div(a=div, text='Get the definition of any English word instantly as you type.', classes='text-lg px-2')

        jp.Input(a=div, placeholder='Type in a word here',
                classes='m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-blue-500 '
                'py-2 px-4')
        jp.Div(a=div, text='There is going to be an output here..', 
                classes='m-2 p-2 text-lg border-2 h-40')

        return web_page
