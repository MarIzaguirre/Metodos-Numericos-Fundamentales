def trapecio(f, a, b, n):
    """
    Calcula la integral aproximada usando la regla del trapecio
    
    Parámetros:
    f : función a integrar
    a : límite inferior
    b : límite superior
    n : número de subintervalos
    
    Retorna:
    float: aproximación de la integral
    """
    h = (b - a) / n  # Ancho de cada subintervalo
    suma = 0.5 * (f(a) + f(b))  # Suma de los extremos
    
    for i in range(1, n):
        x = a + i * h
        suma += f(x)
    
    return suma * h

# Ejemplo de uso
if __name__ == "__main__":
    # Función a integrar:
    def f(x):
        return 3 * x * ((x**2 + 1)**0.5)  # Corregida la sintaxis
    
    # Parámetros de integración
    a = 1.0  # Límite inferior (como float)
    b = 2.0  # Límite superior (como float)
    n = 4    # Número de subintervalos
    
    # Cálculo de la integral
    resultado = trapecio(f, a, b, n)
    valor_real = 8.35191276275
    
    # Resultados
    print(f"Regla del Trapecio (n={n})")
    print(f"Aproximación: {resultado:.8f}")
    print(f"Valor real:    {valor_real:.8f}")
    print(f"Error absoluto: {abs(resultado - valor_real):.6f}")
    print(f"Error relativo: {abs((resultado - valor_real)/valor_real):.6f}")