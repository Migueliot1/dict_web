import justpy as jp

class HomePage:
    '''Represents Home page of the website.'''
    
    path = '/'

    @classmethod
    def serve(cls, req):

        web_page = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=web_page, view='hHh lpR fFf')
        header = jp.QHeader(a=layout, eleveated=True, classes='bg-primary text-white')
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=False, v_model='leftDrawerOpen', side='left', 
                            bordered=True)
        
        # Make a scroller area and add links to pages in it
        scroller = jp.QScrollArea(a=drawer, classes='fit')
        qlist = jp.QList(a=scroller)
        a_classes = 'p-2 m-2 text-lg text-blue-400 hover:text-blue-700'
        jp.A(a=qlist, text='Home', href='/home', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='Dictionary', href='/dictionary', classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text='About', href='/about', classes=a_classes)
        jp.Br(a=qlist)
        
        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon='menu',
                    click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text='Instant Dictionary')

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=web_page, classes='bg-gray-200 h-screen')
        jp.Div(a=container, text='This is the Home page!', classes='text-4xl m2-2')
        jp.Div(a=container, text='There is going to be some text here...', classes='text-lg')

        return web_page
    
    @staticmethod
    def move_drawer(widget, msg):
        '''Static method which hides and makes the drawer appear upon clicking.'''

        if widget.drawer.value:
            widget.drawer.value = False
        elif not widget.drawer.value:
            widget.drawer.value = True