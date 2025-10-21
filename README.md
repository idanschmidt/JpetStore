<html lang="he">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>הפרויקטים שלי</title>
  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background-color: #f7f9fc;
      color: #333;
      margin: 0;
      padding: 0;
      direction: rtl;
      text-align: center;
    }

    header {
      background-color: #0d6efd;
      color: white;
      padding: 30px 0;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    h1 {
      font-size: 2.5em;
      margin: 0;
    }

    main {
      padding: 40px 20px;
      max-width: 1000px;
      margin: auto;
    }

    section {
      margin-bottom: 50px;
    }

    h2 {
      color: #0d6efd;
      border-bottom: 2px solid #0d6efd;
      display: inline-block;
      padding-bottom: 5px;
      margin-bottom: 20px;
    }

    .project-card {
      background-color: white;
      border-radius: 15px;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
      padding: 25px;
      margin: 20px auto;
      text-align: right;
      max-width: 800px;
    }

    .project-card h3 {
      margin-top: 0;
      color: #222;
    }

    .project-card p {
      line-height: 1.6;
    }

    .project-card a {
      display: inline-block;
      margin-top: 15px;
      padding: 10px 20px;
      background-color: #0d6efd;
      color: white;
      text-decoration: none;
      border-radius: 8px;
      transition: background-color 0.3s ease;
    }

    .project-card a:hover {
      background-color: #0b5ed7;
    }

    pre {
      text-align: left;
      background-color: #e3e7f1;
      padding: 15px;
      border-radius: 10px;
      overflow-x: auto;
      max-height: 300px;
      direction: ltr;
    }
  </style>
</head>

<body>
  <header>
    <h1>הפרויקטים שלי</h1>
  </header>

  <main>

    <!-- פרויקט אוטומציה -->
    <section>
      <h2>פרויקט אוטומציה</h2>
      <div class="project-card">
        <h3>סקריפט בדיקות אוטומציה (Python + Selenium)</h3>
        <p>
          זהו סקריפט אוטומציה שבודק תהליך התחברות לאתר חנות חיות (JPetStore). 
          הבדיקה כוללת הכנסת שם משתמש שגוי, סיסמה תקינה, לחיצה על כפתור LOGIN ובדיקת הודעת השגיאה הצפויה.
        </p>
        <a href="MyScriptProject.py" download>הורד את הסקריפט</a>

        <h4>קטע קוד לדוגמה:</h4>
        <pre>
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
        </pre>
      </div>
    </section>

    <!-- פרויקטים של STR -->
    <section>
      <h2>פרויקטים של STR</h2>
      <div class="project-card">
        <h3>דו"ח תוצאות בדיקות (STR)</h3>
        <p>
          מסמך STR מסכם את תוצאות הבדיקות שבוצעו בפרויקט, כולל סטטוס כל בדיקה (עבר/נכשל), 
          בעיות שהתגלו במהלך הרצת התסריטים, והמלצות לשיפורים.
        </p>
      <a href="https://docs.google.com/document/d/1ZHkW4pmOGvSDEkcUjwAW_d1bCNb04D7-/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true" target="_blank">
  צפה במסמך STR
</a>

<a href="https://docs.google.com/document/d/1syDS0rET1S3G7hf44xITtaut-oxyeAo3/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true" target="_blank">
  צפה במסמך STR3
</a>

      </div>
    </section>

    <!-- פרויקטים של STP -->
    <section>
      <h2>פרויקטים של STP</h2>
      <div class="project-card">
        <h3>מסמך תוכנית בדיקות (STP)</h3>
        <p>
          מסמך STP מפרט את אסטרטגיית הבדיקות, היקף הבדיקות, סביבת העבודה, 
          כלי הבדיקה והשיטות בהן השתמשתי במהלך הפרויקט.
        </p>
     <a href="https://docs.google.com/document/d/1JtMgr5dU9URAdJ7VXqxckaiarcgpRlpQ/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true" target="_blank">צפה במסמך STP</a>

<a href="https://docs.google.com/document/d/14S3nZwK5bVuJcRWk5nR6qEZ41IQAXV7F/edit?usp=drive_link&ouid=102490978916154441779&rtpof=true&sd=true" target="_blank">צפה במסמך STP3</a>

      </div>
    </section>

  </main>
</body>
</html>
S
