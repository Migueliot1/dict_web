import justpy as jp
import definition
from webapp import layout

class DictionaryPage:
    '''Represents page which gvies a dictionary term for a word 
    user inputs in.
    '''

    path = '/dictionary'

    @classmethod
    def serve(cls, req):

        web_page = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=web_page)
        
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes='bg-gray-200 h-screen')
        jp.Div(a=div, text='Instant English Dictionary', classes='text-4xl m-2')
        jp.Div(a=div, text='Get the definition of any English word instantly as you type.', classes='text-lg px-2')

        input_div = jp.Div(a=div, classes='grid-cols-2')
        output_div = jp.Div(a=div, text='There is going to be an output here..', 
                            classes='m-2 p-2 text-lg border-2 h-40')

        input_box = jp.Input(a=input_div, placeholder='Type in a word here', outputdiv=output_div,
                classes='m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-blue-500 '
                'py-2 px-4')

        input_box.on('input', cls.get_definition)

        return web_page

    @staticmethod
    def get_definition(widget, msg):
        '''Static method which changes output so the term from dictionary appears.'''
        
        # Get input word
        in_value = widget.value

        defined = definition.Definition(in_value).get()

        # Construct a single string with all definitions
        result = ''
        for i in range(len(defined)):
            result += defined[i] + '\n'
        
        widget.outputdiv.text = result
    