# mail_api
simple mail sending api using Django socket programming!

0. install packages
`apt install python git` 

1. clone this repo
`git clone https://github.com/bahman-ahmadi/mail_api.git`

2. go to directory
`cd mail_api`

3. activate virtual environment
`source venv/bin/activate`
(this is for unix)

4. run the project 
`python manage.py runserver`

5. open your browser and write :
`http://127.0.0.1:8000/?my_mail=bahmanahmadi.mail@gmail.com&my_pass=12345678&to_mail=bit.tm.mail@gmail.com&subject_mail=SUBJECT&text_mail=hello`
