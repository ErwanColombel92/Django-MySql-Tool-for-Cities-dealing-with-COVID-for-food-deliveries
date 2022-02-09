# Django-MySql-Tool-for-Cities-dealing-with-COVID-for-food-deliveries
This project aims to create a web platform that cities could use to organize food deliveries in a COVID or a crisis context. Is uses MySql and Django (Python).

The management of applicants is divided into several parts. There is the management of user accounts, the management of user profiles and the management of orders. These different points will be discussed in the three following parts.

For the basis of the management of user accounts, we used the default User class of Django. This class allows to manage the users of the application by defining if they can be admin or not thanks to a simple boolean. By default, when a user registers, he enters his name, first name, username, password and email address. This information is directly saved in the DB in the auth_user table.

The management of the user account alone is not enough, to be able to add other interesting data, we have created a Profile model, allowing to associate (thanks to an inheritance) the following data to the user account
- address
- city
- department (we only managed the ile de France and the districts of Paris)
- optional profile picture
- 1 dietary restriction to choose from: Gluten free, Meat free, Dried fruit free, Lactose free or No restrictions

![profil](https://user-images.githubusercontent.com/59508102/153101784-b9ed4d42-8137-4463-916b-938f11605ce9.jpg)

In order to avoid multiple orders from the same household, we have also added a household management. Each person can have an account on the site, but only the Head of Household (managed by a boolean in the DB) will have access to the ordering interface. By default, when a user registers and enters an address, a new household is automatically created in the DB (household table) if he is the first member of his family to register. By default, he will be the only head of the family. If a second member registers, by entering his address, Django queries the database and automatically places him in the corresponding household (same address and same city). To change the Head of Household status, the user must contact the site managers (us!).

![foyers](https://user-images.githubusercontent.com/59508102/153101780-e4374ff4-adfa-4648-b5f3-7141c139ce2d.jpg)

The ordering interface starts with a filter choice in order to select which items we want to order. The items displayed take into account the dietary restrictions chosen in the profile page.


![panier](https://user-images.githubusercontent.com/59508102/153101781-0e5e77a5-91ea-4a90-b6b2-067c559ffee2.jpg)

This section of the community interface is only visible on the screen if you are logged in as super user (admin mode user). This is to avoid that a normal user of the site can arrive on this page. The access button to this page is not the only one to be hidden: even if a user tried to access this page without being an administrator, he would be redirected to the login interface. This was made possible by using a lambda expression that takes a logged-in user as input and checks if he is a superuser.

![maps](https://user-images.githubusercontent.com/59508102/153101783-d37a3a63-93f0-4012-a71b-e20af8cb5a1c.jpg)

