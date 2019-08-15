# EM Tennis

Final project Openclassrooms, EM Tennis full stack website, with Paypal

Link project: https://github.com/Seiph59/EM_Tennis_P13
URL address: https://pur-beurre001.herokuapp.com/

# What is this project ?

This project has for objective to create a portal for all associations wishing to better manage
the organisation of an event

# How ?
For this project, we use Python 3 , Django, Paypal

# Libraries Used and Python Version:

* Python 3.6.5
* Django 2.2.3
* django-crispy-forms 1.7.2
* django-paypal 1.0.0
* Pillow 6.1.0
More informations on requirements.txt

# To start

1. Create your virtual environment and install 'requirements.txt'

2. For Paypal settings, you need to change the parameters in settings.py
    * PAYPAL_RECEIVER_EMAIL
    * PAYPAL_TEST = True

3. Before launch make sure to create a superuser with this command 'python manage.py createsuperuser'

4. Execute the following command 'python manage.py migrate'

5. The app is ready to start ('python manage.py runserver' in local)

# In case of bug

You can send me an Email at this address : chimere_62@hotmail.fr and tell what bug do you encounter



