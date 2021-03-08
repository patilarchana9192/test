# test

Run project-
python manage.py runserver

Make Migrations-
python manage.py makemigrations <app_name>

Migrate after make migrations-
python manage.py migrate <app_name>

for signup api -
request_url= http://127.0.0.1:8000/user/signup
request_body={"password":"archana123","username":"archana",
                      "firstname":"archana","lastname":"patil",
                      "email":"archanapatil@gmail.com",
                      "company":"xyz","address":"pune",
                      "dob":"1991-20-09"}

for login api -
request_url= http://127.0.0.1:8000/user/login
requset_bady={"userneme":"archana",
                         "password":"archana123"}

for payment api -
request_url= http://127.0.0.1:8000/user/subscription
request_body={"sub_id":1,"user_id":1,
                      "card_number":"1234567890987654",
                      "cvv":"350","expiry_date":"2025-12-10",
                      "acc_id":1}
request_header={"Authorization":"Bearer token"}



