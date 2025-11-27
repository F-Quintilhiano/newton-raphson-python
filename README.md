

```markdown
🧮 Método de Newton-Raphson

Implementação em Python do **Método de Newton-Raphson** para encontrar raízes de funções não lineares.

Este projeto foi desenvolvido para a disciplina de **Métodos Numéricos e Computacionais**, com foco em modularização, visualização gráfica e interface web.

🚀 Funcionalidades

- **Interface Web (Streamlit):** Painel interativo moderno que roda no navegador.
- **Cálculo Automático de Derivadas:** Usa a biblioteca **SymPy** para calcular $f'(x)$ automaticamente.
- **Gráficos Precisos:** Visualização estilo "GeoGebra" (escala 1:1, eixos centrados).
- **Tabela Detalhada:** Histórico passo a passo das iterações e erro estimado.
- **Modo Terminal:** Versão robusta para execução via linha de comando (`main.py`).

🛠️ Tecnologias

- **Python 3**
- **Streamlit** (Interface Gráfica)
- **SymPy** (Cálculo Simbólico)
- **Matplotlib** (Gráficos)
- **NumPy** (Cálculos Numéricos)

📦 Instalação

Certifique-se de ter o Python 3 instalado.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPO.git
   cd NOME-DO-REPO
   ```

2. **Instale as dependências:**
   ```bash
   pip3 install streamlit numpy matplotlib sympy
   ```

## 🖥️ Como Executar

### 1. Interface Web (Recomendado)
Para abrir o painel visual no seu navegador:
```bash
streamlit run app.py
```

### 2. Modo Terminal
Para rodar apenas o cálculo e salvar o gráfico como imagem (`resultado_grafico.png`):
```bash
python3 main.py
```

## 📂 Estrutura do Projeto

- `app.py`: Interface gráfica web (Streamlit).
- `newton_algoritmo.py`: Núcleo matemático (Lógica do método).
- `main.py`: Interface de terminal (CLI).

## 📊 Exemplo de Teste

Para validar o funcionamento, utilize os seguintes parâmetros:

- **Função:** `x^3 - 2*x - 5`
- **Derivada (Automática):** `3*x^2 - 2`
- **Chute Inicial ($x_0$):** `2.0`
- **Resultado Esperado:** Raiz em `2.09455148` (aprox. 3 iterações).

---

```
