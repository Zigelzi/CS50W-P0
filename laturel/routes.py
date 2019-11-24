from flask import render_template, jsonify, make_response, request
from flask_mail import Message
from datetime import datetime
import sys

from laturel import app, mail
from laturel.forms import CostForm, CarSelectorForm, ContactForm
from laturel.models import model_dict, co2_dict


@app.route('/')
def index():
    return render_template('index.html', active='index')

@app.route('/cars', methods=['GET', 'POST'])
def cars():
    form = CostForm()
    car_form = CarSelectorForm()

    return render_template('cars.html',
                           form=form,
                           car_form=car_form,
                           active='cars'
                           )

@app.route('/db/data', methods=['GET', 'POST'])
def data():
    #  Take the JSON request and convert it to dict
    req = request.get_json()

    #  Set the id values to compare and switch to correct type for DB input in model_dict
    ev = 'ecar_model'
    gasoline = 'gcar_model'
    diesel = 'dcar_model'

    #  Replace the id value for type value to be able to do DB query correctly
    if req['type'] == ev:
        req['type'] = 'ev'
    if req['type'] == gasoline:
        req['type'] = 'gasoline'
    if req['type'] == diesel:
        req['type'] = 'diesel'

    #  Query DB for car values and make dict of values
    model = model_dict(req['type'], req['model'])
    co2 = co2_dict(model['co2'])

    #  Create JSON response from dict and respond it to application
    res = make_response(jsonify(car_info=model, co2=co2), 200)
    return res


@app.route('/', methods=['GET', 'POST'], subdomain='web')
def web_index():
    form = ContactForm()
    if request.method == 'POST':
        recepient = 'miika.a.savela@gmail.com' # Recepient where the contact form is sent to.
        reply_recepient = form.email.data # Where the confirmation email is sent
        # Parse the form element submitted by user and send the email.
        contact_msg = Message(subject='[Web] Uusi yhteydenottopyyntö',
                      recipients=[recepient],
                      sender=app.config['MAIL_DEFAULT_SENDER'])
        print(f'contact_msg sender: {contact_msg.sender}', file=sys.stdout)
        contact_msg.body = f"""Uusi yhteydenottopyyntö
                              Nimi: {form.name.data}
                              Sähköposti: {form.email.data}
                              Puhelinnumero: {form.phone.data}
                              Toivottu yhteydenottotapa: {form.preferred_contact.data}
                              Lisätietoja: {form.description.data}
                           """
        contact_msg.html = f"""<h1>Uusi yhteydenottopyyntö</h1>
                      <p><strong>Nimi</strong></p>
                      <p>{form.name.data}</p>
                      <p><strong>Sähköposti</strong></p>
                      <p>{form.email.data}</p>
                      <p><strong>Puhelinnumero</strong></p>
                      <p>{form.phone.data}</p>
                      <p><strong>Toivottu yhteydenottotapa</strong></p>
                      <p>{form.preferred_contact.data}</p>
                      <p><strong>Lisätietoja</strong></p>
                      <p>{form.description.data}</p>"""

        reply_msg = Message(subject='[Laturel] Yhteydenottopyyntö',
                            recipients=[reply_recepient])
        reply_msg.body = f"""Kiitos yhteydenotostasi!
                             
                             Olemme vastaanottaneet yhteydenottopyyntösi ja vastaamme sinulle viikon sisällä.

                             Syötit seuraavat tiedot:
                             Nimi
                             {form.name.data}
                             Sähköposti
                             {form.email.data}
                             Puhelinnumero
                             {form.phone.data}
                             Toivottu yhteydenottotapa
                             {form.preferred_contact.data}
                             Lisätietoja 
                             {form.description.data}

                             Ystävällisin terveisin
                             Laturel tiimi
                          """
        reply_msg.html = f"""<h1>Kiitos yhteydenotostasi!</h1>
                             <p>Olemme vastaanottaneet yhteydenottopyyntösi ja vastaamme sinulle viikon sisällä.</p>
                             <p>Syötit seuraavat tiedot:</p>
                             <p><strong>Nimi</strong></p>
                             <p>{ form.name.data }</p>
                             <p><strong>Sähköposti</strong></p>
                             <p>{ form.email.data }</p>
                             <p><strong>Puhelinnumero</strong></p>
                             <p>{ form.phone.data }</p>
                             <p><strong>Toivottu yhteydenottotapa</strong></p>
                             <p>{ form.preferred_contact.data }</p>
                             <p><strong>Lisätietoja</strong></p>
                             <p>{ form.description.data }</p>
                          """
        mail.send(contact_msg)
        mail.send(reply_msg)
    return render_template('web/web_index.html', form=form)

@app.route('/e/contact_card', subdomain='web')
def web_contact_card():
    return render_template('web/example_contactcard.html')

@app.route('/e/small_page', subdomain='web')
def web_small_page():
    return render_template('web/example_small_page.html')

@app.route('/e/medium_page', subdomain='web')
def web_medium_page():
    return render_template('web/example_medium_page.html')

@app.route('/', subdomain='vantasia')
def vantasia_index():
    form = ContactForm()
    return render_template('vantasia/vantasia_index.html', form=form)