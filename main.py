from tkinter import *
from tkinter.font import BOLD
from calc import Calculator_app
from tkinter import ttk


class Application(object):

    def __init__(self, root):
        self.root = root
        self.current_typing = ''
        self.prev_result = ''
        self.calc_obj = Calculator_app()
        self.init_window(root)
        self.init_buttons(root)
        self.init_result_screen(root)
        self.get_keyboard_events(root)

    # Initializing the window along with setting weights to columns and rows for responsive design

    def init_window(self, root):
        root.title('Py Calculator')
        root.geometry('290x310')
        Grid.columnconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 1, weight=1)
        Grid.columnconfigure(root, 2, weight=1)
        Grid.columnconfigure(root, 3, weight=1)
        Grid.rowconfigure(root, 0, weight=1)
        Grid.rowconfigure(root, 1, weight=1)
        Grid.rowconfigure(root, 2, weight=1)
        Grid.rowconfigure(root, 3, weight=1)
        Grid.rowconfigure(root, 4, weight=1)
        Grid.rowconfigure(root, 5, weight=1)
        Grid.rowconfigure(root, 6, weight=1)

    # Initializing the result screen with attached functions
    def init_result_screen(self, root):
        s = ttk.Style()
        s.configure('Danger.TFrame', background='red',
                    borderwidth=5, relief='raised')
        self.result_screen = ttk.Frame(root, style='Danger.TFrame').grid(
            column=0, row=0, columnspan=4, sticky=(N))
        self.tracking_equation_upper = ttk.Label(
            self.result_screen, textvariable=self.calc_obj.tkinter_upper, font=('Helvetica', 10, BOLD)).grid(row=0, column=0, columnspan=4, sticky=(E), pady=0, padx=5)
        self.result_text_lower = ttk.Label(
            self.result_screen, textvariable=self.calc_obj.tkinter_lower, font=('Helvetica', 20, BOLD)).grid(row=1, column=0, columnspan=4, sticky=(E), pady=0, padx=5)

   # FUnction to initialize the buttons attaching it to it's location on the frame grid as well as attaching fuctions to it

    def init_buttons(self, root):
        '''
        First line special operators
        '''

        self.button_C = ttk.Button(
            root, text='C', style='my.TButton', command=lambda: self.calc_obj.clear_selections()).grid(row=2, column=0, columnspan=2, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_backSpace = ttk.Button(
            root, text='⌫', command=lambda: self.calc_obj.backSpace(), style='my.TButton').grid(row=2, column=2, columnspan=2, sticky=(N, S, E, W), padx=1, pady=1)

        '''
        Digits Buttons:
            - each based on it's location on the grid
            - self.calc_obj.typing() method used to add the number clicked on to the calc class tracking
        '''
        s = ttk.Style()
        s.configure('my.TButton', font=('Helvetica', 12, BOLD))
        self.button_1 = ttk.Button(
            root, text='1', command=self.type_digit('1'), style='my.TButton').grid(row=5, column=0, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_2 = ttk.Button(
            root, text='2', command=self.type_digit('2'), style='my.TButton').grid(row=5, column=1, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_3 = ttk.Button(
            root, text='3', command=self.type_digit('3'), style='my.TButton').grid(row=5, column=2, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_4 = ttk.Button(
            root, text='4', command=self.type_digit('4'), style='my.TButton').grid(row=4, column=0, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_5 = ttk.Button(
            root, text='5', command=self.type_digit('5'), style='my.TButton').grid(row=4, column=1, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_6 = ttk.Button(
            root, text='6', command=self.type_digit('6'), style='my.TButton').grid(row=4, column=2, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_7 = ttk.Button(
            root, text='7', command=self.type_digit('7'), style='my.TButton').grid(row=3, column=0, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_8 = ttk.Button(
            root, text='8', command=self.type_digit('8'), style='my.TButton').grid(row=3, column=1, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_9 = ttk.Button(
            root, text='9', command=self.type_digit('9'), style='my.TButton').grid(row=3, column=2, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_0 = ttk.Button(
            root, text='0', command=self.type_digit('0'), style='my.TButton').grid(row=6, column=1, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_decimalPoint = ttk.Button(
            root, text='.', command=lambda: self.calc_obj.add_decimal_point(), style='my.TButton').grid(row=6, column=0, sticky=(N, S, E, W), padx=1, pady=1)

        '''
        Math Operators Buttons:
            - Based on location on the grid
        '''
        self.button_divide = ttk.Button(
            root, text='/', command=lambda: self.calc_obj.select_math_operator('/'), style='my.TButton').grid(row=3, column=3, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_multiply = ttk.Button(
            root, text='*', command=lambda: self.calc_obj.select_math_operator('*'), style='my.TButton').grid(row=4, column=3, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_substract = ttk.Button(
            root, text='-', command=lambda: self.calc_obj.select_math_operator('-'), style='my.TButton').grid(row=5, column=3, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_sum = ttk.Button(
            root, text='+', command=lambda: self.calc_obj.select_math_operator('+'), style='my.TButton').grid(row=6, column=3, sticky=(N, S, E, W), padx=1, pady=1)
        self.button_result = ttk.Button(
            root, text='=', command=lambda: self.calc_obj.press_equal(), style='my.TButton').grid(row=6, column=2, sticky=(N, S, E, W), padx=1, pady=1)

    def type_digit(self, digit):
        return lambda: self.calc_obj.typing(digit)

    def get_keyboard_events(self, root):
        root.bind('<KeyPress-0>', lambda e: self.calc_obj.typing('0'))
        root.bind('<KeyPress-1>', lambda e: self.calc_obj.typing('1'))
        root.bind('<KeyPress-2>', lambda e: self.calc_obj.typing('2'))
        root.bind('<KeyPress-3>', lambda e: self.calc_obj.typing('3'))
        root.bind('<KeyPress-4>', lambda e: self.calc_obj.typing('4'))
        root.bind('<KeyPress-5>', lambda e: self.calc_obj.typing('5'))
        root.bind('<KeyPress-6>', lambda e: self.calc_obj.typing('6'))
        root.bind('<KeyPress-7>', lambda e: self.calc_obj.typing('7'))
        root.bind('<KeyPress-8>', lambda e: self.calc_obj.typing('8'))
        root.bind('<KeyPress-9>', lambda e: self.calc_obj.typing('9'))
        root.bind('<KeyPress-.>', lambda e: self.calc_obj.add_decimal_point())
        root.bind('<KeyPress-+>',
                  lambda e: self.calc_obj.select_math_operator('+'))
        root.bind('<KeyPress-->',
                  lambda e: self.calc_obj.select_math_operator('-'))
        root.bind('<KeyPress-/>',
                  lambda e: self.calc_obj.select_math_operator('/'))
        root.bind('<KeyPress-*>',
                  lambda e: self.calc_obj.select_math_operator('*'))
        root.bind('<KeyPress-*>',
                  lambda e: self.calc_obj.select_math_operator('*'))
        root.bind('<KeyPress-Return>',
                  lambda e: self.calc_obj.press_equal())


root = Tk()
Application(root)
root.mainloop()





