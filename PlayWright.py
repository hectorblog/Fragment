from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.debugger_address = "localhost:9222"

# Подключение к уже запущенному браузеру
driver = webdriver.Chrome(options=options)

# Открытие страницы (если она не открыта)
driver.get('https://fragment.com/stars/buy')

# Проверка и нажатие на крестик для удаления предыдущего пользователя
try:
    clear_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span.icon-before.icon-search-clear.tm-search-clear.js-form-clear'))
    )
    clear_button.click()
except:
    pass  # Продолжать, если элемент не найден

# Чтение данных из файла
with open('users.txt', 'r') as file:
    lines = file.readlines()

# Проверка, что файл содержит необходимые строки
if len(lines) < 2:
    raise ValueError("Файл 'users.txt' должен содержать как минимум две строки: имя пользователя и количество звезд.")

username_line = lines[0].strip().split('. ')
quantity_line = lines[1].strip().split('. ')

# Проверка, что строки содержат необходимые элементы
if len(username_line) < 2 or len(quantity_line) < 2:
    raise ValueError("Каждая строка в файле 'users.txt' должна содержать точку и пробел для разделения.")

username = username_line[1]
quantity = quantity_line[1]

# Ввод имени пользователя
user_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'query'))
)
user_input.send_keys(username)

# Ввод количества звезд
quantity_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'quantity'))
)
quantity_input.send_keys(quantity)

# Нажатие кнопки покупки
buy_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.js-stars-buy-btn'))
)
driver.execute_script("arguments[0].click();", buy_button)

# Ожидание и нажатие кнопки "Buy Stars for Ritual MM"
buy_stars_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.tm-button-label.js-buy-stars-button'))
)
driver.execute_script("arguments[0].click();", buy_stars_button)

# Ожидание завершения действий
time.sleep(5)

# Закрытие браузера (не обязательно, если ты хочешь оставить браузер открытым)
# driver.quit()


# "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\Users\Hakuji Soyama\AppData\Local\Google\Chrome\User Data"
