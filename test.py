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

        button_name = "OK"
        # initialize button1, command binding
        self.button1 = tkinter.Button(self.container1, command=self.buttonHandler(button_name, 1, 'Good stuff!'))

        self.button1.focus_force() # focus button1 on startup

        # configure dictionary style
        self.button1['text'] = 'Press Me!'
        self.button1['background'] = 'green'

        self.button1.pack(side=tkinter.LEFT)

        # initialize button2, command binding
        self.button2 = tkinter.Button(self.container1)#, command=self.btn2_left)
        # configure method style
        self.button2.configure(text='Cancel')
        self.button2.configure(background='red')
        self.button2.pack(side=tkinter.LEFT)
        self.button2.bind('<Button-1>', self.btn2_left)
        self.button2.bind('<Return>', self.btn2_left)

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

    def buttonHandler(self, arg1, arg2, arg3):
        print('buttonHandler routine received arguments: %s %s %s' % (arg1.ljust(8), arg2, arg3))

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