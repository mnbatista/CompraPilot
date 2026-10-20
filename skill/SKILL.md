---
name: auditoria-compras
description: Interpreta etiquetas de supermercado, aplica preços normais ou promocionais, calcula itens e carrinhos e confere os valores esperados com os valores cobrados.
compatibility: Requer Python 3. Não requer rede nem pacotes externos.
metadata:
  author: Maycon Batista
  version: "1.1"
---

# Auditoria de compras

Use esta habilidade para interpretar etiquetas, aplicar promoções, calcular compras e conferir comprovantes.

O script está localizado em:

`scripts/calcular_compra.py`

## Responsabilidades

Esta habilidade deve:

- interpretar etiquetas de preços;
- validar a quantidade comprada;
- diferenciar embalagens de unidades internas;
- aplicar preços normais ou promocionais;
- calcular subtotais e o total do carrinho;
- recalcular itens corrigidos ou removidos;
- comparar o total esperado com o valor cobrado;
- auxiliar na conferência do comprovante;
- identificar possíveis divergências.

O agente controla o fluxo da conversa e o formato das respostas. Esta habilidade concentra as regras de interpretação, cálculo e conferência.

## Interpretação da etiqueta

Extraia somente informações legíveis:

- nome e descrição do produto;
- marca;
- peso, volume ou conteúdo da embalagem;
- código EAN ou código de barras;
- preço normal ou de varejo;
- preço promocional ou de atacado;
- quantidade mínima da promoção;
- condições adicionais;
- validade da oferta, quando visível;
- unidade de comercialização.

Não invente informações ausentes ou ilegíveis.

Se produto ou preço não estiver claro, solicite somente a informação necessária ou uma nova fotografia.

## Quantidade obrigatória

A quantidade comprada é obrigatória.

A quantidade pode ser informada:

- junto com a fotografia;
- na mensagem imediatamente anterior;
- na mensagem imediatamente posterior.

Nunca presuma quantidade igual a 1.

Não registre nem calcule o item enquanto a quantidade estiver ausente.

Considere a quantidade informada como número de embalagens, salvo indicação explícita em contrário.

## Interpretação das quantidades

Diferencie:

- quantidade de embalagens compradas;
- quantidade contida em cada embalagem;
- quantidade mínima exigida pela promoção.

Exemplo:

`Carga com 4 unidades, R$ 54,99 a partir de 3 unidades.`

Interpretação:

- conteúdo da embalagem: 4 unidades;
- quantidade mínima: 3 embalagens;
- preço promocional: R$ 54,99 por embalagem.

Não interprete as unidades contidas na embalagem como quantidade comprada.

## Aplicação de promoções

Aplique o preço promocional somente quando:

- existir preço promocional legível;
- a quantidade mínima estiver identificada;
- a quantidade comprada atingir o mínimo;
- as demais condições estiverem confirmadas.

Caso contrário, aplique o preço normal.

A expressão “a partir de 3 unidades” aplica-se a qualquer quantidade igual ou superior a 3. Não exija múltiplos de 3.

Não presuma o cumprimento de condições envolvendo:

- clube;
- CPF;
- aplicativo;
- cartão;
- cupom;
- forma de pagamento;
- combinação de produtos.

Quando uma condição alterar o preço, solicite confirmação ao usuário.

## Promoções especiais

Considere como promoção especial ofertas relacionadas a:

- proximidade do vencimento;
- liquidação;
- etiqueta especial;
- desconto excepcional;
- condição temporária de validade.

Registre internamente:

`Promoção especial: preservar evidência para conferência.`

Não recomende comprar mais apenas porque o preço unitário é menor.

## Validação antes do cálculo

Antes de calcular, confirme:

- identificação do produto;
- quantidade comprada;
- pelo menos um preço aplicável.

Se houver ambiguidade relevante, não calcule nem registre o item até obter a informação necessária.

## Script de cálculo

Use `scripts/calcular_compra.py` para todos os cálculos monetários.

O script possui três operações:

- `item`: calcula o preço aplicado e o subtotal;
- `carrinho`: recalcula os itens e o total da compra;
- `conferir`: compara o total esperado com o cobrado.

Use a saída JSON do script como fonte dos resultados.

Não substitua um cálculo executado com sucesso por um cálculo estimado em linguagem natural.

## Operação item

Use a operação `item` para registrar ou corrigir um produto.

Forneça dados equivalentes a:

```json
{
  "produto": "Carga Gillette Mach3 Carbono 4UN",
  "quantidade": 3,
  "preco_normal": 57.99,
  "preco_promocional": 54.99,
  "quantidade_minima_promocao": 3,
  "condicoes_atendidas": true
}
```

Não inclua campos cuja informação não seja conhecida.

O cálculo é:

`subtotal = quantidade × preço unitário aplicável`

A saída deve conter:

- produto;
- quantidade;
- preço aplicado;
- subtotal;
- regra aplicada.

## Operação carrinho

Use a operação `carrinho` após:

- inclusão de item;
- correção de item;
- remoção de item;
- solicitação do carrinho;
- finalização da compra.

Forneça todos os itens ativos:

```json
{
  "itens": [
    {
      "produto": "Arroz 5 kg",
      "quantidade": 2,
      "preco_normal": 29.90
    }
  ]
}
```

A saída deve conter:

- itens calculados;
- quantidade de produtos diferentes;
- total de unidades ou embalagens;
- total estimado;
- moeda.

Não inclua itens removidos.

## Numeração dos itens

Atribua um número sequencial permanente a cada produto registrado.

Mantenha o mesmo número durante toda a compra.

Se um item for removido, não reutilize seu número.

A numeração deve permitir comandos como:

- Mostrar item 3;
- Corrigir item 2;
- Remover item 4.

## Correções e remoções

Ao corrigir um item:

1. altere somente os dados solicitados;
2. execute novamente a operação `item`;
3. recalcule o carrinho;
4. preserve a numeração do item.

Ao remover um item:

1. exclua o item dos cálculos ativos;
2. não reutilize seu número;
3. recalcule o carrinho.

## Operação conferir

Use a operação `conferir` quando o usuário informar o total cobrado.

Forneça:

```json
{
  "total_esperado": 94.70,
  "total_cobrado": 99.70
}
```

Calcule:

`diferença = total cobrado - total esperado`

Classifique como:

- valores iguais;
- cobrado a mais;
- cobrado a menos.

Não atribua a diferença a um produto específico sem informações individuais do comprovante.

## Conferência do comprovante

Extraia do comprovante:

- descrição do produto;
- quantidade;
- preço unitário bruto;
- subtotal bruto;
- descontos;
- acréscimos;
- valor líquido;
- total cobrado.

Relacione as linhas aos produtos registrados usando, quando disponíveis:

1. código de barras;
2. descrição e marca;
3. peso, volume ou conteúdo;
4. quantidade;
5. preço e subtotal.

Considere abreviações comuns no comprovante.

Não associe produtos apenas por semelhança vaga.

## Descontos separados

Um preço bruto maior não representa automaticamente uma divergência.

Quando houver desconto separado:

1. associe o desconto ao produto correto;
2. calcule o valor líquido;
3. compare o valor líquido com o esperado.

Use:

`valor líquido = valor bruto - descontos + acréscimos`

Depois:

`diferença = valor líquido - valor esperado`

Exemplo:

```text
Esperado: 2 × R$ 3,92 = R$ 7,84
Cobrado bruto: R$ 23,18
Desconto: R$ 15,34
Cobrado líquido: R$ 7,84
Diferença: R$ 0,00
Situação: Conferido
```

## Classificação da conferência

Classifique cada item como:

- `Conferido`: valor líquido igual ao esperado;
- `Possível divergência`: diferença sustentada por dados legíveis;
- `Não localizado`: produto registrado não encontrado;
- `Item adicional`: produto cobrado não registrado;
- `Leitura inconclusiva`: dados insuficientes ou ilegíveis.

Se a fotografia estiver cortada, desfocada ou incompleta, não conclua que houve erro.

Solicite somente uma nova imagem da parte necessária.

## Priorização das divergências

Quando houver divergências, ordene por:

1. maior valor cobrado a mais;
2. promoção especial possivelmente não aplicada;
3. quantidade incorreta;
4. preço unitário incorreto;
5. item adicional.

Identifique a principal divergência usando:

```text
⚠️ Principal divergência

Produto: [produto]
Esperado: R$ [valor]
Cobrado líquido: R$ [valor]
Diferença: R$ [valor]
Item: #[número]
```

## Consulta de etiqueta

Preserve no contexto os dados extraídos de cada etiqueta e sua associação com o número do item.

Quando o usuário consultar um item, disponibilize:

- número;
- produto;
- quantidade;
- preço registrado;
- subtotal;
- condição aplicada;
- código de barras, quando disponível.

A fotografia original só deve ser mencionada como exibida quando a interface realmente disponibilizar o anexo.

Nunca afirme que apresentou a imagem se ela não estiver visível na resposta.

## Insights de economia

Forneça insights somente quando solicitado ou após a conferência.

Diferencie:

- redução do preço unitário;
- economia líquida;
- gasto adicional necessário;
- quantidade adicional;
- necessidade real do produto;
- risco de desperdício;
- validade do produto.

Uma promoção não é necessariamente vantajosa quando exige gasto adicional.

Exemplo:

```text
Comprar mais uma unidade reduz o preço unitário, mas aumenta o gasto total em R$ 6,00. A oferta só é vantajosa se a unidade adicional for necessária e consumida antes do vencimento.
```

## Regras de confiabilidade

- Não invente produto, preço, quantidade, código ou promoção.
- Nunca presuma quantidade igual a 1.
- Não confunda conteúdo da embalagem com quantidade comprada.
- Não aplique promoção sem validar suas condições.
- Não confunda preço bruto com valor líquido.
- Não ignore descontos separados no comprovante.
- Use o script para cálculos monetários.
- Use duas casas decimais para valores monetários.
- Use reais brasileiros no formato `R$ 0,00`.
- Mostre claramente informações incertas.
- Considere os resultados como apoio à conferência.
- Não apresente o resultado como prova definitiva de cobrança indevida.
- Mantenha os dados somente na conversa atual.