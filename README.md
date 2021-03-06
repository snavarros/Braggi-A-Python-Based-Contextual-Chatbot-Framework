<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->

<!-- display the social media buttons in your README -->

[![alt text][1.1]][1]
[![alt text][2.1]][2]
[![alt text][3.1]][3]
[![alt text][6.1]][6]


<!-- links to social media icons -->
<!-- no need to change these -->

<!-- icons with padding -->

[1.1]: http://i.imgur.com/tXSoThF.png (twitter icon with padding)
[2.1]: http://i.imgur.com/P3YfQoD.png (facebook icon with padding)
[3.1]: http://i.imgur.com/yCsTjba.png (google plus icon with padding)
[6.1]: http://i.imgur.com/0o48UoR.png (github icon with padding)

<!-- icons without padding -->

[1.2]: http://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[2.2]: http://i.imgur.com/fep1WsG.png (facebook icon without padding)
[3.2]: http://i.imgur.com/VlgBKQ9.png (google plus icon without padding)
[6.2]: http://i.imgur.com/9I6NRUm.png (github icon without padding)


<!-- links to your social media accounts -->
<!-- update these accordingly -->

[1]: https://twitter.com/Sushrit_Lawliet
[2]: https://www.facebook.com/SushritLawliet/
[3]: https://sushritpasupuleti.blogspot.com
[6]: https://github.com/SushritPasupuleti

<!-- Please don't remove this: Grab your social icons from https://github.com/carlsednaoui/gitsocial -->
# Braggi: A Python Based Contextual Chatbot Framework
Braggi is a Python based Contextual Chatbot Framework, which hopes to integrate all the necessities for a great chatbot framework, to satisfy both enterprise and general audiences alike. Development still underway, more features on the way 😄

<img src="https://3.bp.blogspot.com/-v0h0i-rlvx4/WzszGk4g65I/AAAAAAAAXbg/9sG89XtNigIolOgUGVFxKsPzRUU5P-qvQCLcBGAs/s1600/Cover2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />
     
> Check the Development Branch for Features under development.

# Features
* A DNN based classifier that classifies the intent.
* JSON based scripting to help create conversation patterns and responses.
* A fully scalable model, capable of handling larger models.
* A Django Rest Framework based API.

# Features Planned
- [ ] A parser to extract information from messages (Prices, Dates, Messages, Names).
- [x] restful implimentation in Django.
- [x] ReactJS front-end with built in WebViews.
- [x] Admin dashboard for analytics.
- [ ] Stand alone editor to prepare scripts and customize the bot.
- [ ] GAN based replies 🤔?
- [ ] And lots more...

# Setup
Install the following modules if you don't have them already
#### Python(3.6)
```shell
pip install tensorflow
pip install tflearn
pip install nltk
pip install django-rest-framework
pip install httpie
```
#### node.js
[Download node.js](https://nodejs.org/en/download/)
```shell
npm install react
npm install express
npm install axios
npm install bootstrap
```

# Running the Code
Execute Run.py
```shell
python Run.py
```

For Django Rest Framework based Implimentation
```shell
cd \braggi-rest-api\braggi_rest_api
python manage.py runserver
http http://127.0.0.1:8000/braggi/
```

For the Frontend
```shell
cd \braggi-reactjs-frontend
npm start

cd \backend
node app.js
```

> Open http://127.0.0.1:8000/braggi/ to view the data.
> Open http://127.0.0.1:3000 to view the chat UI
> Open http://127.0.0.1:8000/api-admin/login to login and head into the dashboard for all the Admin glory.

To create a superuser account, follow:
```shell
python manage.py create superuser
Username: Braggi-Admin
Email address:
Password:
Password (again):
Superuser created successfully.
```

# Feedback / FAQs / Contact
Drop me a message anywhere on the links down below 😄

* [Twitter](https://twitter.com/Sushrit_Lawliet)
* [Facebook](https://www.facebook.com/SushritLawliet/)
* [My Blog](https://sushritpasupuleti.blogspot.com)
* [Twitter](https://github.com/SushritPasupuleti)
* My email : [sushrit.pk21@gmail.com](mailto:sushrit.pk21@gmail.com)

# Screenshots
Work in Progress

Chat UI             |  Admin Dashboard Home          |  Dashboard Tools
:-------------------------:|:-------------------------:|:-------------------:
![](https://3.bp.blogspot.com/-oKngW_SwUfI/W5VEE3oUISI/AAAAAAAAX4w/S8XkmAEWjcc4gEweQBDmNBdtsiCW8bDbQCLcBGAs/s1600/Screenshot%2Bfrom%2B2018-09-09%2B21-29-26.png)  |  ![](https://4.bp.blogspot.com/-H_s0XaE29fM/W5VFxP7KELI/AAAAAAAAX5E/1s47ftGI5c89F5BgU11MvoS2KgIYtiHOgCLcBGAs/s1600/Screenshot%2Bfrom%2B2018-09-09%2B21-26-42.png)  | ![](https://2.bp.blogspot.com/-ZXFtczTds6Y/W5VFxG63AvI/AAAAAAAAX5A/dZpSaqlf40AbSQIMsaXzjRvVCmc3oTBJQCLcBGAs/s1600/Screenshot%2Bfrom%2B2018-09-09%2B21-27-12.png)
