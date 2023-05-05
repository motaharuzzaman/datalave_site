from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/services/')
def services():
    return render_template("services.html")

@app.route('/pricing/')
def pricing():
    return render_template("pricing.html")

@app.route('/faq/')
def faq():
    return render_template("faq.html")

@app.route('/case_studies/')
def case_studies():
    return render_template("case_studies.html")

if __name__=='__main__':
    app.run(debug=True)
    
