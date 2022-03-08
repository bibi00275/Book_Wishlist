# Book_Wishlist

**Dependencies**

Python - Programming Language
Flask - The framework used
SQLAlchemy - ORM
Pip - Dependency Management

**Install all project dependencies using:**

pip install -r requirements.txt

**Running**

FLASKAPP=main.py flask run

Adding a New WishList
<img width="1440" alt="Screen Shot 2022-03-07 at 6 18 31 PM" src="https://user-images.githubusercontent.com/22124043/157146629-98b67e39-ccde-4590-adff-85596d4b310c.png">

Updating a WishList
<img width="1440" alt="Screen Shot 2022-03-07 at 6 20 57 PM" src="https://user-images.githubusercontent.com/22124043/157146845-6e61adbd-b3b0-4c9b-b765-90f22e1d4ffb.png">

Deleting a WishList
<img width="1440" alt="Screen Shot 2022-03-07 at 6 22 33 PM" src="https://user-images.githubusercontent.com/22124043/157146995-c30954e6-2568-486e-a138-3b096a725e7f.png">

**Improvments **

I have just created a very basic boiler plate code which would just test out the wishlist functionality, Currently there is no proper directory strucutre, At a high level project structure can have a app folder under which we can have Models folder(Python classes modeling the database), repositories( Python classes allowing you to interact with your models) resources (Python classes containing the HTTP verbs of your routes) routes (Routes definitions and links to their associated resources), util (Some helpfull, non-business Python functions for your project)
we can also have config.py (Project configuration settings) ,manage.py (Project commands) ,server.py for Server configuration 
test folder holding unit test
