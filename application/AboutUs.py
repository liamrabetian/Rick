from application import app

@app.route('/About')
def About():
    return "About Us"