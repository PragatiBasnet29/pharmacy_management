to launch the app
step1: go to terminal and go to required directory and clone by following command
git clone https://github.com/prathamadh/DBMS__Project.git

step2: create virtual environment by :
python -m venv venv

step3:in terminal(use tab to autocomplete)
venv/Scripts/activate

step4:
pip install django

step 5: go to folder that contains manage.py
may required to do two commands (make migrations and migrate)
python manage.py makemigrations
python manage.py migrate

step 6:
python manage.py runserver


the application will run in browser or copy the link and paste in browser.
