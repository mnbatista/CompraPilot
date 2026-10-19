import json
import sys
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

CENTAVOS = Decimal("0.01")


def decimal(valor, campo):
    """Converte números ou textos para Decimal com validação."""
    if valor is None:
        return None
    try:
        texto = str(valor).strip().replace("R$", "").replace(" ", "")
        if "," in texto and "." in texto:
            texto = texto.replace(".", "").replace(",", ".")
        elif "," in texto:
            texto = texto.replace(",", ".")
        return Decimal(texto)
    except (InvalidOperation, ValueError):
        raise ValueError(f"O campo '{campo}' contém um valor inválido.")



def dinheiro(valor):
    """Arredonda um valor monetário para duas casas decimais."""
    return valor.quantize(CENTAVOS, rounding=ROUND_HALF_UP)



def validar_quantidade(valor):
    if valor is None:
        raise ValueError("A quantidade comprada é obrigatória.")

    try:
        quantidade = int(valor)
    except (TypeError, ValueError):
        raise ValueError("A quantidade deve ser um número inteiro.")

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    return quantidade



def calcular_item(item):
    produto = str(item.get("produto", "")).strip()
    if not produto:
        raise ValueError("O nome do produto é obrigatório.")

    quantidade = validar_quantidade(item.get("quantidade"))

    preco_normal = decimal(item.get("preco_normal"), "preco_normal")
    preco_promocional = decimal(
        item.get("preco_promocional"), "preco_promocional"
    )

    minimo = item.get("quantidade_minima_promocao")
    condicoes_atendidas = item.get("condicoes_atendidas", True)

    if preco_normal is None and preco_promocional is None:
        raise ValueError(
            "Informe pelo menos o preço normal ou o preço promocional."
        )

    if minimo is not None:
        try:
            minimo = int(minimo)
        except (TypeError, ValueError):
            raise ValueError(
                "A quantidade mínima da promoção deve ser um número inteiro."
            )

        if minimo <= 0:
            raise ValueError(
                "A quantidade mínima da promoção deve ser maior que zero."
            )

    promocao_aplicavel = (
        preco_promocional is not None
        and condicoes_atendidas is True
        and (minimo is None or quantidade >= minimo)
    )

    if promocao_aplicavel:
        preco_aplicado = preco_promocional
        if minimo is not None:
            regra = f"Preço promocional aplicado a partir de {minimo} unidades"
        else:
            regra = "Preço promocional aplicado"
    else:
        if preco_normal is None:
            raise ValueError(
                "A promoção não foi atendida e não existe preço normal."
            )

        preco_aplicado = preco_normal

        if (
            preco_promocional is not None
            and minimo is not None
            and quantidade < minimo
        ):
            regra = (
                f"Preço normal aplicado: mínimo promocional de {minimo} unidades não atingido"
            )
        elif (
            preco_promocional is not None
            and condicoes_atendidas is not True
        ):
            regra = (
                "Preço normal aplicado: condições promocionais não confirmadas"
            )
        else:
            regra = "Preço normal aplicado"

    preco_aplicado = dinheiro(preco_aplicado)
    subtotal = dinheiro(preco_aplicado * quantidade)

    return {
        "produto": produto,
        "quantidade": quantidade,
        "preco_aplicado": float(preco_aplicado),
        "subtotal": float(subtotal),
        "regra_aplicada": regra,
    }



def calcular_carrinho(dados):
    itens_entrada = dados.get("itens")

    if not isinstance(itens_entrada, list) or not itens_entrada:
        raise ValueError("O carrinho deve conter pelo menos um item.")

    itens_calculados = []
    total = Decimal("0.00")
    total_unidades = 0

    for item in itens_entrada:
        calculado = calcular_item(item)
        itens_calculados.append(calculado)
        total += Decimal(str(calculado["subtotal"]))
        total_unidades += calculado["quantidade"]

    total = dinheiro(total)

    return {
        "itens": itens_calculados,
        "produtos_diferentes": len(itens_calculados),
        "total_unidades": total_unidades,
        "total_compra": float(total),
        "moeda": "BRL",
    }



def conferir_total(dados):
    esperado = decimal(dados.get("total_esperado"), "total_esperado")
    cobrado = decimal(dados.get("total_cobrado"), "total_cobrado")

    if esperado is None or cobrado is None:
        raise ValueError(
            "Os campos total_esperado e total_cobrado são obrigatórios."
        )

    esperado = dinheiro(esperado)
    cobrado = dinheiro(cobrado)
    diferenca = dinheiro(cobrado - esperado)

    if diferenca == 0:
        status = "valores_iguais"
        mensagem = "O valor cobrado corresponde ao total esperado."
    elif diferenca > 0:
        status = "cobrado_a_mais"
        mensagem = "O valor cobrado é maior que o total esperado."
    else:
        status = "cobrado_a_menos"
        mensagem = "O valor cobrado é menor que o total esperado."

    return {
        "total_esperado": float(esperado),
        "total_cobrado": float(cobrado),
        "diferenca": float(diferenca),
        "status": status,
        "mensagem": mensagem,
        "moeda": "BRL",
    }



def executar():
    if len(sys.argv) < 3:
        raise ValueError(
            "Uso: calcular_compra.py <item|carrinho|conferir> '<JSON>'"
        )

    operacao = sys.argv[1].strip().lower()
    dados = json.loads(sys.argv[2])

    if operacao == "item":
        resultado = calcular_item(dados)
    elif operacao == "carrinho":
        resultado = calcular_carrinho(dados)
    elif operacao == "conferir":
        resultado = conferir_total(dados)
    else:
        raise ValueError(
            "Operação inválida. Use item, carrinho ou conferir."
        )

    print(
        json.dumps(
            {"sucesso": True, "resultado": resultado},
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    try:
        executar()
    except Exception as erro:
        print(
            json.dumps(
                {"sucesso": False, "erro": str(erro)},
                ensure_ascii=False,
            )
        )
        sys.exit(1)

