import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. FUNÇÃO AUXILIAR PARA INTERPRETAR TEXTO COMO MATEMÁTICA
# =============================================================================
def avaliar_funcao(expressao, x_val):
    """
    Pega uma string (ex: 'x^2 - 5') e um valor de x, e calcula o resultado.
    """
    # Dicionário de funções permitidas (para o usuário não precisar digitar np.sin)
    contexto_matematico = {
        "x": x_val,
        "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "exp": np.exp, "sqrt": np.sqrt, "log": np.log, "ln": np.log,
        "pi": np.pi, "e": np.e,
        "abs": np.abs
    }
    
    # Python usa ** para potência, mas usuário pode digitar ^. Vamos corrigir:
    expressao_corrigida = expressao.replace('^', '**')
    
    try:
        # eval calcula a string usando o contexto matemático definido acima
        return eval(expressao_corrigida, {"__builtins__": None}, contexto_matematico)
    except Exception as e:
        print(f"Erro ao calcular a função: {e}")
        return None

# =============================================================================
# 2. IMPLEMENTAÇÃO DO MÉTODO DE NEWTON
# =============================================================================
def metodo_newton(f_str, df_str, x0, epsilon, max_iter):
    x_atual = x0
    historico = [x0]
    
    print("\n" + "="*65)
    print(f"{'Iter':<5} | {'xn':<15} | {'f(xn)':<15} | {'Erro Estimado':<15}")
    print("-" * 65)

    for k in range(1, max_iter + 1):
        # Calcula f(x) e f'(x) usando as strings digitadas
        fx = avaliar_funcao(f_str, x_atual)
        dfx = avaliar_funcao(df_str, x_atual)

        if fx is None or dfx is None:
            return x_atual, historico, False # Erro de sintaxe

        # Critério de Segurança: Derivada zero
        if abs(dfx) < 1e-14:
            print(f"\n[ERRO] Derivada muito próxima de zero em x={x_atual:.6f}.")
            print("O método falhou (divisão por zero).")
            return x_atual, historico, False

        # Fórmula de Newton
        x_novo = x_atual - (fx / dfx)
        erro = abs(x_novo - x_atual)

        print(f"{k:<5} | {x_atual:<15.8f} | {fx:<15.8f} | {erro:<15.8f}")

        x_atual = x_novo
        historico.append(x_atual)

        if erro < epsilon:
            print("-" * 65)
            return x_atual, historico, True
            
    print("-" * 65)
    return x_atual, historico, False

# =============================================================================
# 3. GRÁFICO
# =============================================================================
def gerar_grafico(f_str, historico, raiz):
    margem = 2
    # Cria vetor de X ao redor da raiz
    x_vals = np.linspace(min(historico) - margem, max(historico) + margem, 200)
    
    # Calcula Y para todo o vetor (usando nossa função avaliadora)
    try:
        y_vals = avaliar_funcao(f_str, x_vals)
    except:
        # Fallback caso a string não suporte vetorização direta
        y_vals = [avaliar_funcao(f_str, x) for x in x_vals]

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f'f(x) = {f_str}', color='blue')
    plt.axhline(0, color='black', linewidth=1)
    
    # Plota os pontos da iteração
    y_hist = [avaliar_funcao(f_str, x) for x in historico]
    plt.plot(historico, y_hist, 'ro--', label='Iterações', alpha=0.6)
    
    # Marca a raiz
    plt.plot(raiz, avaliar_funcao(f_str, raiz), 'go', markersize=8, label=f'Raiz: {raiz:.4f}')
    
    plt.title(f"Método de Newton-Raphson\nFunc: {f_str}")
    plt.grid(True)
    plt.legend()
    plt.show()

# =============================================================================
# 4. PROGRAMA PRINCIPAL
# =============================================================================
def main():
    print("=== MÉTODO DE NEWTON-RAPHSON (ENTRADA MANUAL) ===")
    print("Instruções de digitação:")
    print(" - Use 'x' como variável.")
    print(" - Operações: +, -, *, /")
    print(" - Potência: x^3 ou x**3")
    print(" - Funções: sin(x), cos(x), exp(x) [para e^x], log(x) [ln]")
    print(" - Exemplo: x^3 - 2*x - 5")
    print("--------------------------------------------------")

    # Solicitar Strings do Usuário
    f_str = input("Digite a função f(x): ").strip()
    df_str = input("Digite a derivada f'(x): ").strip()
    
    try:
        x0 = float(input("Chute inicial x0: "))
        epsilon = float(input("Erro máximo (epsilon): "))
        max_iter = int(input("Máximo de iterações: "))
    except ValueError:
        print("Erro: Digite apenas números para x0, epsilon e iterações.")
        return

    # Executar método
    raiz, historico, convergiu = metodo_newton(f_str, df_str, x0, epsilon, max_iter)

    # Exibir Resultados
    print("\n>>> RESULTADO FINAL <<<")
    print(f"Raiz aproximada: {raiz:.10f}")
    print(f"Iterações: {len(historico)-1}")
    print(f"Status: {'CONVERGIU' if convergiu else 'NÃO CONVERGIU'}")

    ver_grafico = input("\nGerar gráfico? (s/n): ").lower()
    if ver_grafico == 's':
        gerar_grafico(f_str, historico, raiz)

if __name__ == "__main__":
    main()