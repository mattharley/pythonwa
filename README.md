# PDPD meetup site

A home for the Perth Django and Python community.

Please check out our [Meetup.com group page](http://www.meetup.com/Perth-Django-Users-Group/) for more details

And our [Slack Channel](https://pdpdmeetup-slack.herokuapp.com/)

## Developing Locally

*This project runs python3 because nobody uses python2 anymore.*

### Install pipenv

if you do not already have pipenv installed, you should do it!
follow the instructions here <https://docs.pipenv.org/en/latest/install/>

you may also want to consider install pyenv if you haven't already done so for python version support with pipenv.
<https://realpython.com/intro-to-pyenv/>

### Creating the virtual environment

move to the directory with this file in it and run the following command

    pipenv install --dev

this will install all the required packages for production and development.

### Activating the virtual environment

If your shell hasn't automatically enabled your virtual environment, you should now be able to access your virtual environment with this command

    pipenv shell

### Setting up the local development database

Run these commands to apply the latest migrations

    python manage.py migrate

### Running the local development server

Now you should be able to run the local dev server by running this command

    python manage.py runserver

## Testing

*It doesn't look like anyone has written any tests, Pull requests welcome!*

## Code style

### Black

code is formatted with `black` <https://black.readthedocs.io/>. Please consider running black over your files before you commit them. 

to run black go to the directory this file is in and run the following command.

    black .

### .editorconfig

To help editor with code formatting rules, we use a .editorconfig file (<http://editorconfig.org>), most modern code editors support this, some like VS Code require a plugin, see the link above for information on your editor of choice.

## Deployment

### requrements.txt

~~`requirements.txt` is for Heroku.~~

Heroku now prefers to use Pipfile over requirements.txt, so as long as you've installed your package with `pipenv install` and not `pip install` you shouldn't need to do anything else!

### Heroku

https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Install Heroku Client to get the `heroku` command:

- https://devcenter.heroku.com/articles/heroku-cli

Login to Heroku with Toolbelt:

- `heroku login`

Clone pdpdmeetup repository:

- `git clone https://github.com/mattharley/pdpdmeetup.git`

Add heroku remote URL:

- `cd pdpdmeetup`
- `git remote add heroku https://git.heroku.com/pdpdmeetup.git`

Deploy! (Probably fail if you don't have permission on Heroku, please ask Matt for access)

- `git push heroku master`

## Other useful info (especially for beginners)

Indent standard = 4 spaces

`project root` - This is the folder where all files relating to the project and its apps are stored.
Path = `/pdpdmeetup/`

`project app` - This is the core app for the project. Essentially its just the first app that got created and often contains core logic or shared files such as common templates.
Path = `/pdpdmeetup/pdpdmeetup/`

Templates are split into two locations.

1. Project templates which are shared amongst all apps are stored under the `project app`'s templates folder
Path = `/pdpdmeetup/pdpdmeetup/templates`

2. App templates which are app specific (where `app1` is the app name)
Path = `pdpdmeetup/app1/templates`
