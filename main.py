import argparse
import pandas as pd
import math

def carregar(nome_modelo, caminho="dados.csv"):
    df = pd.read_csv(caminho, sep=';', encoding='utf-8-sig')
    return df[df['nome_modelo'] == nome_modelo].iloc[0]

def processar_modelo(tipo, modelo, tempo, calculo):
    if tipo == "rotativa" and calculo == "potencia":
        cf = modelo['cf']
        p = modelo['p']
        s = modelo['s']
        A = modelo['A']
        omega = modelo['omega']
        R = modelo['R']
        k = modelo['k']
        W = modelo['W']
        Utip = modelo['Utip']
        V = modelo['V']
        v0 = modelo['v0']
        d0 = modelo['d0']

        P0 = cf / 8 * p * s * A * omega ** 3 * R ** 3
        Pi = (1 + k) * (W ** 1.5) / math.sqrt(2 * p * A)
        Blade_Profile = P0 * (1 + 3 * V ** 2 / Utip ** 2)
        parte1 = 1 + (V ** 4) / (4 * v0 ** 4)
        parte2 = (V ** 2) / (2 * v0 ** 2)
        Induced = Pi * math.sqrt(parte1 - parte2)
        parasite = 0.5 * d0 * p * s * A * V ** 3
        pv = Blade_Profile + Induced + parasite

        print(f"Potência total estimada: {pv:.4f} W")

    elif tipo == "rotativa" and calculo == "energia":
        cf = modelo['cf']
        p = modelo['p']
        s = modelo['s']
        A = modelo['A']
        omega = modelo['omega']
        R = modelo['R']
        k = modelo['k']
        W = modelo['W']
        Utip = modelo['Utip']
        V = modelo['V']
        v0 = modelo['v0']
        d0 = modelo['d0']

        P0 = cf / 8 * p * s * A * omega**3 * R**3
        Pi = (1 + k) * (W**1.5) / math.sqrt(2 * p * A)
        Blade_Profile = P0 * (1 + 3 * (V**2) / (Utip**2))
        termo_interno = (1 + (V**4) / (4 * v0**4)) - ((V**2) / (2 * v0**2))
        termo_interno = max(termo_interno, 0) 
        Induced = Pi * math.sqrt(termo_interno)
        parasite = 0.5 * d0 * p * s * A * V**3

        P_total = Blade_Profile + Induced + parasite  
        E0 = P_total * tempo  

        print(f"Energia estimada: {E0:.4f} J")



    elif tipo == "fixa" and calculo == "potencia":
        p = modelo['p']
        Cd0 = modelo['Cd0']
        s = modelo['s']
        ar = modelo['ar']
        W = modelo['W']
        e = modelo['e']
        T = float(modelo['T'])
        v = modelo['V']

        C1 = (p * Cd0 * s) / 2
        C2 = (2 * W ** 2) / (math.pi * e * ar) * p * s

        print(f"Potência parasita: {C1:.4f} W")
        print(f"Potência induzida: {C2:.4f} W")

    elif tipo == "fixa" and calculo == "energia":
        p = modelo['p']
        Cd0 = modelo['Cd0']
        s = modelo['s']
        ar = modelo['ar']
        W = modelo['W']
        e = modelo['e']
        T = float(modelo['T'])
        v = modelo['V']

        if tempo > T:
            print("tempo de voo maior que o tempo máximo do VANT")
        else:
            C1 = (p * Cd0 * s) / 2
            C2 = (2 * W ** 2) / (math.pi * e * ar) * p * s
            Elsf = tempo * (C1 * v ** 3 + C2 / v)
            print(f"Energia estimada: {Elsf:.4f} J")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tempo", required=True, type=float, help="Tempo de voo")
    parser.add_argument("-c", "--calculo", required=True, help="potencia ou energia")
    parser.add_argument("-m", "--modelo", required=True, help="Nome do modelo")
    args = parser.parse_args()

    modelo = carregar(args.modelo)
    tipo = modelo['tipo'].strip().lower()
    tempo = float(args.tempo)
    processar_modelo(tipo, modelo, tempo, args.calculo.lower())


main()
