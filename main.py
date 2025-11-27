import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# Importa a lógica de cálculo
from newton_algoritmo import executar_metodo, avaliar_funcao

def gerar_grafico_estatico(f_str, historico, raiz):
    """
    Gera o gráfico e salva em disco em vez de mostrar na tela.
    Isso garante compatibilidade com servidores e sistemas sem interface gráfica.
    """
    plt.style.use('default')
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Configuração de visualização 
    x_vals = np.linspace(-8, 8, 400)
    try:
        y_vals = avaliar_funcao(f_str, x_vals)
    except:
        y_vals = [avaliar_funcao(f_str, x) for x in x_vals]
        
    # Plotagem
    ax.plot(x_vals, y_vals, label=f'f(x) = {f_str}', color='#006442', linewidth=2.5)
    
    # Configuração dos eixos e escala
    ax.set_aspect('equal')
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    
    # Centralizar eixos
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # Plotar iterações
    y_hist = [avaliar_funcao(f_str, x) for x in historico]
    ax.plot(historico, y_hist, 'b--', alpha=0.6)
    ax.scatter(historico, y_hist, color='blue', s=30, label='Iterações')
    ax.scatter(raiz, avaliar_funcao(f_str, raiz), color='red', s=80, zorder=5, label='Raiz')
    
    # Grid de 1 em 1
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.grid(True, which='both', linestyle='-', linewidth=0.5, alpha=0.3)
    ax.legend()

    # Salvar arquivo
    nome_arquivo = "resultado_grafico.png"
    plt.savefig(nome_arquivo)
    print(f"\n[INFO] Gráfico gerado e salvo como '{nome_arquivo}'.")

def main():
    print("=== MÉTODO DE NEWTON-RAPHSON (Modo Terminal) ===")
    
    # Entrada de dados
    f_str = input("Função f(x) [ex: x^3 - 2*x - 5]: ").strip()
    df_str = input("Derivada f'(x) [ex: 3*x^2 - 2]: ").strip()
    
    try:
        x0 = float(input("Chute inicial x0: "))
        epsilon = float(input("Erro tolerado (epsilon): "))
        max_iter = int(input("Máximo de iterações: "))
    except ValueError:
        print("Erro: Entrada numérica inválida.")
        return

    # Execução do algoritmo
    raiz, historico, tabela, convergiu, msg = executar_metodo(f_str, df_str, x0, epsilon, max_iter)

    # Exibição da Tabela Formatada
    print("\n" + "="*65)
    print(f"{'Iter':<5} | {'xn':<15} | {'f(xn)':<15} | {'Erro':<15}")
    print("-" * 65)
    
    for linha in tabela:
        print(f"{linha['iter']:<5} | {linha['xn']:<15.8f} | {linha['fx']:<15.8f} | {linha['erro']:<15.8f}")
    
    print("-" * 65)
    print(f"\n>>> STATUS: {msg}")
    print(f"Raiz Final: {raiz:.10f}")

    # Geração do Gráfico 
    opt = input("\nGerar arquivo de gráfico? (s/n): ").lower()
    if opt == 's':
        gerar_grafico_estatico(f_str, historico, raiz)

if __name__ == "__main__":
    main()