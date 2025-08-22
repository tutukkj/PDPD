# Projeto PDPD - Implementação de modelos teóricos de consumo de energia para VANTs (Drones)

## Sobre o Projeto
Projeto de pesquisa de Iniciação Científica da UFABC, desenvolvido no programa *Pesquisando Desde o Primeiro Dia (PDPD)*. Oferece uma ferramenta em Python para cálculo de consumo energético e potência em drones de asa rotativa e asa fixa, baseada em modelos teóricos validados pela literatura.

##  Funcionalidades
- **Cálculo**: Estimativa de potência instantânea ou energia consumida ao longo do tempo
- **Modelos Teóricos Validados**: Equações para drones de asa rotativa e asa fixa
- **Banco de Dados Editável**: Parâmetros armazenados em CSV para fácil adição de novos modelos
- **Uso por Terminal**: Execução e parametrização direta via terminal

##  Pré-requisitos
- Python 3.10 ou superior
- Bibliotecas: `pandas` e `numpy`

## Como Usar

### 1. Clonar e Instalar
```bash
git clone https://github.com/tutukkj/PDPD.git
cd projeto-vants
pip install -r requirements.txt
```

### 2. Configurar Base de Dados
Os parâmetros dos drones estão em `data/drones.csv` (delimitador `;`), assim sendo possivel adicionar novos modelos de drones com facilidade. Exemplo da estrutura:

| nome_modelo              | tipo     | cf | p  | s  | A   | omega | R  | k  | W   | Utip | V  | v0 | d0 | Cd0 | ar | e  | T  |
|----------------------|----------|----|----|----|-----|-------|----|----|-----|------|----|----|----|-----|----|----|----|
| Modelo_generico      | rotativa | ...| ...| ...| ... | ...  | ...| ...| ... | ... | ...| ...| ...| ... | ...| ...| ...|
| PHX                  | fixa     | ...| ...| ...| ... | ...  | ...| ...| ... | ... | ...| ...| ...| ... | ...| ...| ...|

### 3. Executar o Programa
**Parâmetros:**
- `-m/--modelo`: Nome do drone (obrigatório)
- `-t/--tempo`: Tempo de voo em minutos (obrigatório)
- `-c/--calculo`: Tipo de cálculo (`potencia` ou `energia`) (obrigatório)

**Exemplos:**
```bash
# Calcular energia para drone de asa rotativa
python src/main.py --m Modelo_generico --t 55 --c energia

# Calcular potência para drone de asa fixa
python src/main.py --m PHX --t 30 --c potencia
```

## Estrutura do Projeto
```
.
├── data/
│   └── dados.csv          # Banco de dados dos modelos
├── main.py 
├── README.md
└── requirements.txt
```
