# הפרויקטים שלי 🚀

שלום! אני **עידן שמידט**, בודק תוכנה ג'וניור עם ידע ב-Manual וב-Automation Testing, **Python**, **Selenium** ו-**ISTQB Certified**.  
כאן תמצאו את הפרויקטים שלי מהקורס, כולל פרויקטים ידניים, אוטומציה ומסמכי בדיקה.

---

## פרויקט אוטומציה 🐾

### סקריפט בדיקות אוטומציה (Python + Selenium)

זהו סקריפט אוטומציה שבודק תהליך התחברות לאתר חנות חיות (JPetStore).  
הבדיקה כוללת הכנסת שם משתמש שגוי, סיסמה תקינה, לחיצה על כפתור LOGIN ובדיקת הודעת השגיאה הצפויה.

**קישור להורדת הסקריפט:** [MyScriptProject.py](MyScriptProject.py)

**קטע קוד לדוגמה:**

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jpetstore.aspectran.com/")

sign_in_button = driver.find_element(By.CLASS_NAME, "btn-outline-light")
sign_in_button.click()
time.sleep(3)

username = driver.find_element(By.ID, "username")
username.send_keys("david")

password = driver.find_element(By.ID, "password")
password.send_keys("I1234")

driver.find_element(By.CLASS_NAME, "text-center").click()
time.sleep(3)

error = driver.find_element(By.CLASS_NAME, "alert-danger")
print("Error message:", error.text)

if "Invalid username or password" in error.text:
    print("עבר - בדיקה הצליחה")
else:
    print("נכשל - הודעה לא תואמת")

driver.quit()
````

---

## פרויקטים של STR 📄

### דו"ח תוצאות בדיקות (STR)

מסמך STR מסכם את תוצאות הבדיקות שבוצעו בפרויקט, כולל סטטוס כל בדיקה (עבר/נכשל), בעיות שהתגלו במהלך הרצת התסריטים והמלצות לשיפורים.

**קישורים למסמכים:**

* [צפה במסמך STR](https://docs.google.com/document/d/1ZHkW4pmOGvSDEkcUjwAW_d1bCNb04D7-/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true)
* [צפה במסמך STR3](https://docs.google.com/document/d/1syDS0rET1S3G7hf44xITtaut-oxyeAo3/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true)

---

## פרויקטים של STP 📋

### מסמך תוכנית בדיקות (STP)

מסמך STP מפרט את אסטרטגיית הבדיקות, היקף הבדיקות, סביבת העבודה, כלי הבדיקה והשיטות בהן השתמשתי במהלך הפרויקט.

**קישורים למסמכים:**

* [צפה במסמך STP](https://docs.google.com/document/d/1JtMgr5dU9URAdJ7VXqxckaiarcgpRlpQ/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true)
* [צפה במסמך STP3](https://docs.google.com/document/d/14S3nZwK5bVuJcRWk5nR6qEZ41IQAXV7F/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true)

## מסמך דו"ח הרצה\תקלה  ⚡

### דו"ח הרצה\תקלה  (TER)

מסמך זה מפרט את מקרי הבדיקה שהורצו, התוצאה הצפויה והתוצאה בפועל, כולל סטטוס ההרצה.

**קישורים למסמכים:**

* [צפה במסמך דו"ח הרצה\תקלה](https://docs.google.com/spreadsheets/d/1OEnQ_YLOUShtHNLHoUYGdec5xxerhPdl/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true)



