from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://automationexercise.com")

wait = WebDriverWait(driver, 10)

# ✅ Gérer cookies (version robuste)
try:
    accept_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Autoriser')]"))
    )
    accept_btn.click()
except:
    print("Bouton cookies non trouvé, on force suppression overlay")

    # 💥 solution de secours (très pro)
    driver.execute_script("""
        let overlay = document.querySelector('.fc-dialog-overlay');
        if (overlay) { overlay.remove(); }
    """)

# Cliquer sur login
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))).click()

# Remplir email
wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("s@gmail.com")

# Remplir mdp
driver.find_element(By.NAME, "password").send_keys("1234567890")

# Cliquer login
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# Vérification
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Logged in as')]")))

print("✅ Test login réussi")

driver.quit()