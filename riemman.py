def riemann(f, a, b, n):
    """
    Calcula la integral aproximada usando el método de Riemann
    
    Parámetros:
    f : función a integrar
    a : límite inferior
    b : límite superior
    n : número de subintervalos
    
    Retorna:
    float: aproximación de la integral
    """
    h = (b - a) / n  # Ancho de cada subintervalo
    suma = 0.0  # Inicializar la suma
    
    for i in range(n):
        x = a + i * h  # Punto izquierdo del subintervalo
        suma += f(x)  # Sumar el valor de la función en el punto
    
    return suma * h

# Ejemplo de uso
if __name__ == "__main__":
    # Función a integrar:
    def f(x):
        return 3 * x * ((x**2 + 1)**0.5)  # Corregida la sintaxis
    
    a = 1.0  # Límite inferior
    b = 2.0  # Límite superior
    n = 4  # Número de subintervalos
    
    resultado = riemann(f, a, b, n)
    valor_real = 8.35191276275
    
    print(f"Aproximación: {resultado:.6f}")
    print(f"Valor real: {valor_real:.6f}")
    print(f"Error relativo: {abs((valor_real - resultado)/valor_real):.6f}")