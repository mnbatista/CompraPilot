# Configuração do CompraPilot no Agent Builder

Este guia explica como recriar o CompraPilot no Microsoft 365 Copilot Agent Builder usando os arquivos disponíveis neste repositório.

## 1. Visão geral

O CompraPilot é um agente pessoal para acompanhamento de compras em supermercados.

O agente pode:

- registrar uma lista de compras;
- interpretar fotografias de etiquetas;
- solicitar a quantidade comprada;
- calcular subtotais e total acumulado;
- interpretar promoções por quantidade;
- informar itens ainda não comprados;
- gerar um relatório final;
- comparar o total esperado com o total do caixa;
- auxiliar na conferência de comprovantes;
- gerar insights de economia.

> O CompraPilot é um projeto independente e open source. O funcionamento dos recursos depende das funcionalidades e licenças disponíveis no ambiente Microsoft 365 do usuário.

---

## 2. Pré-requisitos

Antes de configurar o agente, verifique se o ambiente possui:

- acesso ao Microsoft 365 Copilot;
- acesso ao Agent Builder;
- permissão para criar agentes;
- suporte ao envio de imagens na conversa;
- acesso ao recurso de habilidades personalizadas;
- permissão para importar um pacote de habilidade ZIP.

As habilidades personalizadas podem estar disponíveis apenas em ambientes participantes de programas de versão prévia.

---

## 3. Criar o agente

No Microsoft 365 Copilot:

1. Acesse **Agentes e habilidades**.
2. Selecione **Novo agente**.
3. Abra a guia **Configurar**.
4. Preencha os campos conforme as seções seguintes.

---

## 4. Identidade do agente

### Nome

```text
CompraPilot
```

### Descrição curta

```text
Assistente pessoal para compras inteligentes.
```

### Descrição completa

```text
Acompanhe sua lista de compras, registre produtos a partir de fotos das etiquetas, monitore o valor acumulado da compra, confira promoções e identifique oportunidades de economia.

Ao finalizar, receba um relatório detalhado com os itens comprados, o valor estimado da compra e possíveis divergências entre os preços registrados e os valores cobrados no caixa.
```

A descrição também está disponível em:

```text
agent/descricao.md
```

---

## 5. Ícone

Utilize o arquivo:

```text
assets/icon.png
```

O ícone do CompraPilot combina:

- carrinho de compras;
- lista de verificação;
- brilho associado à inteligência artificial;
- paleta azul e verde-água.

Se o Agent Builder solicitar um formato diferente, redimensione a imagem sem alterar sua proporção.

---

## 6. Instruções

Copie integralmente o conteúdo do arquivo:

```text
agent/instrucoes.md
```

Cole no campo **Instruções** do Agent Builder.

Antes de salvar, confirme se a primeira definição contém:

```text
Você é o CompraPilot, um assistente pessoal para compras inteligentes.
```

Não mantenha referências ao nome antigo `ConferePreço`.

As instruções devem orientar o agente a usar a habilidade `auditoria-compras` para cálculos, promoções, finalização e conferência.

---

## 7. Adicionar a habilidade

A habilidade do CompraPilot está localizada em:

```text
skill/
```

A estrutura esperada é:

```text
skill/
├── SKILL.md
└── scripts/
    └── calcular_compra.py
```

### Criar o pacote ZIP

O arquivo ZIP deve possuir esta estrutura interna:

```text
auditoria-compras.zip
├── SKILL.md
└── scripts/
    └── calcular_compra.py
```

O arquivo `SKILL.md` deve aparecer diretamente na raiz do ZIP.

Não use esta estrutura:

```text
auditoria-compras.zip
└── auditoria-compras/
    ├── SKILL.md
    └── scripts/
```

### Importar a habilidade

No Agent Builder:

1. Localize a seção **Habilidades**.
2. Selecione **Adicionar**.
3. Escolha a opção para importar uma habilidade.
4. Envie o arquivo `auditoria-compras.zip`.
5. Confirme se o nome apresentado é `auditoria-compras`.
6. Revise a descrição e os arquivos incluídos.
7. Salve ou atualize o agente.

### Funções da habilidade

A habilidade possui três operações conceituais:

- `item`: calcula o preço aplicável e o subtotal;
- `carrinho`: recalcula os itens e o total da compra;
- `conferir`: compara o total esperado com o valor cobrado.

---

## 8. Conhecimento

O MVP do CompraPilot não exige fontes adicionais de conhecimento.

Não é necessário adicionar:

- arquivos corporativos;
- sites externos;
- bibliotecas do SharePoint;
- manuais de supermercados;
- tabelas de preços.

As informações da compra devem vir diretamente:

- das mensagens do usuário;
- das fotografias das etiquetas;
- da lista de compras;
- do comprovante enviado;
- dos cálculos da habilidade.

Fontes de conhecimento poderão ser adicionadas futuramente para interpretar regras específicas de promoções, unidades de medida ou programas de fidelidade.

---

## 9. Conteúdo de trabalho

Para um agente pessoal de compras, aplique o princípio do menor acesso necessário.

### Arquivos na nuvem

Configuração recomendada:

```text
Desativado
```

O CompraPilot não precisa pesquisar todos os arquivos do usuário para acompanhar uma compra.

### Outlook

Configuração recomendada:

```text
Desativado
```

O CompraPilot não precisa pesquisar e-mails.

### Teams

Configuração recomendada:

```text
Desativado
```

O CompraPilot não precisa pesquisar mensagens ou reuniões.

### Conectores do Copilot

Configuração inicial recomendada:

```text
Nenhum
```

Conectores poderão ser avaliados em versões futuras, mas não são necessários para o MVP.

### Pesquisa na Web

Configuração recomendada para o MVP:

```text
Desativado
```

Os preços utilizados nos cálculos devem vir das etiquetas enviadas pelo usuário, não de pesquisas na internet.

A pesquisa na Web poderá ser testada futuramente para comparações de preços, desde que o agente diferencie claramente:

- preço fotografado no estabelecimento;
- preço encontrado na internet;
- preço esperado da compra atual.

### Anexos

Mantenha habilitado o recurso que permite ao usuário anexar imagens à conversa, quando disponível.

O envio de imagens é necessário para:

- etiquetas de preço;
- comprovantes;
- cupons fiscais;
- listas de compras fotografadas.

---

## 10. Prompts sugeridos

Cadastre os seguintes títulos e mensagens.

### Iniciar compra

```text
Iniciar uma nova compra. Vou enviar fotos das etiquetas e informar as quantidades dos produtos comprados.
```

### Mostrar carrinho

```text
Mostre o carrinho atual com todos os produtos registrados, quantidades, subtotais e o total acumulado.
```

### Finalizar compra

```text
Finalize a compra e gere o relatório completo com todos os itens, preços aplicados, promoções utilizadas e total estimado.
```

### Conferir valor do caixa

```text
Quero comparar o valor informado pelo caixa com o total estimado da compra.
```

### Conferir cupom fiscal

```text
Vou enviar uma foto do cupom fiscal. Analise os itens e compare com os produtos registrados na compra.
```

### Mostrar itens faltantes

```text
Compare minha lista de compras com os produtos registrados e mostre os itens que ainda não foram encontrados ou comprados.
```

### Registrar lista de compras

```text
Vou enviar minha lista de compras. Registre os itens e acompanhe o que for sendo comprado durante a compra.
```

### Analisar economia

```text
Analise as promoções registradas e identifique oportunidades reais de economia ou possíveis pegadinhas.
```

### Resumo rápido

```text
Mostre um resumo da compra até agora com quantidade de produtos, valor acumulado e itens pendentes da lista.
```

Os prompts também estão documentados em:

```text
agent/prompts-sugeridos.md
```

---

## 11. Modo de resposta

Utilize inicialmente:

```text
Automático
```

O agente deve responder de forma:

- objetiva;
- clara;
- organizada;
- adequada ao uso em dispositivos móveis;
- transparente sobre leituras incertas.

Valores monetários devem utilizar o formato brasileiro:

```text
R$ 0,00
```

---

## 12. Salvar e atualizar

Após preencher todos os campos:

1. Revise o nome e a descrição.
2. Confirme que as instruções mencionam `CompraPilot`.
3. Confirme que a habilidade aparece como `auditoria-compras`.
4. Revise os prompts sugeridos.
5. Selecione **Criar** ou **Atualizar**.
6. Abra a área de visualização e execute os testes descritos a seguir.

---

## 13. Teste básico

### Teste 1: iniciar compra

Envie:

```text
Iniciar compra
```

Resposta esperada:

```text
Compra iniciada. Envie a foto da primeira etiqueta e informe a quantidade colocada no carrinho.
```

---

### Teste 2: quantidade ausente

Envie uma fotografia de etiqueta sem informar a quantidade.

Resposta esperada:

```text
Quantas unidades desse produto você colocou no carrinho?
```

O agente não deve presumir quantidade igual a 1.

---

### Teste 3: promoção atingida

Utilize um produto com:

```text
Preço normal: R$ 57,99
Preço promocional: R$ 54,99
Quantidade mínima: 3
Quantidade comprada: 3
```

Resultado esperado:

```text
Preço aplicado: R$ 54,99
Subtotal: R$ 164,97
Regra: preço promocional aplicado a partir de 3 unidades
```

---

### Teste 4: promoção não atingida

Utilize o mesmo produto com quantidade 2.

Resultado esperado:

```text
Preço aplicado: R$ 57,99
Subtotal: R$ 115,98
Regra: preço normal aplicado porque a quantidade mínima não foi atingida
```

---

### Teste 5: múltiplos produtos

Registre pelo menos dois produtos e envie:

```text
Mostrar carrinho
```

Confirme se o agente apresenta:

- todos os produtos;
- quantidades corretas;
- preço aplicado;
- subtotal de cada produto;
- total acumulado correto.

---

### Teste 6: correção de item

Envie:

```text
Corrija a quantidade do primeiro produto para 4.
```

Confirme se o agente:

1. altera somente o item solicitado;
2. recalcula o subtotal;
3. recalcula o total acumulado;
4. mantém os demais itens.

---

### Teste 7: finalização

Envie:

```text
Finalizar compra
```

Confirme se o relatório contém:

- produto;
- quantidade;
- preço unitário;
- regra aplicada;
- subtotal;
- produtos diferentes;
- total de unidades;
- total estimado.

---

### Teste 8: conferência do caixa

Após finalizar, envie:

```text
O caixa informou um total de R$ 173,97.
```

Confirme se o agente mostra:

- total esperado;
- total informado;
- diferença;
- classificação da diferença.

---

### Teste 9: comprovante

Envie uma fotografia legível do comprovante.

Confirme se o agente não inventa itens ou valores quando uma parte da imagem estiver ilegível.

---

## 14. Critérios de aprovação

A configuração pode ser considerada válida quando o CompraPilot:

- não registra produtos sem quantidade;
- não inventa preços ilegíveis;
- distingue conteúdo da embalagem de quantidade comprada;
- aplica promoções somente quando as condições são atendidas;
- mantém múltiplos produtos na conversa;
- recalcula o carrinho após correções;
- apresenta o total correto;
- preserva os registros depois da finalização;
- informa incertezas na leitura do comprovante.

---

## 15. Limitações conhecidas

- Os dados do carrinho são mantidos no contexto da conversa atual.
- Uma nova conversa pode não recuperar uma compra anterior.
- Fotografias desfocadas, cortadas ou com reflexos podem prejudicar a leitura.
- Descrições abreviadas no cupom podem dificultar a associação com a etiqueta.
- Promoções de clube, CPF, aplicativo, cartão ou forma de pagamento exigem confirmação.
- O resultado deve ser tratado como estimativa para conferência.
- A disponibilidade de habilidades e execução de scripts depende do ambiente Microsoft 365.

---

## 16. Privacidade

Antes de compartilhar imagens, revise se o comprovante contém:

- CPF;
- dados de pagamento;
- identificação pessoal;
- códigos ou informações que não deseja compartilhar.

O CompraPilot não precisa de acesso amplo ao Outlook, Teams ou arquivos corporativos para executar sua função principal.

---

## 17. Solução de problemas

### A habilidade não é aceita

Verifique se:

- o arquivo se chama exatamente `SKILL.md`;
- o YAML está no início do arquivo;
- o YAML contém `name` e `description`;
- o `SKILL.md` está na raiz do ZIP;
- o arquivo Python está dentro de `scripts/`;
- os arquivos foram salvos em UTF-8;
- os arquivos não possuem extensões ocultas como `.txt`.

### O Markdown aparece como HTML

O conteúdo provavelmente foi copiado de um editor de texto rico.

Remova elementos como:

```text
<ol>
<li>
<br>
<code>
```

Edite os arquivos usando Visual Studio Code, Notepad++ ou outro editor de texto simples.

### O agente não solicita a quantidade

Confirme se `agent/instrucoes.md` e `skill/SKILL.md` contêm a regra:

```text
Nunca presuma quantidade igual a 1.
```

### O agente aplica a promoção incorretamente

Confirme se foram extraídos:

- preço normal;
- preço promocional;
- quantidade mínima;
- quantidade comprada;
- demais condições da promoção.

### O carrinho perde itens

Mantenha toda a compra na mesma conversa e evite iniciar outro chat antes da finalização.

---

## 18. Próximos passos

Após validar a configuração:

1. execute uma compra real com poucos produtos;
2. registre erros de leitura;
3. compare os cálculos com o caixa;
4. documente os resultados;
5. abra uma issue no repositório para cada melhoria identificada.

Consulte também:

- `docs/instalacao.md`;
- `docs/arquitetura.md`;
- `docs/roadmap.md`;
- `exemplos/compra-simples.md`;
- `exemplos/promocao-atacado.md`;
- `exemplos/conferencia-caixa.md`.