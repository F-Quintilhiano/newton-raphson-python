import numpy as np

def avaliar_funcao(expressao, x_val):
    """
    Interpreta a string matemática fornecida pelo usuário e calcula o valor numérico.
    """
    # Mapeamento para permitir que o 'eval' reconheça funções matemáticas padrão
    contexto = {
        "x": x_val,
        "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "exp": np.exp, "sqrt": np.sqrt, "log": np.log, "ln": np.log,
        "pi": np.pi, "e": np.e, "abs": np.abs
    }
    
    # Ajusta sintaxe de potência (padrão usuário '^' para padrão Python '**')
    expressao_corrigida = expressao.replace('^', '**')
    
    try:
        return eval(expressao_corrigida, {"__builtins__": None}, contexto)
    except Exception:
        return None

def executar_metodo(f_str, df_str, x0, epsilon, max_iter):
    """
    Executa o algoritmo de Newton-Raphson.
    Retorna: (raiz, histórico, tabela_dados, status_convergencia, mensagem)
    """
    x_atual = x0
    historico = [x0] 
    dados_tabela = [] 

    for k in range(1, max_iter + 1):
        fx = avaliar_funcao(f_str, x_atual)
        dfx = avaliar_funcao(df_str, x_atual)

        # Validação de sintaxe antes de prosseguir
        if fx is None or dfx is None:
            return x_atual, historico, dados_tabela, False, "Erro de Sintaxe na Função"

        # Proteção contra divisão por zero (ponto crítico ou derivada nula)
        if abs(dfx) < 1e-14:
            return x_atual, historico, dados_tabela, False, "Derivada nula (divisão por zero)"

        # Iteração do método: x(n+1) = x(n) - f(x)/f'(x)
        x_novo = x_atual - (fx / dfx)
        erro = abs(x_novo - x_atual)

        # Registro dos dados para exibição na interface
        dados_tabela.append({
            "iter": k, 
            "xn": x_atual, 
            "fx": fx, 
            "erro": erro
        })

        x_atual = x_novo
        historico.append(x_atual)

        # Verificação do critério de parada
        if erro < epsilon:
            return x_atual, historico, dados_tabela, True, "Convergência alcançada"

    return x_atual, historico, dados_tabela, False, "Limite de iterações atingido"