#מייבא פונקציית זמן,מודל דפדפן,ומחלקה שמאפשרת בחירת אלמנטים לפי מזהים שונים
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#פותח דפדפן חדש
driver = webdriver.Chrome()
#סקריפט בדיקות התחברות לאתר
#בדיקות עבור שני משתמשים: YUVAL and idan

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

#בדיקה שנייה
# ניווט לדף האתר
driver.get("https://jpetstore.aspectran.com/")
print("***תוצאה צפויה-Error message: Invalid username or password. Signon failed.")
#פעולה ראשונה-עבור לדף התחברות בלחיצה על כפתור SIGN IN
sign_in_button = driver.find_element(By.CLASS_NAME,"btn-outline-light")
sign_in_button.click()
time.sleep(5)
print("עבר לדף התחברות")

#פעולה שנייה-רשום שם משתמש תקין
Username_field1=driver.find_element(By.ID,"username")
Username_field1.clear()
Username_field1.send_keys("idan")
time.sleep(5)
print("כתיבת שם משתמש-idan")

#פעולה שלישית- רשום סיסמה שגויה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("5555")
time.sleep(5)
print("כתיבת סיסמה-5555")

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
    print("עבר-בדיקה שנייה עברה בהצלחה")
else:
    print("נכשל-בדיקה שנייה נכשלה")

print("\n")

#בדיקה שלישית
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

#פעולה שלישית- רשום סיסמה שגויה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("5555")
time.sleep(5)
print("כתיבת סיסמה-5555")

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
    print("עבר-בדיקה שלישית עברה בהצלחה")
else:
    print("נכשל-בדיקה שלישית נכשלה")

print("\n")

#בדיקה רביעית
# ניווט לדף האתר
driver.get("https://jpetstore.aspectran.com/")
print("***תוצאה צפויה- מתחבר")
#פעולה ראשונה-עבור לדף התחברות בלחיצה על כפתור SIGN IN
sign_in_button = driver.find_element(By.CLASS_NAME,"btn-outline-light")
sign_in_button.click()
time.sleep(5)
print("עבר לדף התחברות")

#פעולה שנייה-רשום שם משתמש תקינה
Username_field1=driver.find_element(By.ID,"username")
Username_field1.clear()
Username_field1.send_keys("idan")
time.sleep(5)
print("כתיבת שם משתמש-idan")

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

#פעולה חמישית- מצא את כפתור SIGNOUT+MY ACCOUNT
sign_out_button=driver.find_element(By.ID,"dropdownMenuButton")
sign_out_button.click()
time.sleep(5)
print("מוצגת הודעת WELCOME IDAN+מוצא את כפתור SIGNOUT")

#תוצאה
result = driver.find_element(By.LINK_TEXT, "Sign Out")
actualText = result.text
print("actual:", actualText)

# השוואה בין תוצאה צפויה לתוצאה רצויה
expectedText = "Sign Out"
if actualText == expectedText:
    print("עבר - התחברות הצליחה(בדיקה רביעית)")
else:
    print("נכשל - התחברות לא הצליחה(בדיקה רביעית)")

print("\n")

print("הסתיימה הרצת בדיקות משתמש ראשון - idan")
print("\n" + "*" * 80 + "\n")

driver.quit()

#פותח דפדפן חדש
driver = webdriver.Chrome()

#YUVAL - הרצת בדיקות משתמש שני
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
Username_field1.send_keys("RONI")
time.sleep(5)
print("כתיבת שם משתמש-RONI")

#פעולה שלישית- רשום סיסמה תקינה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("Y4321")
time.sleep(5)
print("כתיבת סיסמה-Y4321")

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

#בדיקה שנייה
# ניווט לדף האתר
driver.get("https://jpetstore.aspectran.com/")
print("***תוצאה צפויה-Error message: Invalid username or password. Signon failed.")
#פעולה ראשונה-עבור לדף התחברות בלחיצה על כפתור SIGN IN
sign_in_button = driver.find_element(By.CLASS_NAME,"btn-outline-light")
sign_in_button.click()
time.sleep(5)
print("עבר לדף התחברות")

#פעולה שנייה-רשום שם משתמש תקין
Username_field1=driver.find_element(By.ID,"username")
Username_field1.clear()
Username_field1.send_keys("YUVAL")
time.sleep(5)
print("כתיבת שם משתמש-YUVAL")

#פעולה שלישית- רשום סיסמה שגויה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("7777")
time.sleep(5)
print("כתיבת סיסמה-7777")

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
    print("עבר-בדיקה שנייה עברה בהצלחה")
else:
    print("נכשל-בדיקה שנייה נכשלה")

print("\n")

#בדיקה שלישית
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
Username_field1.send_keys("RONI")
time.sleep(5)
print("כתיבת שם משתמש-RONI")

#פעולה שלישית- רשום סיסמה שגויה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("7777")
time.sleep(5)
print("כתיבת סיסמה-7777")

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
    print("עבר-בדיקה שלישית עברה בהצלחה")
else:
    print("נכשל-בדיקה שלישית נכשלה")

print("\n")

#בדיקה רביעית
# ניווט לדף האתר
driver.get("https://jpetstore.aspectran.com/")
print("***תוצאה צפויה- מתחבר")
#פעולה ראשונה-עבור לדף התחברות בלחיצה על כפתור SIGN IN
sign_in_button = driver.find_element(By.CLASS_NAME,"btn-outline-light")
sign_in_button.click()
time.sleep(5)
print("עבר לדף התחברות")

#פעולה שנייה-רשום שם משתמש תקינה
Username_field1=driver.find_element(By.ID,"username")
Username_field1.clear()
Username_field1.send_keys("YUVAL")
time.sleep(5)
print("כתיבת שם משתמש-YUVAL")

#פעולה שלישית- רשום סיסמה תקינה
Password_field2=driver.find_element(By.ID,"password")
Password_field2.clear()
Password_field2.send_keys("Y4321")
time.sleep(5)
print("כתיבת סיסמה-Y4321")

#פעולה רביעית- לחץ על כפתור LOGIN
log_in_button = driver.find_element(By.CLASS_NAME,"text-center")
log_in_button.click()
time.sleep(5)
print("לוחץ על כפתור -LOGIN")

#פעולה חמישית- מצא את כפתור SIGNOUT+MY ACCOUNT
sign_out_button=driver.find_element(By.ID,"dropdownMenuButton")
sign_out_button.click()
time.sleep(5)
print("מוצגת הודעת WELCOME YUVAL+מוצא את כפתור SIGNOUT")

#תוצאה
result = driver.find_element(By.LINK_TEXT, "Sign Out")
actualText = result.text
print("actual:", actualText)

# השוואה בין תוצאה צפויה לתוצאה רצויה
expectedText = "Sign Out"
if actualText == expectedText:
    print("עבר - התחברות הצליחה(בדיקה רביעית)")
else:
    print("נכשל - התחברות לא הצליחה(בדיקה רביעית)")

print("\n")

print("הסתיימה הרצת הבדיקות משתמש שני - YUVAL")
print("הסתיימה הרצת הבדיקות")

driver.quit()