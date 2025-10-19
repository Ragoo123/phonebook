import os
from flask import Flask, render_template
from dotenv import load_dotenv
from extensions import db, login_manager, bcrypt, csrf, htmx, bootstrap
from sqlalchemy import text,select
from models import Contact
from forms import ContactForm



# Load environment variables
load_dotenv()

# --------------------------
# Initialize Flask apps
# --------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# --------------------------
# Initialize extensions
# --------------------------
db.init_app(app)
#login_manager.init_app(app)
#login_manager.login_view = 'login'
bcrypt.init_app(app)
csrf.init_app(app)
htmx.init_app(app)
bootstrap.init_app(app)  



# --------------------------
# Routes
# --------------------------
@app.route('/')
def index():
    all_contacts = Contact.query.all()
    contact_form = ContactForm()

    return render_template('index.html', all_contacts=all_contacts, contact_form=contact_form)  

@app.route('/add_contact', methods=['POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        print("Form validated successfully.")
        new_contact = Contact(
            name=form.name.data,
            phone_number=form.phone_number.data
        )
        db.session.add(new_contact)
        db.session.commit()
    return render_template('partials/_contact_card.html', contact=new_contact)


# --------------------------
# Run the app
# --------------------------
if __name__ == '__main__':
    app.run(debug=True)
