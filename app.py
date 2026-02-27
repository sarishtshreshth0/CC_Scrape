from flask import Flask, render_template, request, Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.chrome.service import Service
import os



import time

app = Flask(__name__)

def scrape_live(problem_name):

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    driver = webdriver.Edge(options=options)
    email = os.environ.get("saristhshreshth12@gmail.com")
    password = os.environ.get("for_scrape_S@1")
    # 🔥 Stylish Header
    yield """
    <html>
    <head>
        <title>Live Scraping</title>
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono&family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                font-family: 'Poppins', sans-serif;
                padding: 40px;
            }
            h1 {
                text-align: center;
                margin-bottom: 30px;
            }
            .log {
                background: rgba(255,255,255,0.08);
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            .code-block {
                background: #111;
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 25px;
                overflow-x: auto;
                font-family: 'JetBrains Mono', monospace;
                font-size: 14px;
                border-left: 5px solid #00c6ff;
            }
            hr {
                border: none;
                height: 1px;
                background: rgba(255,255,255,0.2);
                margin: 25px 0;
            }
        </style>
    </head>
    <body>
    <h1>🚀 Live CodeChef Scraping</h1>
    """

    yield '<div class="log">Opening CodeChef...</div>'

    driver.get("https://www.codechef.com")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[text()='Login']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@placeholder='Username or Email']").send_keys(email)
    driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[2]").send_keys(password)
    driver.find_element(By.XPATH, "(//input[@type='submit'])[2]").click()

    yield '<div class="log">Login Done ✅</div>'
    time.sleep(6)

    driver.get(f"https://www.codechef.com/status/{problem_name}?language=PYPY3&status=Correct")
    yield f'<div class="log">Opened Status Page for {problem_name}</div>'
    time.sleep(5)

    links = driver.find_elements(By.XPATH, "//span[@aria-label='View submission']")

    for i in range(len(links)):

        links = driver.find_elements(By.XPATH, "//span[@aria-label='View submission']")
        links[i].click()
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)

        try:
            code = driver.find_element(By.CLASS_NAME, "ace_content").text
        except:
            code = "Code not found"

        yield f"""
        <hr>
        <h3>Submission {i+1}</h3>
        <div class="code-block">
        <pre>{code}</pre>
        </div>
        """

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

    driver.quit()
    yield "<h2>Scraping Finished 🎉</h2></body></html>"

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/scrape", methods=["POST"])
def scrape():
    problem_name = request.form["problem"]
    return Response(scrape_live(problem_name), mimetype='text/html')


if __name__ == "__main__":
    app.run(debug=True)
