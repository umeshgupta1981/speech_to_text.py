import tkinter


class Calculator_app(object):
    '''
    initializing the class with variables:
        - result: holding result from calculation
        - tkinter_lower: holds the value for what you type into the equation and communicates it to the GUI
        - tkinter_upper: holds the string representation for the equation
        - left & right: the left & right sides of the equation
        - math_operator_selected: flag if pressed on math operator
        - math_operator: holds the selected math operator
        - decimal_flag: flag to change calculation to Floats
    '''

    def __init__(self):
        self.pressed_equal_Flag = False
        self.result = 0
        self.tkinter_lower = tkinter.StringVar()
        self.tkinter_upper = tkinter.StringVar()
        self.left = ''
        self.right = ''
        self.math_operator_selected = False
        self.math_operator = None
        self.decimal_flag = False
        self.operationAsEqualFlag = False

    # Calculate once equal button clicked in GUI
    def computation(self):
        if self.left == '' and self.math_operator_selected == False:
            self.result = 0
            self.clear_selections()
        elif self.math_operator_selected:
            if self.math_operator == '+':
                self.sum()
            elif self.math_operator == '-':
                self.substract()
            elif self.math_operator == '/':
                self.divide()
            elif self.math_operator == '*':
                self.multiply()
        else:
            pass
        print('Result: ' + str(self.result))

    # Add Numbers to right or left depend on which side of the equation right now
    def typing(self, digit):
        if self.math_operator_selected and self.result != 0:
            self.left = self.result
            self.right += str(digit)
            self.tkinter_lower.set(self.right)
            print('right: ' + str(self.right))
        elif self.math_operator_selected:
            self.right += str(digit)
            self.tkinter_lower.set(self.right)
            print('right: ' + str(self.right))
        elif self.pressed_equal_Flag:
            self.clear_selections()
            self.left += str(digit)
            self.tkinter_lower.set(self.left)
            print('left: ' + str(self.left))
            self.pressed_equal_Flag = False
        else:
            self.left += str(digit)
            self.tkinter_lower.set(self.left)
            print('left: ' + str(self.left))

        self.pressed_equal_Flag = False

    # Selecting Math operator based on what was pressed triggered by GUI
    def select_math_operator(self, operator):
        if self.math_operator_selected and self.left != '' and self.right != '':
            self.operationAsEqualFlag = True
            self.computation()
            self.math_operator = operator
            self.change_tkinter_vars_on_equal()
            self.operationAsEqualFlag = False
            self.right = ''
            self.left = self.result
            print('selected operator: ' + self.math_operator)
        elif self.math_operator_selected:
            self.math_operator = operator
            self.tkinter_upper.set(
                str(self.tkinter_lower.get()) + ' ' + operator)
            print('selected operator: ' + self.math_operator)
        else:
            self.math_operator = operator
            self.math_operator_selected = True
            self.tkinter_upper.set(
                str(self.tkinter_lower.get()) + ' ' + operator)
            print('selected operator: ' + self.math_operator)

    # Clearing on "C" Press
    def clear_selections(self):
        self.decimal_flag = False
        self.result = 0
        self.left = ''
        self.right = ''
        self.math_operator_selected = False
        self.math_operator = None
        self.tkinter_upper.set('')
        self.tkinter_lower.set('0')

    '''
    Math Operations' Functions
    '''

    def sum(self):
        if self.decimal_flag:
            self.result = float(self.left) + float(self.right)
        else:
            self.result = int(self.left) + int(self.right)
        self.change_tkinter_vars_on_equal()
        self.right = ''
        self.left = self.result

        print("left here: " + str(self.left))

    def substract(self):
        if self.decimal_flag:
            self.result = float(self.left) - float(self.right)
        else:
            self.result = int(self.left) - int(self.right)

        self.change_tkinter_vars_on_equal()
        self.right = ''
        self.left = self.result

        print("left here: " + str(self.left))

    def divide(self):
        if self.decimal_flag:
            self.result = float(self.left) / float(self.right)
        else:
            self.result = int(self.left) / int(self.right)

        self.change_tkinter_vars_on_equal()
        self.right = ''
        self.left = self.result

        print("left here: " + str(self.left))

    def multiply(self):
        if self.decimal_flag:
            self.result = float(self.left) * float(self.right)
        else:
            self.result = int(self.left) * int(self.right)
        self.change_tkinter_vars_on_equal()
        self.right = ''
        self.left = self.result

        print("left here: " + str(self.left))

    # Updates tkinter GUI vars with values on equal button press
    def change_tkinter_vars_on_equal(self):
        if self.operationAsEqualFlag:
            self.tkinter_upper.set(
                str(self.result) + ' ' + str(self.math_operator))
            self.tkinter_lower.set(str(self.result))

        else:
            self.tkinter_upper.set(
                self.tkinter_upper.get() + ' ' + self.right + ' =')
            self.tkinter_lower.set(self.result)

    # deletion to current typing

    def backSpace(self):
        if self.math_operator_selected and self.right != '':
            if self.right[:-1] == '.':
                self.decimal_flag = False
            self.right = self.right[:-1]
            self.tkinter_lower.set(self.right)
        elif (not self.math_operator_selected) and self.left != '':
            if self.left[:-1] == '.':
                self.decimal_flag = False
            self.left = self.left[:-1]
            self.tkinter_lower.set(self.left)
        else:
            pass

    # Checks if already added decimal point or not
    def add_decimal_point(self):
        self.decimal_flag = True
        if self.math_operator_selected:
            if '.' in self.right:
                pass
            else:
                self.typing('.')
        elif not self.math_operator_selected:
            if '.' in self.left:
                pass
            else:
                self.typing('.')
        else:
            pass

    def press_equal(self):
        self.computation()
        self.math_operator_selected = False
        self.pressed_equal_Flag = True