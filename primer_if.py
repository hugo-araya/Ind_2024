# Si gasto hasta $100, pago con dinero en efec=vo.
# Sino, si gasto más de $100 pero menos de $300,
# pago con tarjeta de débito. Sino, pago con tarjeta de crédito.
gasto = int(input('gasto: '))
if gasto < 100:
    print('Pago con efectivo')
if gasto >= 100 and gasto < 300:
    print('Pagar con debito')
if gasto >= 300:
    print('Pagar credito')
