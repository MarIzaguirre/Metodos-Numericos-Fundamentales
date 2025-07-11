import math

def newton_raphson(f, df, x0, error_max, max_iter):
    """
    Método de Newton-Raphson para encontrar raíces de funciones
    
    Parámetros:
    f : función diferenciable
    df : derivada de la función f
    x0 : aproximación inicial
    error_max : error máximo permitido
    max_iter : máximo número de iteraciones
    
    Retorna:
    (raiz, error, iteraciones) : tupla con la aproximación, error final e iteraciones
    """
    x_actual = x0
    error_actual = 1.0
    i = 0
    
    for i in range(1, max_iter + 1):
        fx = f(x_actual)
        dfx = df(x_actual)
        
        if dfx == 0:
            raise ValueError("Derivada cero. No se puede continuar.")
        
        x_nuevo = x_actual - fx / dfx
        error_actual = abs(x_nuevo - x_actual)
        
        print(f"Iteración {i}: x = {x_nuevo:.6f}, error = {error_actual:.6f}")
        
        if error_actual < error_max:
            print(f"\nConvergencia alcanzada en {i} iteraciones")
            print(f"Error final: {error_actual:.6f}")
            return x_nuevo, error_actual, i
        
        x_actual = x_nuevo
    
    print(f"\nAdvertencia: Máximo de iteraciones ({max_iter}) alcanzado")
    print(f"Último error obtenido: {error_actual:.6f}")
    return x_actual, error_actual, max_iter

if __name__ == "__main__":
    # Función a analizar: x² - 2 = 0 (solución es √2 ≈ 1.414213)
    def f(x):
        return x**2 - 2
    
    def df(x):
        return 2*x
    
    # Parámetros del método
    x0 = 1.0          # Aproximación inicial
    error_max = 0.03   # Error máximo permitido
    max_iter = 1000     # Máximo de iteraciones
    
    # Aplicar método
    try:
        raiz, error, iteraciones = newton_raphson(f, df, x0, error_max, max_iter)
        
        # Mostrar resultados
        print(f"\nRaíz aproximada: {raiz:.6f}")
        print(f"Error relativo: {error:.6f}")
        print(f"Iteraciones realizadas: {iteraciones}")
        print(f"Valor exacto √2: {math.sqrt(2):.6f}")
        print(f"Diferencia con valor exacto: {abs(raiz - math.sqrt(2)):.6f}")
        
    except ValueError as e:
        print(f"\nError: {e}")