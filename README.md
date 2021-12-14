# ESCO Music 
#### Video Demo: https://youtu.be/S3CJxMik88U
#### Description: 
    ESCO music is an informational application for music lovers and musicians created with Django.  The site allows users to register to create their own accounts and subsequently, to log in and out of those accounts. Once a user has created an account, they can then create profiles for bands at their will and add them into the database (SQLite).  A user also has the ability to update or edit band profiles (only the ones they have created, while logged in). Users who want to learn more about a specific band can click the profile name to see details about the band.  This can aid in helping music lovers to find new bands to listen to as well as to create exposure for smaller, local bands.  

    After first creating the django project and virtual env in the terminal, I then created the band_profiles app.  This app has the data models (models.py) which allows management of all the profiles in the database.  In (admin.py) I registered the app with the django admin (a prebuilt feature in Django).  Superusers can access the admin page and edit User accounts and also band profiles as deemed necessary (this page is found at "http://127.0.0.1:8000/admin" when running the dev env). Regular users cannot access this page for security purposes. I then created (forms.py, urls.py and views.py) to deal with the apps form input, url routes, and django views (page views), respectively. 
    
    Inside the band_profiles app you will also find the (templates) folder which holds all the html pages used in the app. The foundation (base.html) contains all <head> info, where I uploaded Bootstrap4 and also some static files.  In the <body> I inserted the Bootstrap navbar with collapsible burger menu and the footer. Inside the <main> section I inlcuded the Django templates to insert the different page views. All subsequent templates build off of this base (the navbar and footer are in every page). In (edit_profile.html) I added the code to deal with the edit profile view and form.  Inside (index.html) I inserted the code for a basic landing page which welcomes a new explorer. In (new_profile.html) I allowed for a user to create a new band profile (only after registering and logging in). In (profile.html) I created the dynamic page which displays a specific band's profile after a user clicks the name from the Band Profiles collection. In (profiles.html) I created the dynamic grid which displays all the bands included in the database in alphabetical order. 

    Moving on the EsCoMusic folder (the generic project folder), I adjusted (settings.py) so that my app would work and also include the abilty to use static files and images rendered with the pillow library. In (urls.py) I added the ability for the project to route pages from the users app (covered shortly), the band profiles app, and the admin.

    The users app is also another app I created in the terminal which is included in the django language and allows for simple set-up of user accounts functionality. I adjusted the (urls.py and views.py) here so that my URL routes and page views would work in the project.  

    Esco_env is the folder which contains the info for the virtual environment that I designed the project in. This is automatically created by Django and holds all the library info and venv scripts. 

    The media folder has been set-up to hold static images which have been uploaded into new band profiles. All band pictures reside here after they are formatted by Pillow and added to the database.
    
    The static folder holds the music icon which I chose to use in my document tab. It also contains a static css files (style.css) which contains some styling for the footer and navbar. It also includes (clock.js) which is a javascript program i created to display a live clock in the footer page. This clock formats the time and then displays it.  The script is run every second so it tracks the time just like any opter digital clock would. 

    The (db.sqlite3) is my database file built on SQLITE3. This comes standard in django projects and holds all the info for our profiles and users.

    The (manage.py) file carries out basic tasks from the terminal including launching the development server.  This can be achieved by first activating the virtual env (esco_env\scripts\activate) and then running (python manage.py runserver).  

    Lastly, are the readme file which you are currently reading and then the (requirements.txt) file which includes all the package libraries I used in the project. 