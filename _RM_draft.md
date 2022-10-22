# Song Mates

[Link to deployed site](https://songmates.herokuapp.com/)

## Purpose

Thanks to modern technology, musicians can make great quality recordings at home. There's never been a better time for musicians to be able to express themselves via the 
medium of digital recording. Great music is often the result of collaboration, and while audio technology enables musicians to work with each other remotely, how do you find people to collaborate with?
 
The purpose of Song Mates is to provide a platform for musicians who want to write, perform and record material to find like minded people to collaborate with, whether that be for a song or an album.

Users can register with Song Mates, and create a profile with an image, a biography or summary of what they're looking for, and can specify the instruments they play and relevant skills. They can search for potential collaborators using these criteria, and make collaboration requests (like a connection request on LinkedIn or friend request on Facebook). Users can send direct messages to their  connections.

**Important**

Song mates is a work in progress. The backend is in place and key features for a minimum viable product have been implemented, however no real styling or design has yet been applied. At least one additional feature (user to user messaging) will be implemented for the final version, to be completed by mid-November 2022.

## Table of contents

## User stories

## Agile development methodology

## Features

### Future features

- There is currently a lot of HTML duplicated between the `find_collabs.html` and `single_profile.html` templates. These could be refactored into a single template, but this would require passing in additional data and adding conditional statements to the template to determine whether it should render as a single profile or multiple profiles (e.g. this would influence whether or not to render search features, the correct heading for the page etc).

## Planning

## Frameworks, libraries and dependencies

### Django 3.2

### Psychopg 2
Python PostgreSQL adapater

### Gunicorn
Python WSGI HTTP server

### dj-database-url
Django utility to create an environment variable to configure the Django application

### Django-allauth
User account management django application suite

### Cloudinary and django-cloudinary-storage
Libraries to enable storage of static files and media in Cloudinary

### Crispy Forms
Django app to simplify form rendering

### Crispy Bootstrap 5
Bootstrap 5 templates for Crispy Forms

### Bootstrap 5
Front end CSS and JavaScript library

## Data model

## Testing

### Fixed bugs
- Testing of the update profile form showed that profile pictures were not uploading to cloudinary. This was rectifed by adding the `enctype="multipart/form-data"` attribute to the form element.
- While testing the search feature, it was realised that if the user did not select any genres, no profiles would be returned. This was fixed by adding a simple conditional statement to ensure that profiles are not filtered by genre if no genres are selected.
- During testing, it was found that the 'Show my collaborators only' checkbox on the search form was overriding other search results. For example, if a genre of 'Hip-Hop' was selected in the genres menu and the checkbox to show collaborators only was selected, collaborators would show in the search results even if none of them were matched with the 'Hip-Hop' selection. The correct outcome in this case would be no search results. This was bug was caused by an incorrect boolean condition in an if statement and easily fixed.

### Manual testing

### Automated tests

### Validator testing

##  Bugs

Initially, allauth configuration was set to require the user to login with an email address and for email verification to be required. However, this caused a Django 'connection refused' error. This was caused by the fact no email server was availabe to send verification request emails. Settings were changed so that account login is by username rather than email address. 

### Resolved bugs

### Unresolved bugs

## Deployment

## Credits

### Code

- The steps to connect to a Heroku Postgres database and deploy were adapted from the Code Institute 'I think therefore I blog' tutorial. This includes defining `DATABASE_URL` and `SECRET_KEY` environment variables in an `env.py` file in the local environment and adding corresponding config variables in the Heroku dashboard, using dj_database_url to create a URL from the Heroku database URL in `settings.py`, updating `ALLOWED_HOSTS` in `settings.py` with the deployed Heroku URL and adding the templates path to a `TEMPLATES_DIR` variable in `settings.py`.
- This [stackoverflow article](https://stackoverflow.com/questions/68810221/login-required-decorator-gives-object-has-no-attribute-user-error) was referenced to understand how to use the 'login-required' decorator with a class based view
- The approach to deleting a user account (actually making the account inactive) in response to a button was adapted from [this stackoverflow article](https://stackoverflow.com/questions/38047408/how-to-allow-user-to-delete-account-in-django-allauth)
- The Bootstrap 5 documentation was extensively referenced for guidance on implementing navbars and modal dialogs.
- The approach to using a crispy form Div helper class to layout form elements next to each other was based on [this stackoverflow article](https://stackoverflow.com/questions/23021746/get-two-fields-inline-in-django-crispy-forms-but-not-others-horizontal)
- The approach to using the crispy forms HTML help class to display an image from the database model in a form was based on (https://stackoverflow.com/questions/21076248/imagefield-preview-in-crispy-forms-layout)
- The approach to using a custom template tag to pass data to the base HTML template was adapated from (https://stackoverflow.com/questions/21062560/django-variable-in-base-html) and then refined with reference to the official Django documentation.
- This [stack overflow question](https://stackoverflow.com/questions/53672002/how-to-call-conditional-statements-on-template-tags-with-no-arguments-django) was referenced for details on how to convert a custom template tag to a variable in Django template.
- The technique for displaying values of a many to many field in the admin panel was adapted from [stack overflow question](https://stackoverflow.com/questions/18108521/many-to-many-in-list-display-django)
- This [stack overflow question](https://stackoverflow.com/questions/21666963/django-forms-multiplechoicefield-only-selects-one-value) was referenced to discover how to access a list of values returned by a multiple choice Django form element.
- The technique of using an `initial` argument when initialising a form to set a form input's initial value is from (https://stackoverflow.com/questions/604266/django-set-default-form-values)
- Using the `_in` lookup parameter to find out if the value of a field exists within a list was adapated from (https://stackoverflow.com/questions/70703168/check-if-each-value-within-list-is-present-in-the-given-django-model-table-in-a)
- The syntax for searching on a property of a foreign key object is adapated from (https://stackoverflow.com/questions/35012942/related-field-got-invalid-lookup-icontains)
- The technique for overriding the save method of a Django model class in order to compute the value of a field based on the values of other fields is adapted from(https://stackoverflow.com/questions/22157437/model-field-based-on-other-fields)

### Content

- Font Awesome icons
    - [Burger menu icon](https://fontawesome.com/icons/bars?s=solid&f=classic)
    - ['Collaborator' icon](https://fontawesome.com/icons/user?s=solid&f=classic
- Placeholder profile image by WandererCreative and downloaded from [Pixabay](https://pixabay.com/images/id-973460/)