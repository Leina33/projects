# Awards 

A awards is webiste where users can signing and post there projects, other users can review them and like the project.

## Built By [DOMINIC RUTTO](https://github.com/Leina33/)

The awards   website where you can post and share your projects and other users can views and on them. You can view the site at:https://awardsapp1.herokuapp.com/

## Description

## User Stories

These are the behaviours/features that the application implements for use by a user.
As a user I would like to:

- See the project i posted
- upload my profile picture
- like

## Specifications

| Behaviour                            |            Input             |                                                               Output |
| :----------------------------------- | :--------------------------: | -------------------------------------------------------------------: |
| Display project                      |       **On page load**       |             List of various project sources is displayed per category |
| Display categories                   |      **Click on image**      |           Redirected to a page with a list of images from the source |
| Display profile                      |       **On page load**       |              Each profile should have the like and the API used      |
| Read an entire desc                  | **check category sub-title** | Redirected to the picked category source's site to read entire proje |
| view project                         |        **Click view**        |                                 load the project url  area           |

## SetUp / Installation Requirements

### Prerequisites

- python3.6
- pip
- virtualenv
- psql database
- API

### Cloning

- In your terminal:
  \$ git clone https://github.com/Leina33/projects.git

## Running the Application

- Creating the virtual environment
  $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
- Installing Django and other Modules
  $ python3.6 -m pip install djang0==1.11
        $ python3.6 -m pip install Flask-Bootstrap4
  $ python makemigration photos
        $ python manage.py migrate
  $ pip install psycopg2
        $ pip install pyuploadcare
  #check on requirements.txt file
- To run the application, in your terminal:
  \$ python3.6 manage.py runserver

## Testing the Application

- To run the tests for the class files:
  $ cd app
        $ python3.6 test.py

## Technologies Used

- Python3.6
- Django
- Html
- Bootstrap4
- JAVASCRIPT
- AJAX

## License

MIT &copy;2019 [DOminic Rutto](https://github.com/Leina33)
