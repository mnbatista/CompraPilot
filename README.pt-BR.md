# 🛒 CompraPilot

[English](README.md) | [Português do Brasil](README.pt-BR.md)

![Banner do CompraPilot](assets/banner-github.png)

## Você já se perguntou se o preço cobrado no caixa é o mesmo que estava na prateleira?

O **CompraPilot** é um copiloto de compras com IA, criado com o Microsoft 365 Copilot Agent Builder.

Ele ajuda consumidores a acompanhar compras em tempo real, validar promoções, calcular o total esperado, comparar preços de prateleira com os valores do comprovante e identificar possíveis divergências.

> **Verificação de preços e comprovantes com IA.**

Diferente de uma simples lista de compras ou calculadora, o CompraPilot preserva o contexto de cada preço, incluindo quantidades, condições promocionais e informações extraídas das etiquetas.

**Validado em cenários reais de compras e reconciliação de comprovantes.**

---

## 🎯 O Problema

Promoções nem sempre são fáceis de entender.

Uma etiqueta pode apresentar:

- preço normal de varejo;
- preço menor para a compra de várias unidades;
- exigência de cadastro em clube de vantagens;
- desconto exclusivo pelo aplicativo;
- condição relacionada à forma de pagamento;
- desconto para produto próximo ao vencimento;
- promoções como “compre 2 e leve 3”.

Mesmo quando a oferta é entendida corretamente, o valor cobrado no caixa pode ser diferente do preço exibido na prateleira.

Conferir tudo manualmente enquanto existe uma fila no caixa pode ser lento e desconfortável, especialmente quando o consumidor precisa localizar rapidamente a etiqueta correspondente ao produto.

O CompraPilot foi criado para tornar esse processo mais estruturado, transparente e prático.

---

## 💡 A Solução

Durante a compra, o consumidor fotografa a etiqueta e informa a quantidade colocada no carrinho.

O CompraPilot:

1. lê as informações do produto e do preço;
2. interpreta as condições da promoção;
3. aplica o preço unitário correspondente;
4. calcula o subtotal do item;
5. mantém o total esperado da compra;
6. preserva as informações para conferência posterior.

No caixa, o consumidor pode comparar o total esperado com o valor apresentado pelo operador.

Depois do pagamento, o consumidor pode enviar uma imagem do comprovante para que o CompraPilot compare os preços registrados com os valores efetivamente cobrados.

O CompraPilot também diferencia:

- possíveis divergências de preço;
- descontos lançados separadamente no comprovante;
- diferenças legítimas causadas por produtos vendidos por peso;
- itens adicionais que não estavam no total estimado.

---

## ✨ Principais Recursos

- ✅ Leitura de etiquetas por fotografia
- ✅ Confirmação obrigatória da quantidade
- ✅ Interpretação de preços normais e promocionais
- ✅ Validação de promoções por quantidade mínima
- ✅ Cálculo de subtotal e total em tempo real
- ✅ Respostas compactas durante a compra
- ✅ Acompanhamento da lista de compras
- ✅ Identificação de itens faltantes
- ✅ Correção e remoção de produtos
- ✅ Modo Caixa compacto
- ✅ Comparação com o total apresentado no caixa
- ✅ Análise de comprovantes
- ✅ Interpretação de descontos separados
- ✅ Reconciliação de produtos vendidos por peso
- ✅ Identificação de possíveis divergências
- ✅ Explicação de diferenças legítimas

---

## 📸 Como Funciona

### 1. Registrar uma lista de compras

O consumidor pode começar enviando uma lista:

```text
Arroz
Café
Leite
Papel higiênico
```

O CompraPilot acompanha os produtos planejados e identifica quais itens ainda não foram comprados.

Essa etapa é opcional. A compra também pode começar sem uma lista previamente cadastrada.

---

### 2. Iniciar uma compra

```text
Iniciar compra
```

O CompraPilot cria um novo carrinho e descarta os cálculos da compra anterior.

---

### 3. Registrar etiquetas

O consumidor envia uma fotografia da etiqueta e informa a quantidade:

```text
Quantidade: 3
```

O CompraPilot tenta extrair:

- nome do produto;
- marca;
- peso, volume ou conteúdo da embalagem;
- código de barras, quando visível;
- preço normal;
- preço promocional;
- quantidade mínima da promoção;
- condições adicionais;
- validade da oferta, quando visível.

Se a quantidade não for informada, o CompraPilot pergunta em vez de presumir uma unidade.

---

### 4. Acompanhar os gastos com respostas compactas

Para reduzir a rolagem da conversa, o excesso de informações e o consumo de dados móveis, o CompraPilot apresenta uma resposta compacta depois de cada item:

```text
✅ Item registrado

Coco Ralado Sweet Coco
Qtd: 2
Subtotal: R$ 7,84

Total: R$ 7,84
```

O carrinho completo aparece somente quando solicitado ou quando a compra é finalizada.

---

### 5. Corrigir ou remover produtos

O consumidor pode atualizar o carrinho usando comandos em linguagem natural:

```text
Corrija a quantidade do arroz para 3.
```

```text
Remova o café.
```

```text
O preço correto é R$ 18,90.
```

O CompraPilot recalcula o item afetado e o total esperado.

---

### 6. Finalizar a compra

```text
Finalizar compra
```

O CompraPilot apresenta um relatório compacto contendo:

- número do item;
- produto;
- quantidade;
- preço unitário aplicado;
- condição promocional;
- subtotal;
- total esperado;
- itens ainda não comprados.

---

### 7. Usar o Modo Caixa

Quando o consumidor informa:

```text
Modo caixa
```

o CompraPilot apresenta uma tabela compacta ordenada pelo impacto financeiro:

| # | Produto | Qtd. | Preço unitário | Subtotal |
|---:|---|---:|---:|---:|
| 1 | Produto A | 4 | R$ 12,50 | R$ 50,00 |
| 2 | Produto B | 2 | R$ 8,00 | R$ 16,00 |

Essa visualização foi criada para consultas rápidas enquanto o consumidor está no caixa.

Também é possível solicitar um produto específico:

```text
Mostrar item 2
```

O CompraPilot apresenta somente as informações associadas ao item.

> A possibilidade de reapresentar a fotografia original da etiqueta depende da interface do chat. O CompraPilot nunca deve afirmar que mostrou uma imagem quando ela não estiver visível na resposta.

---

### 8. Comparar o total do caixa

O consumidor pode informar o total apresentado pelo operador:

```text
O total do caixa é R$ 165,73.
```

O CompraPilot compara:

```text
Total esperado: R$ 154,73
Total do caixa: R$ 165,73
Diferença: R$ 11,00
```

Uma diferença indica que pode ser necessário realizar uma conferência mais detalhada.

Entretanto, o CompraPilot não atribui a diferença a um produto específico sem os dados individuais do caixa ou do comprovante.

---

### 9. Analisar o comprovante

Depois do pagamento, o consumidor pode enviar uma fotografia do comprovante.

O CompraPilot tenta:

- extrair os produtos;
- identificar quantidades;
- interpretar preços unitários;
- identificar descontos separados;
- comparar valores líquidos com os valores esperados;
- detectar itens ausentes ou adicionais;
- reconciliar produtos vendidos por peso;
- destacar possíveis divergências.

Um valor bruto maior não representa automaticamente um erro.

Alguns sistemas de caixa registram primeiro o preço normal e lançam o desconto promocional em uma linha separada. Quando o desconto estiver disponível, o CompraPilot compara o valor esperado com o **valor líquido cobrado**.

---

## 🧾 Exemplo de Conferência de Comprovante

Suponha que o valor esperado seja:

```text
2 × R$ 3,92 = R$ 7,84
```

O comprovante apresenta:

```text
Valor bruto: R$ 23,18
Desconto: R$ 15,34
Valor líquido: R$ 7,84
```

O CompraPilot deve classificar o item como:

```text
Diferença: R$ 0,00
Situação: Conferido
```

Isso evita que um desconto promocional lançado separadamente seja classificado incorretamente como divergência.

> Os casos reais preservam os valores e a moeda utilizados originalmente nos testes.

---

## ✅ Validado em Cenários Reais de Compra

O CompraPilot não foi desenvolvido somente com exemplos simulados.

O agente já foi utilizado em compras reais envolvendo supermercados, atacarejos, promoções, produtos vendidos por peso, reconciliação de comprovantes e conferência no caixa.

### Ambientes Testados

- ✅ Supermercados
- ✅ Atacarejos

### Cenários Validados

- ✅ Registro de etiquetas
- ✅ Confirmação obrigatória da quantidade
- ✅ Promoções por quantidade mínima
- ✅ Descontos para produtos próximos ao vencimento
- ✅ Seleção entre preço normal e promocional
- ✅ Interpretação do conteúdo da embalagem
- ✅ Compra de várias unidades
- ✅ Correção e remoção de itens
- ✅ Acompanhamento da lista de compras
- ✅ Identificação de itens faltantes
- ✅ Cálculo do total em tempo real
- ✅ Modo Compra Compacto
- ✅ Modo Caixa
- ✅ Comparação com o total do caixa
- ✅ Conferência de comprovantes
- ✅ Descontos lançados separadamente
- ✅ Carnes e outros produtos previamente pesados
- ✅ Produtos pesados somente no caixa
- ✅ Reconciliação de diferenças legítimas

### Exemplo Real: Reconciliação de Produtos Vendidos por Peso

Durante uma compra real, o total do comprovante ficou **R$ 37,40 acima** do total estimado pelo CompraPilot.

Em vez de classificar imediatamente a diferença como erro de preço, o CompraPilot identificou que todo o valor correspondia a produtos cujo preço final dependia do peso medido no caixa:

| Produto | Peso no caixa | Valor cobrado |
|---|---:|---:|
| Limões | 1,430 kg | R$ 18,45 |
| Bananas | 1,020 kg | R$ 4,07 |
| Mamão | 2,030 kg | R$ 12,16 |
| Abacates | 0,910 kg | R$ 2,72 |
| **Total** |  | **R$ 37,40** |

A reconciliação foi:

```text
Total estimado: R$ 1.415,57
Total do comprovante: R$ 1.452,97
Diferença inicial: R$ 37,40

Total dos produtos pesados no caixa: R$ 37,40
Diferença não explicada: R$ 0,00
```

**Resultado**

- ✅ Comprovante reconciliado com sucesso
- ✅ Nenhuma divergência de preço encontrada
- ✅ Produtos registrados compatíveis com as etiquetas
- ✅ Produtos vendidos por peso identificados corretamente
- ✅ Total final validado com sucesso

### Melhorias Desenvolvidas a Partir do Uso Real

Compras reais influenciaram diretamente a evolução do CompraPilot.

Durante um dos primeiros testes, localizar as informações de uma etiqueta dentro de uma conversa longa foi difícil enquanto o operador do caixa aguardava.

Essa observação levou à criação de:

- ✅ **Modo Compra Compacto**, reduzindo o texto gerado depois de cada item;
- ✅ **Modo Caixa**, apresentando uma tabela curta para conferência;
- ✅ **Itens numerados**, permitindo comandos como `Mostrar item 3`;
- ✅ **Consulta rápida de produtos**, reduzindo a necessidade de pesquisar todo o histórico.

O CompraPilot está sendo aprimorado por meio de experiências reais, resultados mensuráveis e aprendizados documentados em campo.

---

## 📚 Exemplos Reais

Os exemplos detalhados estão disponíveis na pasta [`examples/`](examples/):

- [Compra básica](examples/basic-shopping.md)
- [Promoção por quantidade](examples/quantity-promotion.md)
- [Conferência no caixa](examples/checkout-verification.md)
- [Reconciliação de comprovante](examples/receipt-reconciliation.md)
- [Acompanhamento da lista de compras](examples/shopping-list-tracking.md)
- [Produtos vendidos por peso](examples/weighted-products.md)
- [Jornada de validação em cenários reais](examples/real-world-validation.md)

Os exemplos documentam comportamentos esperados, regras de cálculo, resultados de testes e melhorias do produto.

---

## 🧠 Princípios de Projeto

### Precisão Antes da Automação

O CompraPilot não deve inventar preços, quantidades, códigos de barras ou condições promocionais que estejam ilegíveis.

### A Quantidade É Obrigatória

O CompraPilot não deve presumir silenciosamente que o consumidor comprou uma unidade.

### Conteúdo da Embalagem Não É Quantidade Comprada

Uma embalagem contendo quatro unidades é diferente de quatro embalagens colocadas no carrinho.

### Uma Diferença Nem Sempre É um Erro

Produtos vendidos por peso, descontos separados e cobranças adicionais legítimas devem ser reconciliados antes de uma divergência ser indicada.

### O Valor Líquido É o Que Importa

Descontos lançados no comprovante devem ser considerados antes da comparação entre o valor esperado e o valor cobrado.

### Experiência Compacta no Celular

As respostas devem ser curtas porque o consumidor pode estar caminhando pelo estabelecimento, utilizando um celular e dependendo de dados móveis.

### A Verificação Humana Continua Importante

O CompraPilot oferece apoio à decisão. O resultado não deve ser tratado como prova definitiva de cobrança incorreta.

---

## 🚀 Status dos Recursos

| Recurso | Status |
|---|---|
| Registro de etiqueta por fotografia | ✅ Disponível |
| Confirmação obrigatória da quantidade | ✅ Disponível |
| Promoções simples | ✅ Disponível |
| Promoções por quantidade mínima | ✅ Disponível |
| Cálculo do carrinho | ✅ Disponível |
| Modo Compra Compacto | ✅ Disponível |
| Modo Caixa | ✅ Disponível |
| Acompanhamento da lista | ✅ Disponível |
| Identificação de itens faltantes | ✅ Disponível |
| Comparação com o total do caixa | ✅ Disponível |
| Análise de comprovantes | ✅ Disponível |
| Descontos separados no comprovante | ✅ Disponível |
| Conferência de produtos previamente pesados | ✅ Disponível |
| Reconciliação de produtos pesados no caixa | ✅ Disponível |
| Explicação de diferenças legítimas | ✅ Disponível |
| Recuperação da imagem original por item | ⚠️ Depende da interface |
| Compras com mais de 100 itens | 🧪 Em teste de campo |
| Insights de economia | 🚧 Planejado |
| Análise de vantagens promocionais | 🚧 Planejado |
| Histórico de compras | 🔮 Futuro |
| Perfil de consumo | 🔮 Futuro |

---

## 📂 Estrutura do Repositório

```text
CompraPilot/
│
├── README.md
├── README.pt-BR.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
│
├── agent/
│   ├── description.md
│   ├── instructions.md
│   ├── suggested-prompts.md
│   └── agent-builder-configuration.md
│
├── assets/
│   ├── banner-github.png
│   ├── icon.png
│   └── logo.png
│
├── docs/
│   ├── architecture.md
│   ├── installation.md
│   └── roadmap.md
│
├── examples/
│   ├── basic-shopping.md
│   ├── checkout-verification.md
│   ├── quantity-promotion.md
│   ├── real-world-validation.md
│   ├── receipt-reconciliation.md
│   ├── shopping-list-tracking.md
│   └── weighted-products.md
│
└── skill/
    ├── SKILL.md
    └── scripts/
        └── calculate_purchase.py
```

---

## ⚙️ Instalação

### Pré-requisitos

A implementação atual requer:

- acesso ao Microsoft 365 Copilot;
- acesso ao Microsoft 365 Copilot Agent Builder;
- permissão para criar agentes;
- suporte ao envio de imagens;
- acesso a habilidades personalizadas e execução de scripts no ambiente.

A disponibilidade de funcionalidades e habilidades personalizadas pode variar conforme o ambiente Microsoft 365, o licenciamento, as configurações da organização e a participação em programas de versão prévia.

### 1. Criar o Agente

Abra o Microsoft 365 Copilot Agent Builder e crie um agente chamado:

```text
CompraPilot
```

### 2. Configurar a Descrição

Copie o conteúdo de:

```text
agent/description.md
```

Cole no campo de descrição do agente.

### 3. Configurar as Instruções

Copie o conteúdo de:

```text
agent/instructions.md
```

Cole no campo de instruções do Agent Builder.

### 4. Adicionar os Prompts Sugeridos

Utilize os prompts documentados em:

```text
P.

### 6. Importar a Skill

No Agent Builder:

1. abra a configuração do agente;
2. localize a seção de habilidades;
3. adicione uma habilidade personalizada;
4. envie o pacote ZIP;
5. revise o nome, a descrição e os arquivos incluídos;
6. salve ou atualize o agente.

### 7. Executar um Teste Básico

Comece com:

```text
Iniciar compra
```

Envie uma fotografia legível de uma etiqueta e informe a quantidade.

Depois, teste:

```text
Mostrar carrinho
```

```text
Finalizar compra
```

```text
Modo caixa
```

```text
Mostrar item 1
```

Consulte também o guia completo:

docs/installation.md

---

## 🧪 Cenários de Teste Recomendados

Antes de utilizar o CompraPilot em uma compra grande, teste:

1. produto com apenas preço normal;
2. produto com promoção por quantidade mínima;
3. quantidade inferior ao mínimo promocional;
4. produto com desconto por validade próxima;
5. correção de item;
6. remoção de item;
7. vários produtos na mesma conversa;
8. comparação com o total do caixa;
9. comprovante com descontos separados;
10. produto previamente pesado com preço final;
11. produto pesado somente no caixa;
12. imagem incompleta ou ilegível do comprovante.

---

## ⚠️ Limitações Atuais

- Os dados da compra são mantidos na conversa atual.
- Uma nova conversa pode não recuperar o carrinho anterior.
- Compras muito longas podem atingir limites de contexto ou usabilidade.
- Fotografias desfocadas, cortadas, escuras ou com reflexos podem reduzir a qualidade da leitura.
- As descrições no comprovante podem estar abreviadas e dificultar a associação.
- A interface pode não conseguir reapresentar a fotografia original da etiqueta.
- Promoções de clube, aplicativo, cartão, CPF ou forma de pagamento podem exigir confirmação.
- Produtos pesados no caixa não podem receber um valor final antes de o peso ser conhecido.
- O CompraPilot não substitui os processos oficiais de atendimento ou conferência do estabelecimento.
- O projeto ainda está sendo testado em compras com mais de 100 itens.

---

## 🔒 Privacidade

Antes de enviar um comprovante, verifique se ele contém:

- CPF ou outro identificador pessoal;
- informações de pagamento;
- dados de programas de fidelidade;
- identificação de cadastro no estabelecimento;
- outras informações que não devam ser compartilhadas.

O CompraPilot não precisa de acesso a e-mails, mensagens do Teams ou arquivos organizacionais sem relação com a compra.

---

## 💡 Casos de Uso

### Supermercados

- Conferência entre preço da prateleira e preço do caixa
- Validação de promoções
- Controle do orçamento em tempo real
- Reconciliação de comprovantes
- Conferência de produtos vendidos por peso

### Atacarejos

- Preços definidos por quantidade
- Descontos por volume
- Promoções com quantidade mínima
- Controle de carrinhos maiores

### Farmácias e Outros Estabelecimentos

- Validação de descontos
- Comparação de ofertas
- Conferência de comprovantes
- Acompanhamento do total da compra

---

## 🗺️ Roadmap

### Versão 1.0 — Base do MVP

- ✅ Registro de etiquetas
- ✅ Confirmação de quantidade
- ✅ Interpretação de promoções
- ✅ Cálculo do carrinho
- ✅ Relatório final

### Versão 1.1 — Usabilidade em Compras Reais

- ✅ Acompanhamento da lista de compras
- ✅ Identificação de itens faltantes
- ✅ Modo Compra Compacto
- ✅ Modo Caixa
- ✅ Melhorias na conferência de comprovantes

### Versão 1.2 — Conferência Avançada

- 🚧 Validação de compras grandes
- 🚧 Reconciliação aprimorada de comprovantes
- ✅ Reconciliação de produtos vendidos por peso
- 🚧 Priorização de divergências
- 🚧 Métricas de testes em campo

### Versão 1.3 — Inteligência de Compra

- Insights de economia
- Análise de vantagens promocionais
- Identificação de promoções que diminuem o preço unitário, mas aumentam gastos desnecessários
- Consideração de validade e risco de desperdício

### Versão 2.0 — Assistente Pessoal de Compras

- Histórico de compras
- Padrões de consumo
- Histórico de preços
- Recomendações personalizadas

Consulte o roadmap detalhado:

docs/roadmap.md

---

## 🤝 Como Contribuir

Contribuições, ideias, relatos de testes reais e sugestões de melhoria são bem-vindos.

Antes de enviar um pull request, leia:

```text
CONTRIBUTING.md
```

Contribuições úteis incluem:

- novos tipos de promoção;
- formatos diferentes de comprovantes;
- exemplos de produtos vendidos por peso;
- regras internacionais de preços;
- melhorias de localização;
- aprimoramento de prompts;
- testes dos cálculos;
- sugestões de acessibilidade e experiência móvel.

---

## 🌍 Idiomas

O README principal está em inglês para tornar o projeto acessível a uma audiência internacional.

A versão em inglês está disponível aqui:

[Read the README in English](README.md)

Os cenários reais preservam a moeda e os valores utilizados originalmente nos testes.

Contribuições futuras podem adicionar outros idiomas, moedas e modelos regionais de promoção.

---

## 👨‍💻 Autor

Criado por **Maycon de Novaes Batista**.

O CompraPilot começou como um experimento pessoal para responder a uma pergunta simples:

> O preço cobrado no caixa é o mesmo que estava na prateleira?

O projeto evoluiu por meio de compras reais, promoções reais, produtos vendidos por peso e cenários reais de reconciliação de comprovantes.

---

## ⚖️ Aviso Legal

O CompraPilot é um projeto comunitário, independente e de código aberto.

Não é um produto oficial da Microsoft e não possui afiliação ou endosso da Microsoft ou de qualquer estabelecimento comercial.

Microsoft, Microsoft 365 e Copilot são marcas comerciais do grupo de empresas Microsoft.

O CompraPilot oferece estimativas e apoio à decisão. O consumidor deve confirmar preços, promoções, comprovantes e políticas diretamente com o estabelecimento.

---

## ⭐ Apoie o Projeto

Se o CompraPilot ajudou você ou inspirou um cenário real de uso do Copilot:

- ⭐ Deixe uma estrela no repositório
- 🐛 Abra uma issue
- 💡 Sugira um cenário de promoção ou comprovante
- 🧪 Compartilhe resultados de testes reais
- 🚀 Contribua para o projeto

---

**CompraPilot**

*Acompanhe seu carrinho. Confira seu comprovante. Entenda o que você pagou.*