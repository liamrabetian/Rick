from datetime import datetime
@app.route('/')
def index():
 return render_template('index.html',
 current_time=datetime.utcnow())

