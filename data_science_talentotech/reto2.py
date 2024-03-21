import pandas as pd

datos_ventas = [
        {'producto': 'Grafitos', 'region': 'Norte', 'ventas': 100, 'gastos': 50},
        {'producto': 'Bloqueador', 'region': 'Sur', 'ventas': 150, 'gastos': 75},
        {'producto': 'Grafitos', 'region': 'Oriente', 'ventas': 120, 'gastos': 60},
        {'producto': 'Bloqueador', 'region': 'Centro', 'ventas': 80, 'gastos': 40},
        {'producto': 'Bloqueador', 'region': 'Sur', 'ventas': 50, 'gastos': 30},
        {'producto': 'Peptidos', 'region': 'Centro', 'ventas': 180, 'gastos': 48},
        {'producto': 'Platino', 'region': 'Norte', 'ventas': 20, 'gastos': 8},
        {'producto': 'Platino', 'region': 'Centro', 'ventas': 135, 'gastos': 14},
        {'producto': 'Grafitos', 'region': 'Sur', 'ventas': 160, 'gastos': 30},
        {'producto': 'Peptidos', 'region': 'Sur', 'ventas': 60, 'gastos': 15}
    ]

df = pd.DataFrame(datos_ventas)

name_product = input()

product = df[df['producto'] == name_product]
if not product.empty:
    regions = []
    for i in product['region']:
        if i not in regions:
            regions.append(i)
    maximum = product['ventas'].max()
    region_max = product['region'][product['ventas'] == maximum]

    print(', '.join(regions))
    print(region_max.to_string(index = False))
else:
    print('Producto no encontrado')