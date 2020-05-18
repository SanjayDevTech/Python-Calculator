from tkinter import *

expression = ""


def catVar(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clear(length):
    global expression
    if length == "all":
        expression = ""
        
    else:
        expression = expression[:-1]
    equation.set(expression)

def calculate():
    global expression
    try:
        expression = str(eval(expression))
        equation.set(expression)
    except SyntaxError:
        expression = ""
        equation.set("Syntax error")
    except:
        expression = ""
        equation.set("Error")

if __name__ == '__main__':
    
    
    root = Tk()
    root.title("Calculator")
    root.configure(background="light green")
    root.minsize(275,400)
    root.maxsize(275,400)
    equation = StringVar()
    expression_field = Entry(root, textvariable=equation)
    expression_field.grid(columnspan=8, ipadx=75)

    oneButton = Button(root, text='1',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(1))
    oneButton.grid(row=2, column=0,columnspan=2)

    twoButton = Button(root, text='2',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(2))
    twoButton.grid(row=2, column=2,columnspan=2)

    threeButton = Button(root, text='3',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(3))
    threeButton.grid(row=2, column=4,columnspan=2)

    fourButton = Button(root, text='4',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(4))
    fourButton.grid(row=3, column=0,columnspan=2)

    fiveButton = Button(root, text='5',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(5))
    fiveButton.grid(row=3, column=2,columnspan=2)

    sixButton = Button(root, text='6',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(6))
    sixButton.grid(row=3, column=4,columnspan=2)

    sevenButton = Button(root, text='7',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(7))
    sevenButton.grid(row=4, column=0,columnspan=2)

    eightButton = Button(root, text='8',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(8))
    eightButton.grid(row=4, column=2,columnspan=2)

    nineButton = Button(root, text='9',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(9))
    nineButton.grid(row=4, column=4,columnspan=2)

    resetButton = Button(root, text='Reset',bg ='red',fg='white',width=8,height=4,command=lambda: clear("all"))
    resetButton.grid(row=5, column=0,columnspan=2)

    zeroButton = Button(root, text='0',bg ='red',fg='white',width=8,height=4,command=lambda: catVar(0))
    zeroButton.grid(row=5, column=2,columnspan=2)

    clearButton = Button(root, text='Clear',bg ='red',fg='white',width=8,height=4,command=lambda: clear("1"))
    clearButton.grid(row=5, column=4,columnspan=2)

    equalButton = Button(root, text=' = ',bg ='red',fg='white',width=18,height=4,command=lambda: calculate())
    equalButton.grid(row=6, column=0,columnspan=4)

    plusButton = Button(root, text=' + ',bg ='red',fg='white',width=8,height=4,command=lambda: catVar('+'))
    plusButton.grid(row=2, column=6,columnspan=2)

    subButton = Button(root, text=' - ',bg ='red',fg='white',width=8,height=4,command=lambda: catVar('-'))
    subButton.grid(row=3, column=6,columnspan=2)

    mulButton = Button(root, text=' * ',bg ='red',fg='white',width=8,height=4,command=lambda: catVar('*'))
    mulButton.grid(row=4, column=6,columnspan=2)

    divButton = Button(root, text=' / ',bg ='red',fg='white',width=8,height=4,command=lambda: catVar('/'))
    divButton.grid(row=5, column=6,columnspan=2)

    powerButton = Button(root, text=' ^ ',bg ='red',fg='white',width=8,height=4,command=lambda: catVar('**'))
    powerButton.grid(row=6, column=6,columnspan=2)

    rootButton = Button(root, text=' √ ',bg ='red',fg='white',width=8,height=4,command=lambda: catVar('**(0.5)'))
    rootButton.grid(row=6, column=4,columnspan=2)
    
    root.mainloop()
