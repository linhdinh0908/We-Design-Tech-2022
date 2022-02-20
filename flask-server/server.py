from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

app = Flask(__name__)

# API route


@app.route("/")
def show_job():
    # Create job description dataframe using pandas
    df = pd.DataFrame({'job name': [], 'responsibilities': [], 'requirements': [
    ], 'willingness to accessibilty': [], 'company_rating': []})

    # Create soup object and parse text html
    url = "https://ca.indeed.com/Ontario-Pension-Plan-jobs?vjk=b56ea92310c792e1"
    r = requests.get(url)
    soup = bs(r.text, 'html.parser')
    result = soup.find('div', class_="")
    return


if __name__ == "__main__":
    app.run(debug=True)
