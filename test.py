import tkinter

class MyApp:
    def __init__(self, myparent):
        # initialize root
        self.myparent = myparent

        # name of last button
        self.myLastButtonInvoked = ""

        # initialize container
        self.container1 = tkinter.Frame(myparent)
        self.container1.pack()

        # initialize button1, command binding
        self.button1 = tkinter.Button(self.container1)#, command=self.btn1_left)

        self.button1.focus_force() # focus button1 on startup

        # configure dictionary style
        self.button1['text'] = 'Press Me!'
        self.button1['background'] = 'green'

        self.button1.pack(side=tkinter.LEFT)

        # event binding
        self.button1.bind('<Button-1>', self.btn1_left)
        self.button1.bind('<Return>', self.btn1_left)
        self.button1.bind('<space>', self.btn1_left)


        # initialize button2, command binding
        self.button2 = tkinter.Button(self.container1)#, command=self.btn2_left)
        # configure method style
        self.button2.configure(text='Cancel')
        self.button2.configure(background='red')
        self.button2.pack(side=tkinter.LEFT)
        self.button2.bind('<Button-1>', self.btn2_left)
        self.button2.bind('<Return>', self.btn2_left)


        # initialize button3
        self.button3 = tkinter.Button(self.container1)
        # configure method style same line
        self.button3.configure(text='Join me?', background='cyan')
        self.button3.pack(side=tkinter.LEFT)

        # initialize button4 & configure
        self.button4 = tkinter.Button(self.container1, text='Goodbye', background='red')
        self.button4.pack(side=tkinter.LEFT)

    def btn1_left(self, event):
        self.myLastButtonInvoked = self.button1.widgetName
        print("Last button that was invoked: %s" % self.myLastButtonInvoked)
        print("button1Click event handler")
        if(self.button1['background'] == 'green'):
            self.button1['background'] = 'yellow'
        else:
            self.button1['background'] = 'green'

    def btn2_left(self, event):
        self.myLastButtonInvoked = self.button2.widgetName
        print("Last button that was invoked: %s" % self.myLastButtonInvoked)
        print("button1Click event handler")
        self.myparent.destroy()

def report_event(event):
    """Print a description of an event, based on its attributes.
    """
    event_name = {"2": "KeyPress", "4": "ButtonPress"}
    print("Time: %s" % event.time)
    print("EventType: %s, EventName: %s, EventWidgetID: %s, EventKeySymbol: %s"
    % (event.type, event_name[event.type], event.widget, event.keysym))

print("\n" * 100) # clear screen
root = tkinter.Tk()
myapp = MyApp(root)
root.mainloop()