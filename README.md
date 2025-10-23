# pre-entrega-automation-testing-nicolas-oxman
Pruebas automatizadas para el sitio Sauce Demo, desarrolladas en Python con Pytest y Selenium WebDriver. Valida funciones clave como login, inventario y carrito, aplicando buenas prácticas de testing y generación de reportes HTML.
 
Propósito del proyecto
Con el fin de ahorrar tiempo y recursos, se quiere automatizar flujos críticos de módulos de:

Pantalla de Login, utilizando datos válidos e inválidos
Menú principal, con submenues, filtros, y catálogo de productos
Carrito de compras, al agregar productos al mismo
Tecnologías usadas
Python
Selenium webdriver (Levantar browser automatizado)
pytest (test unitarios)
Estructura de carpetas
README.md

pytest.ini (Configuraciones iniciales pytest)

test/

funciones.py 
test_login.py
test_nav_inv.py
test_carrito.py
reportes.html
Ejecución de tests
Para correr todos los tests, utilizar el siguiente archivo
run.py
