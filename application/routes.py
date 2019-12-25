from flask import render_template
from application import app
from application.models import User,Post

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', title='Home', Users=users)