from funciones import iniciar_driver, login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    driver, wait = iniciar_driver()

    try:
        # Ejecutar login
        login(driver, wait)

        # Validar URL y título
        assert "/inventory.html" in driver.current_url, "❌ No se redirigió al inventario"
        titulo = driver.title
        assert "Swag Labs" in titulo, f"❌ Título incorrecto: {titulo}"

        print("✅ Login exitoso y validado correctamente")

    except Exception as e:
        print(f"❌ Error en test_login: {e}")
        driver.save_screenshot("reports/error_login.png")
        raise
    finally:
        driver.quit()
