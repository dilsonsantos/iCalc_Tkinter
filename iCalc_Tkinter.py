# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:35:34 2023

@author: Dilson Santos
"""

import tkinter.font

class Calculadora:
    def __init__(self):
        self.a = None
        self.b = None
        self.operacao = None
        self.resultado = None
        self.contagem_comandos = 0
        self.ponto_decimal = False
        self.metodo_ativo = True

    def selecionar_operacao(self):
        self.metodo_ativo = False
        if self.operacao == "+":
            self.somar()
        elif self.operacao == "-":
            self.subtrair()
        elif self.operacao == "*":
            self.multiplicar()
        elif self.operacao == "/":
            self.dividir()

    def ponto_decimal(self):
        if self.metodo_ativo:
            self.selecionar_operacao()
            self.metodo_ativo = True
        global resultado
        if self.a is None:
            resultado.set("{}.".format(self.a))
            self.a = float(0)
        elif self.b is None:
            resultado.set("{}.".format(self.a))
            self.a = float(self.a)
        elif self.b is not None:
            resultado.set("{}.".format(self.b))
            self.b = float(self.b)
        self.ponto_decimal = True

    def somar(self):
        global resultado
        if self.operacao == "-":
            self.subtrair()
        elif self.operacao == "*":
            self.multiplicar()
        elif self.operacao == "/":
            self.dividir()
        if self.b is not None:
            self.resultado = self.a + self.b
            self.a = self.resultado
            self.b = None
            resultado.set("{}".format(self.resultado))
        self.contagem_comandos += 1
        self.operacao = "+"

    def subtrair(self):
        global resultado
        if self.operacao == "+":
            self.somar()
        elif self.operacao == "*":
            self.multiplicar()
        elif self.operacao == "/":
            self.dividir()
        if self.operacao == "*":
            self.multiplicar()
        elif self.operacao == "/":
            self.dividir()
        if self.b is not None:
            self.resultado = self.a - self.b
            self.a = self.resultado
            self.b = None
            resultado.set("{}".format(self.resultado))
        self.operacao = "-"
        self.contagem_comandos += 1

    def multiplicar(self):
        global resultado
        if self.operacao == "+":
            self.somar()
        elif self.operacao == "-":
            self.subtrair()
        elif self.operacao == "/":
            self.dividir()

        if self.b is not None:
            self.resultado = self.a * self.b
            self.a = self.resultado
            self.b = None
            resultado.set("{}".format(self.resultado))
        self.contagem_comandos += 1
        self.operacao = "*"

    def dividir(self):
        global resultado
        if self.operacao == "+":
            self.somar()
        elif self.operacao == "-":
            self.subtrair()
        elif self.operacao == "*":
            self.multiplicar()

        if self.b is not None:
            if self.b == 0:
                self.resultado = 0
            else:
                if self.a % self.b == 0:
                    self.resultado = self.a // self.b
                else:
                    self.resultado = self.a / self.b
            resultado.set("{}".format(self.resultado))
            self.a = self.resultado
            self.b = None
        self.contagem_comandos += 1
        self.operacao = "/"

    def limpar(self):
        global resultado
        self.a = None
        self.b = None
        self.operacao = ""
        self.resultado = None
        resultado.set("0")
        self.metodo_ativo = True
        self.contagem_comandos = 0
        self.ponto_decimal = False

    def negativo(self):
        global resultado
        if self.metodo_ativo:
            self.selecionar_operacao()
            self.metodo_ativo = True
        if self.a is not None:
            self.resultado = -self.a
            self.a *= -1
            resultado.set("{}".format(self.resultado))

    def porcentagem(self):
        global resultado
        if self.metodo_ativo:
            self.selecionar_operacao()
            self.metodo_ativo = True
        if self.a is not None:
            self.resultado = self.a / 100
            self.a = self.resultado
            resultado.set("{}".format(self.resultado))
        self.contagem_comandos += 1

    def igual(self):
        global resultado
        self.selecionar_operacao()
        if self.resultado is not None:
            resultado.set("{}".format(self.resultado))
        self.contagem_comandos = 0
        self.metodo_ativo = 0
        self.operacao = "="

    def obter_resultado(self):
        return self.resultado

    def definir_resultado(self, resultado):
        self.resultado = resultado

    def numeros(self, parametro):
        global resultado
        if self.operacao == "=":
            self.limpar()
        if self.ponto_decimal is False:
            if self.contagem_comandos == self.contagem_comandos != 0:
                if self.a and self.b is not None and self.resultado is not None:
                    self.a = self.resultado
                    a = "{}{}".format(self.b, parametro)
                    self.b = a
                    resultado.set(a)
                if self.a is not None and self.b is None:
                    a = "{}{}".format(self.a, parametro)
                    self.a = int(a)
                    resultado.set("{}".format(int(a)))
                elif self.a is not None and self.b is not None:
                    a = "{}{}".format(self.b, parametro)
                    self.b = int(a)
                    resultado.set("{}".format(int(a)))
            else:
                if self.a and self.b is not None and self.resultado is not None:
                    self.resultado = self.a
                    self.b = parametro
                    resultado.set("{}".format(self.b))
                elif self.b is None and self.a is not None:
                    self.b = parametro
                    resultado.set("{}".format(self.b))
                elif self.b is None and self.a is None:
                    self.a = parametro
                    resultado.set("{}".format(self.a))

    def ponto_decimal(self):
        if self.ponto_decimal:
            return
        self.ponto_decimal = True
        global resultado
        if self.a is None:
            self.a = "0"
        elif self.b is None:
            self.a += "."
        else:
            self.b += "."
        resultado.set("{}".format(self.a if self.b is None else self.b))

    def adicionar_zero(self, parametro):
        global resultado
        if self.operacao == "=":
            self.limpar()
        if self.ponto_decimal is False:
            if self.contagem_comandos == self.contagem_comandos != 0:
                if self.a and self.b is not None and self.resultado is not None:
                    self.a = self.resultado
                    a = "{}{}".format(self.b, parametro)
                    self.b = a
                    resultado.set(a)
                if self.a is not None and self.b is None:
                    a = "{}{}".format(self.a, parametro)
                    self.a = int(a)
                    resultado.set("{}".format(int(a)))
                elif self.a is not None and self.b is not None:
                    a = "{}{}".format(self.b, parametro)
                    self.b = int(a)
                    resultado.set("{}".format(int(a)))
            else:
                if self.a and self.b is not None and self.resultado != 0:
                    self.resultado = self.a
                    self.b = parametro
                    resultado.set("{}".format(self.b))
                elif self.b is None and self.a is not None:
                    self.b = parametro
                    resultado.set("{}".format(self.b))
                elif self.b is None and self.a is None:
                    self.a = parametro
                    resultado.set("{}".format(self.a))

def play():
    janela_principal.mainloop()

janela_principal = tkinter.Tk()
janela_principal.title("Calculadora Python")
janela_principal.geometry("480x640")
janela_principal.configure(background="black", padx=5, pady=5)
janela_principal.minsize(300, 440)
janela_principal.maxsize(300, 440)

fonte = tkinter.font.Font(font="TkHeadingFont", weight="bold")

resultado = tkinter.StringVar()
label = tkinter.Label(
    janela_principal,
    textvariable=resultado,
    font=(fonte, 40),
    background="black",
    fg="white",
    borderwidth=0,
    height=0,
    width=0,
)
label.grid(row=0, column=0, columnspan=4, sticky="e", padx=2, pady=2)

calculadora = Calculadora()

botoes_calculadora = [
    [
        ("C", 1, lambda: calculadora.limpar()),
        ("+/-", 1, lambda: calculadora.negativo()),
        ("%", 1, lambda: calculadora.porcentagem()),
        ("÷", 1, lambda: calculadora.dividir()),
    ],
    [
        ("7", 1, lambda: calculadora.numeros(7)),
        ("8", 1, lambda: calculadora.numeros(8)),
        ("9", 1, lambda: calculadora.numeros(9)),
        ("x", 1, lambda: calculadora.multiplicar()),
    ],
    [
        ("4", 1, lambda: calculadora.numeros(4)),
        ("5", 1, lambda: calculadora.numeros(5)),
        ("6", 1, lambda: calculadora.numeros(6)),
        ("-", 1, lambda: calculadora.subtrair()),
    ],
    [
        ("1", 1, lambda: calculadora.numeros(1)),
        ("2", 1, lambda: calculadora.numeros(2)),
        ("3", 1, lambda: calculadora.numeros(3)),
        ("+", 1, lambda: calculadora.somar()),
    ],
    [
        ("0", 2, lambda: calculadora.numeros(0)),
        (".", 1, lambda: calculadora.ponto_decimal()),
        ("=", 1, lambda: calculadora.igual()),
    ],
]

frame = tkinter.Frame(janela_principal, background="black")
frame.grid(row=1, column=0, sticky="nsew", padx=2, pady=2)
row = 0

# As imagens dos botoes
laranja = "orange.png"
cinza_light = "lightgrey.png"
cinza_dark = "darkgrey.png"
cinza_claro_duplo = "dg1.png"

for botoes in botoes_calculadora:
    data = 0
    for texto, valor, comando in botoes:
        if (
            "{}".format(texto) in ["-", "+", "=", "÷", "x"]
        ):
            botao = tkinter.Button(
                frame,
                image="laranja",
                compound="center",
                background="black",
                font=[fonte, 20, "bold"],
                activebackground="black",
                text="{}".format(texto),
                fg="white",
                border=0,
                command=comando,
            )
            botao.grid(row=row, column=data, columnspan=valor, sticky="nsew", padx=2, pady=2)
            data += valor
        elif "{}".format(texto) in ["C", "+/-", "%"]:
            botao = tkinter.Button(
                frame,
                image="cinza_light",
                compound="center",
                background="black",
                font=(fonte, 20),
                activebackground="black",
                text="{}".format(texto),
                fg="white",
                border=0,
                command=comando,
            )
            botao.grid(
                row=row, column=data, columnspan=valor, sticky="nsew", padx=2, pady=2
            )
        elif "{}".format(texto) == "0":
            botao = tkinter.Button(
                frame,
                image="cinza_dark_duplo",
                compound="center",
                background="black",
                font=(fonte, 20),
                activebackground="black",
                text="{}".format(texto),
                fg="white",
                border=0,
                command=comando,
            )
            botao.grid(
                row=row, column=data, columnspan=2, sticky="nsew", padx=2, pady=2
            )
        else:
            botao = tkinter.Button(
                frame,
                image="cinza_dark",
                compound="center",
                background="black",
                font=(fonte, 20),
                activebackground="black",
                text="{}".format(texto),
                fg="white",
                border=0,
                command=comando,
            )
            botao.grid(
                row=row, column=data, columnspan=valor, sticky="nsew", padx=2, pady=2
            )
        data += valor
    row += 1

if __name__ == "__main__":
    play()
