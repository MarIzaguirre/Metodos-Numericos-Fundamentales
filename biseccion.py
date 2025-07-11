import math

def biseccion(f, a, b, error_max, max_iter):
    """
    Método de bisección para encontrar raíces de funciones
    
    Parámetros:
    f : función continua
    a, b : intervalo inicial [a, b] donde f(a)*f(b) < 0
    error_max : error máximo permitido
    max_iter : máximo número de iteraciones
    
    Retorna:
    (raiz, error) : tupla con la aproximación y el error final
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b]")
    
    error_actual = 1.0
    m_anterior = a
    i = 0
    
    while error_actual > error_max and i < max_iter:
        m_actual = (a + b) / 2
        error_actual = abs((m_actual - m_anterior) / m_actual) if i > 0 else 1.0
        
        # Actualizar intervalo
        if f(a) * f(m_actual) < 0:
            b = m_actual
        elif f(m_actual) * f(b) < 0:
            a = m_actual
        else:
            return m_actual, error_actual
        
        m_anterior = m_actual
        i += 1
    
    return m_actual, error_actual

if __name__ == "__main__":
    # Función a analizar
    def f(x):
        return ((x - 2)**2) - math.log(x)
    
    # Parámetros del método
    a = 1.0  # Límite inferior del intervalo
    b = 2.0  # Límite superior del intervalo
    error_max = 0.05
    max_iter = 1000 
    
    raiz, error = biseccion(f, a, b, error_max, max_iter)
    
    print(f"Raíz aproximada: {raiz:.6f}")
    print(f"Error relativo: {error:.6f}")
    print(f"Valor de f(raíz): {f(raiz):.6f}")