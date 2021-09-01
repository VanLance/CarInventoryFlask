from flask import Blueprint, render_template, request, redirect, url_for, flash
from carInventory.forms import UserLoginForm
from carInventory.models import User,db
auth = Blueprint('auth',__name__, template_folder='auth_templates')



@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    form =  UserLoginForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            print(email,password)

            user=User(email, password = password)
            
            db.session.add(user)
            db.session.commit()
            
            flash(f'You have successfuly created a user account {email}', 'User_created')
            return redirect(url_for('site.home'))

    except:
        raise Exception('Invalid Form Data: Please Check Your Form')
    
    return render_template('signup.html', form=form)

@auth.route('/signin', methods = ["GET", "POST"])
def signin():
    form = UserLoginForm()
    return render_template('signin.html')

@auth.route('/logout', methods = ["GET", "POST"])
def logout():
    return render_template('logout.html')