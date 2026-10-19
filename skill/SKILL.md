---
name: auditoria-compras
description: Registra produtos de supermercado a partir de etiquetas, calcula preços normais ou promocionais, mantém o total estimado da compra e confere possíveis divergências com o valor informado pelo caixa ou com o comprovante.
compatibility: Requer Python 3. Não requer rede nem pacotes externos.
metadata:
  author: Maycon Batista
  version: "1.0"
---

# Auditoria de compras

Use esta habilidade para registrar, calcular, finalizar e conferir uma compra de supermercado.

## Arquivos da habilidade

O script de cálculo está localizado em:

`scripts/calcular_compra.py`

Use esse script para:

- calcular o preço aplicável e o subtotal de um item;
- recalcular todos os itens e o total do carrinho;
- comparar o total esperado com o valor cobrado.

## Estados da compra

Considere os seguintes estados:

- não iniciada;
- em andamento;
- finalizada;
- em conferência.

Mantenha os itens da compra na conversa atual até o usuário iniciar outra compra.

## Iniciar compra

Quando o usuário disser "Iniciar compra" ou algo equivalente:

1. Inicie uma compra vazia.
2. Desconsidere itens e totais da compra anterior.
3. Defina o estado como "em andamento".
4. Responda:

> Compra iniciada. Envie a foto da primeira etiqueta e informe a quantidade colocada no carrinho.

Se o usuário enviar uma etiqueta antes de iniciar a compra, pergunte se deseja iniciar uma nova compra.

## Interpretar etiqueta

Ao receber uma fotografia de etiqueta, extraia somente as informações legíveis:

- nome do produto;
- marca;
- peso, volume ou conteúdo da embalagem;
- código de barras;
- preço normal ou de varejo;
- preço promocional ou de atacado;
- quantidade mínima exigida;
- condições adicionais da promoção;
- validade da oferta, quando visível;
- unidade de comercialização.

Não invente dados ausentes ou ilegíveis.

Se algum dado necessário não estiver claro, informe exatamente qual dado precisa ser confirmado.

## Quantidade obrigatória

A quantidade comprada é obrigatória.

O usuário pode informar a quantidade:

- junto com a fotografia;
- na mensagem imediatamente anterior;
- na mensagem imediatamente posterior.

Se a quantidade não tiver sido informada, pergunte apenas:

> Quantas unidades desse produto você colocou no carrinho?

Nunca presuma quantidade igual a 1.

Não registre o item nem acrescente seu valor ao total enquanto a quantidade estiver ausente.

## Interpretação de quantidades

Diferencie sempre:

- quantidade de embalagens compradas;
- quantidade contida em cada embalagem;
- quantidade mínima exigida pela promoção.

Exemplo:

> Carga com 4 unidades, R$ 54,99 a partir de 3 unidades.

Interprete como:

- conteúdo de cada embalagem: 4 unidades;
- quantidade mínima da promoção: 3 embalagens;
- preço promocional por embalagem: R$ 54,99.

Não interprete as 4 unidades contidas na embalagem como quantidade comprada.

## Aplicação de preço

Aplique o preço promocional somente quando:

- existir um preço promocional legível;
- a quantidade mínima estiver identificada;
- a quantidade comprada atingir o mínimo;
- as demais condições exigidas estiverem confirmadas.

Caso contrário, aplique o preço normal.

A expressão "a partir de 3 unidades" significa que o preço promocional se aplica a todas as quantidades iguais ou superiores a 3. Não exija múltiplos de 3.

Para condições envolvendo clube, CPF, aplicativo, cartão, forma de pagamento, cupom ou combinação de produtos, pergunte ao usuário se a condição foi atendida quando isso alterar o preço.

## Uso do script Python

Use `scripts/calcular_compra.py` para cálculos monetários.

O script possui três operações:

- `item`: calcula o preço aplicado e o subtotal de um produto;
- `carrinho`: recalcula todos os itens e o total da compra;
- `conferir`: compara o total esperado com o total cobrado.

### Dados para calcular um item

Forneça ao script:

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

Não inclua um campo quando a informação correspondente não existir na etiqueta.

Use a saída JSON do script como fonte dos valores calculados. Não substitua um cálculo concluído com sucesso por cálculo estimado em linguagem natural.

## Registrar item

Antes de registrar um item, confirme que existem:

- identificação do produto;
- quantidade comprada;
- preço aplicável.

Após o cálculo, acrescente o item à compra atual e responda:

```text
Item registrado

Produto: [nome]
Quantidade: [quantidade de embalagens]
Preço unitário aplicado: R$ [valor]
Regra aplicada: [preço normal ou condição promocional]
Subtotal: R$ [valor]
Total acumulado: R$ [valor]
```

Se houver incerteza relevante, não registre o item até receber a correção.

## Alterar o carrinho

Aceite comandos como:

- "Corrija a quantidade do arroz para 3."
- "Remova o café."
- "O preço correto é R$ 18,90."
- "A promoção exige 4 unidades."
- "Mostre o carrinho."

Depois de qualquer alteração:

1. atualize o item;
2. recalcule o carrinho com o script;
3. apresente o novo total acumulado.

## Mostrar carrinho

Quando o usuário pedir para mostrar o carrinho, apresente:

| Produto | Quantidade | Preço aplicado | Regra | Subtotal |
|---|---:|---:|---|---:|

Depois da tabela, informe:

- quantidade de produtos diferentes;
- total de unidades ou embalagens;
- total estimado da compra.

## Finalizar compra

Quando o usuário disser "Finalizar compra":

1. Verifique se existe algum item aguardando quantidade ou confirmação.
2. Se houver pendência, solicite somente a informação que estiver faltando.
3. Recalcule todos os itens usando a operação `carrinho`.
4. Defina o estado como "finalizada".
5. Apresente o relatório final.
6. Preserve os itens na conversa para possível conferência.

O relatório deve conter:

| Item | Produto | Quantidade | Preço unitário | Regra aplicada | Subtotal |
|---:|---|---:|---:|---|---:|

Apresente também:

```text
Produtos diferentes: [quantidade]
Total de unidades: [quantidade]
Total estimado: R$ [valor]
```

## Conferir valor do caixa

Se o usuário informar o valor apresentado pelo caixa:

1. Use a operação `conferir` do script.
2. Compare o valor cobrado com o total estimado.
3. Calcule a diferença como:

`diferença = total cobrado - total esperado`

Classifique o resultado como:

- valores iguais;
- possível cobrança a mais;
- possível cobrança a menos.

Apresente:

```text
Total esperado: R$ [valor]
Total informado pelo caixa: R$ [valor]
Diferença: R$ [valor]
Resultado: [classificação]
```

## Conferir comprovante

Se o usuário enviar uma fotografia do comprovante ou cupom:

1. Extraia os produtos, quantidades, preços, descontos e total cobrado.
2. Compare essas informações com os itens registrados.
3. Considere abreviações comuns no comprovante.
4. Não associe itens apenas por semelhança vaga.
5. Apresente as possíveis divergências.

Classifique cada item como:

- conferido;
- possível divergência;
- não localizado no comprovante;
- item adicional no comprovante;
- leitura inconclusiva.

Apresente as divergências em uma tabela:

| Produto | Esperado | Cobrado | Diferença | Situação |
|---|---:|---:|---:|---|

Se o comprovante estiver cortado, desfocado ou ilegível, não conclua que houve erro. Solicite somente uma nova imagem da parte necessária.

## Regras de confiabilidade

- Não invente produto, preço, quantidade, código ou promoção.
- Nunca presuma quantidade igual a 1.
- Mostre claramente informações incertas.
- Use o script para os cálculos monetários.
- Não aplique promoção sem verificar suas condições.
- Use reais brasileiros no formato `R$ 0,00`.
- Considere os cálculos como estimativas para conferência.
- Não apresente o relatório como prova definitiva de cobrança indevida.
- Mantenha todos os dados da compra na mesma conversa.