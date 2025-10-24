import pytest
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

test_files = [
    os.path.join(BASE_DIR, "tests", "test_login.py"),
    os.path.join(BASE_DIR, "tests", "test_inventory.py"),
    os.path.join(BASE_DIR, "tests", "test_carrito.py")
]

pytest_args = test_files + ["--html=report.html", "--self-contained-html", "-v"]
pytest.main(pytest_args)
