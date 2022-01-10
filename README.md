# five_crowns

### An app to keep stats on winners of Five Crowns with friends 
Add players; add games; add scores for games.
For each player, see number of games played, min, max and average score.

#### Virtual Environment
Create and activate a virtual environment. Use Python3 as the interpreter. Suggest locating the venv/ directory outside of the code directory

Mac Version:
python3 -m venv env
source env/bin/activate

Windows Version:
python -m venv env
env\Scripts\activate

#### Install required modules
pip install -r requirements.txt (pip3 for Mac)
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#### View Site
Local site available at http://127.0.0.1:8000

#### Create superuser
python manage.py createsuperuser
enter username and password
Uuse these to log into admin console at
https://127.0.0.1:8000/admin


#### Screenshots
![Screen Shot 2022-01-10 at 12 03 29 PM](https://user-images.githubusercontent.com/54478043/148824807-ee8dcc8f-feb0-4266-bb8a-5b9f76ed07ba.png)
![Screen Shot 2022-01-10 at 1 04 57 PM](https://user-images.githubusercontent.com/54478043/148824826-75f728f0-740f-4ace-980b-94b8c948e2d8.png)
