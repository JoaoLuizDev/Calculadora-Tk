from tkinter import *
from tkinter import ttk
from tkinter import font

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = "#FFAB40"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=270)
frame_corpo.grid(row=1, column=0)

todos_valores = ""
ponto_usado = False

valor_texto = StringVar()

def entrada_valores(tecla):
    global todos_valores, ponto_usado

    if tecla.isdigit():

        if todos_valores == "0":
            todos_valores = tecla
        else:
            todos_valores += tecla
        valor_texto.set(todos_valores)
    elif tecla in ['+', '-', '*', '/', '**']:
        if todos_valores and todos_valores[-1] in ['+', '-', '*', '/', '**']:
            todos_valores = todos_valores[:-1] + tecla
        else:
            todos_valores += tecla
        valor_texto.set(todos_valores)
    elif tecla == '.':
        if not ponto_usado:
            todos_valores += tecla
            valor_texto.set(todos_valores)
            ponto_usado = True
    elif tecla == 'BackSpace':
        if todos_valores:
            if todos_valores[-1] == '.':
                ponto_usado = False
            todos_valores = todos_valores[:-1]
            valor_texto.set(todos_valores)
    elif tecla == '=':
        calcular()

def calcular():
    global todos_valores, ponto_usado

    try:
        resultado = eval(todos_valores)
        valor_texto.set(str(resultado))
        todos_valores = str(resultado)
    except Exception as e:
        valor_texto.set("Erro")
        todos_valores = ""
    ponto_usado = False

def limpar_tela():
    global todos_valores, ponto_usado
    todos_valores = ""
    valor_texto.set("")
    ponto_usado = False

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e",
                  justify=RIGHT, font=('Ivy', 18), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

fonte_Ivy = font.Font(family="Ivy", size=13, weight="bold")

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor5, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=limpar_tela)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, text="<--", width=5, height=2, bg=cor5, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('BackSpace'))
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('/'))
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('7'))
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('8'))
b_5.place(x=59, y=52)
b_6 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('9'))
b_6.place(x=118, y=52)
b_7 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('*'))
b_7.place(x=177, y=52)
b_8 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('4'))
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
             overrelief=RIDGE, command=lambda: entrada_valores('5'))
b_9.place(x=59, y=104)
b_10 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('6'))
b_10.place(x=118, y=104)
b_11 = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('-'))
b_11.place(x=177, y=104)
b_12 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('1'))
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('2'))
b_13.place(x=59, y=156)
b_14 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('3'))
b_14.place(x=118, y=156)
b_15 = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('+'))
b_15.place(x=177, y=156)

b_16 = Button(frame_corpo, text="0", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('0'))
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, fg=cor1, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('.'))
b_17.place(x=59, y=208)
b_18 = Button(frame_corpo, text="^", width=5, height=2, bg=cor5, fg=cor2, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=lambda: entrada_valores('**'))
b_18.place(x=118, y=208)
b_19 = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=fonte_Ivy, relief=RAISED,
              overrelief=RIDGE, command=calcular)
b_19.place(x=177, y=208)

janela.mainloop()
