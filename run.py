import pytest

# Lista de archivos de pruebas a ejecutar
test_files = [
    "test-login.py",
    "test_nav_inv.py",
    "test_carrito.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report1.html","--self-contained-html","-v"]

pytest.main(pytest_args)