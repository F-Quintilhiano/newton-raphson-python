import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import sympy as sp

from newton_algoritmo import executar_metodo, avaliar_funcao

# --- Função Auxiliar para Derivada Simbólica ---
def calcular_derivada_automatica(texto_funcao):
    """
    Usa o SymPy para calcular a derivada da string fornecida.
    """
    if not texto_funcao:
        return ""
    
    try:
        x = sp.symbols('x')
        expr = sp.sympify(texto_funcao.replace('^', '**'))
        derivada = sp.diff(expr, x)
        
       
        return str(derivada).replace('**', '^')
    except:
    
        return ""

# --- Configuração da Página ---
st.set_page_config(page_title="Newton-Raphson", layout="wide")
st.title("Método de Newton-Raphson")

# --- Painel Lateral de Inputs ---
st.sidebar.header("Parâmetros")

# 1. Campo da Função
f_str = st.sidebar.text_input("Função f(x)", value="x^3 - 2*x - 5")

# 2. Cálculo Automático da Derivada
# Calculamos a derivada baseada no que foi digitado acima
derivada_sugerida = calcular_derivada_automatica(f_str)

# 3. Campo da Derivada
# O parametro 'value' recebe o calculo automático. 
# Se o SymPy falhar (erro de sintaxe), usamos um valor padrão seguro.
valor_inicial_derivada = derivada_sugerida if derivada_sugerida else "3*x^2 - 2"
df_str = st.sidebar.text_input("Derivada f'(x)", value=valor_inicial_derivada)

x0 = st.sidebar.number_input("Chute Inicial (x0)", value=2.0, step=0.1)
epsilon = st.sidebar.number_input("Erro Máximo (Epsilon)", value=0.0001, format="%.5f")
max_iter = st.sidebar.number_input("Máximo Iterações", value=20, step=1)

if st.sidebar.button("Calcular"):
    # Execução do Algoritmo
    raiz, historico, tabela, convergiu, msg = executar_metodo(f_str, df_str, x0, epsilon, int(max_iter))

    # Exibição de Status
    col1, col2 = st.columns(2)
    with col1:
        if convergiu:
            st.success(f"Status: {msg}")
        else:
            st.error(f"Status: {msg}")
    with col2:
        st.metric(label="Raiz Aproximada", value=f"{raiz:.8f}")

    # --- Gráfico ---
    st.subheader("Visualização Gráfica")
    
    plt.style.use('default') 
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Configuração de visualização (-8 a 8)
    x_vals = np.linspace(-8, 8, 400)
    
    try:
        y_vals = avaliar_funcao(f_str, x_vals)
    except:
        y_vals = [avaliar_funcao(f_str, x) for x in x_vals]
        
    ax.plot(x_vals, y_vals, label=f'f(x) = {f_str}', color='#006442', linewidth=2.5)
    
    # Configuração Isométrica (Quadrada) e Eixos
    ax.set_aspect('equal')
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    y_hist = [avaliar_funcao(f_str, x) for x in historico]
    ax.plot(historico, y_hist, color='blue', linestyle='--', linewidth=1, alpha=0.6)
    ax.scatter(historico, y_hist, color='blue', s=30, label='Iterações')
    ax.scatter(raiz, avaliar_funcao(f_str, raiz), color='red', s=80, zorder=5, label='Raiz')

    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.3)
    
    ax.legend(loc='upper left')
    st.pyplot(fig)

    # Tabela
    st.subheader("Tabela de Iterações")
    st.dataframe(tabela, use_container_width=True)