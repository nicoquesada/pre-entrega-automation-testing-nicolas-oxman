from funciones import iniciar_driver, login
from selenium.webdriver.common.by import By


def test_navegacion_inventario():
    driver, wait = iniciar_driver()

    try:
        login(driver, wait)

        # 1 Validar título de página
        titulo = driver.title
        assert titulo == "Swag Labs", f"Título incorrecto: {titulo}"
        print(f"✅ Título validado: {titulo}")

        # 2 Verificar productos visibles
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(productos) > 0, "No se encontraron productos en el inventario"
        print(f"✅ {len(productos)} productos visibles en la página")

        # 3 Mostrar nombre y precio del primero
        primer = productos[0]
        nombre = primer.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio = primer.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"🛍️ Primer producto: {nombre} | Precio: {precio}")

        # 4 Validar interfaz
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert menu.is_displayed() and filtro.is_displayed(), "Menú o filtro no visibles"
        print("✅ Menú y filtro visibles correctamente")

    except Exception as e:
        print(f"❌ Error en test_navegacion: {e}")
        driver.save_screenshot("reports/error_navegacion.png")
        raise
    finally:
        driver.quit()
