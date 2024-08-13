a = float(input('ingrese el valor de a:'))
b = float(input('ingrese el valor de b:'))
c = float(input('ingrese el valor de c:'))

AreaRectangulo = a*b
AreaTriangulo = a-c *b / 2
AreaTotal = AreaRectangulo+AreaTriangulo
print('el area del triangulo es', AreaTriangulo, 'el area del rectangulo es', AreaRectangulo,'el area total es', AreaTotal)
