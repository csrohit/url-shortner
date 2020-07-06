# url-shortner

pip3 install pipenv

pipenv install // install pipenv in the current directory

pipenv shell // to enter virtual environment
exit // to exit from the virtual environment

pipenv install flask	// install pipenv in the virtual environment

export FLASK_APP=hello	// name of the flask app in the virtual environment
flask run	// start the flask app

export FLASK_ENV = development	// change default environment from production to development

default app name is app.py but we have to specify the environment everytime we launch a virtual environment
