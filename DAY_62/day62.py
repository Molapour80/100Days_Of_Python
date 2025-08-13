from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# تنظیمات مرورگر (اختیاری)
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # باز کردن مرورگر در حالت تمام‌صفحه

# مسیر WebDriver (مثلاً chromedriver.exe)
driver_path = "path/to/chromedriver.exe"
service = Service(driver_path)

# راه‌اندازی مرورگر
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL فرم مورد نظر
form_url = "https://example.com/contact"  # جایگزین کنید با آدرس واقعی
driver.get(form_url)

try:
    # منتظر ماندن تا فرم بارگذاری شود (مطمئن‌سازی از وجود فیلدها)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))  # جایگزین کنید با المان واقعی
    )

    # پر کردن فیلدهای فرم
    driver.find_element(By.NAME, "username").send_keys("JohnDoe")  # فیلد نام کاربری
    driver.find_element(By.NAME, "email").send_keys("john@example.com")  # فیلد ایمیل
    driver.find_element(By.NAME, "message").send_keys("This is an automated form submission!")  # فیلد پیام

    # کلیک روی دکمه ارسال (با XPath, ID, یا CSS_SELECTOR)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # تأخیر برای مشاهده نتیجه (اختیاری)
    time.sleep(3)
    print("فرم با موفقیت ارسال شد!")

except Exception as e:
    print(f"خطا در اجرای اتوماسیون: {e}")

finally:
    # بستن مرورگر
    driver.quit()