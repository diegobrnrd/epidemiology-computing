# Declaração de Uso de Ferramentas de Inteligência Artificial

Durante o desenvolvimento da entrega final desta disciplina (código e artigo), a Inteligência Artificial (Gemini) foi utilizada estritamente como uma ferramenta de apoio para sintaxe de programação, documentação de bibliotecas e formatação matemática. A autoria intelectual da análise e da estrutura do modelo é humana.

Abaixo estão os resumos dos prompts utilizados para consultas pontuais:

**Interação 1: Dúvida sobre a biblioteca SciPy**
*   **Prompt do Usuário:** "Estou escrevendo um código em Python para simular o modelo epidemiológico SEIR. Como eu configuro corretamente a função `odeint` da biblioteca `scipy.integrate` para resolver um sistema com 4 equações diferenciais simultâneas (S, E, I, R)? Me dê apenas um exemplo da sintaxe de como empacotar os valores iniciais e passar os argumentos extras (args)."
*   **Uso:** A resposta ajudou a corrigir um erro de dimensão nas variáveis (shape) na hora de passar as taxas (beta, sigma, gamma) para o integrador numérico.

**Interação 2: Melhoria visual do gráfico (Matplotlib)**
*   **Prompt do Usuário:** "Já resolvi as equações e tenho as matrizes S, E, I e R ao longo de 200 dias. Escreva um trecho de código usando `matplotlib.pyplot` que plote essas 4 linhas com um visual adequado para um artigo acadêmico. Gostaria de linhas com cores padrão, a curva de expostos tracejada, uma legenda limpa e uma grade (grid) suave ao fundo."
*   **Uso:** O trecho sugerido pela IA foi adaptado com as cores desejadas e incorporado na rotina final de plotagem para melhorar a qualidade da imagem do artigo.

**Interação 3: Formatação das Equações (LaTeX)**
*   **Prompt do Usuário:** "Pode gerar o código em formatação LaTeX para as quatro equações diferenciais ordinárias do modelo SEIR (dS/dt, dE/dt, dI/dt e dR/dt) considerando a divisão pela população N na taxa de infecção? Preciso colar isso na metodologia do meu texto."
*   **Uso:** As equações geradas pela IA foram copiadas para garantir a formatação científica correta dos símbolos no editor de texto.
