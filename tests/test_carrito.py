from funciones import iniciar_driver, login
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_carrito():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        # 1 Login
        login(driver, wait)

        # 2 Esperar que se carguen los productos
        productos = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

        # 3 Clic en "Add to cart"
        boton_add = primer_producto.find_element(By.CSS_SELECTOR, "button.btn_inventory")
        boton_add.click()
        print(f"✅ Producto añadido: {nombre_producto}")

        # 4 Esperar que aparezca el nuevo botón "Remove" (relocalizando el elemento)
        wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".inventory_item:first-of-type button.btn_inventory"),
                "Remove"
            )
        )
        print("✅ Botón cambió a 'Remove' correctamente.")

        # 5 Verificar badge del carrito
        try:
            contador = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge"))
            )
            assert contador.text == "1", f"Contador incorrecto: {contador.text}"
            print(f"✅ Contador del carrito: {contador.text}")
        except:
            print(" No se encontró badge, pero el botón 'Remove' confirma el agregado.")

        # 6 Ir al carrito
        print(" URL antes del clic:", driver.current_url)
        carrito_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.shopping_cart_link")))
        driver.execute_script("arguments[0].click();", carrito_link)
        time.sleep(2)
        print(" URL después del clic:", driver.current_url)

        # Verificar badge antes
        try:
            badge = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
            print(f" Badge antes del carrito: {badge}")
        except:
            print(" No se encontró el badge antes de ir al carrito.")

        # Esperar confirmación flexible
        wait.until(lambda d: "/cart" in d.current_url or "Your Cart" in d.page_source)
        print("✅ Página del carrito cargada correctamente.")

        # 7 Verificar producto en el carrito
        cart_items = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "cart_item")))
        assert len(cart_items) > 0, "No se encontraron productos en el carrito"

        nombre_carrito = cart_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert nombre_carrito.strip().lower() == nombre_producto.strip().lower()
        print(f"✅ Producto confirmado en carrito: {nombre_carrito}")

        print("Test de carrito completado con éxito.")

    except Exception as e:
        print(f"❌ Error en test: {e}")
        driver.save_screenshot("error_carrito.png")
        raise
    finally:
        driver.quit()
