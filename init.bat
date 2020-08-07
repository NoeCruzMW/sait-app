set FLASK_APP=app/app
set FLASK_ENV=development
echo flask db init
flask db migrate -m "Added company table."
echo flask run