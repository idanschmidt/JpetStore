<html lang="he">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>הפרויקטים שלי</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: WHITE;
      color: #333;
      margin: 0;
      padding: 0;
      direction: rtl;
      text-align: center;
    }
    header {
      background-color: WHITE;
      color: white;
      padding: 20px 0;
    }
    h1 {
      margin: 0;
    }
    main {
      padding: 30px;
    }
  </style>
</head>
<body>
  <header>
    <h1>הפרויקטים שלי</h1>
  </header>
 
  <main>
    <html lang="he">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>סקריפט אוטומציה</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: WHITE;
      color: #333;
      margin: 0;
      padding: 0;
      direction: rtl;
      text-align: center;
    }
    header {
      background-color: BLUE;
      color: white;
      padding: 20px 0;
    }
    h1 {
      margin: 0;
    }
    main {
      padding: 30px;
    }
    pre {
      text-align: left;
      background-color:BLUE;
      padding: 20px;
      border-radius: 10px;
      overflow-x: auto;
      max-height: 400px;
    }
    a {
      display: inline-block;
      margin-top: 20px;
      padding: 10px 20px;
      background-color:BLACK;
      color: white;
      text-decoration: none;
      border-radius: 8px;
    }
    a:hover {
      background-color: #005ea2;
    }
  </style>
</head>
<body>
  
    <h1>סקריפט בדיקות אוטומציה</h1>
 

  <main>
    <a href="MyScriptProject.py" download>הורד את הסקריפט שלי</a>

    <h2>תצוגת הקוד (חלקית)</h2>
    <pre>
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# פותח דפדפן חדש
 driver = webdriver.Chrome()

# בדיקות התחברות עבור משתמשים: idan ו-YUVAL
#הרצת בדיקות משתמש ראשון - idan
#בדיקה ראשונה
# ניווט לדף האתר
driver.get("https://jpetstore.aspectran.com/")

print("***תוצאה צפויה-Error message: Invalid username or password. Signon failed.")
#פעולה ראשונה-עבור לדף התחברות בלחיצה על כפתור SIGN IN
sign_in_button = driver.find_element(By.CLASS_NAME,"btn-outline-light")
sign_in_button.click()
time.sleep(5)
print("עבר לדף התחברות")

#פעולה שנייה-רשום שם משתמש שגוי
Username_field1=driver.find_element(By.ID,"username")
Username_field1.clear()
Username_field1.send_keys("david")
time.sleep(5)
print("כתיבת שם משתמש-david")

#פעולה שלישית- רשום סיסמה תקינה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("I1234")
time.sleep(5)
print("כתיבת סיסמה-I1234")

#פעולה רביעית- לחץ על כפתור LOGIN
log_in_button = driver.find_element(By.CLASS_NAME,"text-center")
log_in_button.click()
time.sleep(5)
print("לוחץ על כפתור -LOGIN")

#תוצאה
result=driver.find_element(By.CLASS_NAME,"alert-danger")
error_message_text=result.text
print("Error message:", error_message_text)

# השוואה בין תוצאה צפויה לתוצאה רצויה
expectedText ="Invalid username or password.  Signon failed."
if "Invalid username or password" in error_message_text:
    print("עבר-בדיקה ראשונה עברה בהצלחה")
else:
    print("נכשל-בדיקה ראשונה נכשלה")
print("\n")

 driver.quit()
    </pre>
  </main>
</body>
</html>

  </main>
</body>
</html>
