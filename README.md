Perth Django and Python Developers
==================================

A home for the Perth Django and Python community. 

Please check out our [Meetup.com group page](http://www.meetup.com/Perth-Django-Users-Group/) for more details

And our [Slack Channel](https://pdpdmeetup-slack.herokuapp.com/)

Deployment
==========

https://devcenter.heroku.com/articles/getting-started-with-python#set-up

Install Heroku Client to get the `heroku` command.

- Arch Linux: https://aur.archlinux.org/packages/heroku-toolbelt/
- Ubuntu: ???

Login to Heroku with Toolbelt:
- `heroku login`

Clone pdpdmeetup repository:
- `git clone https://github.com/mattharley/pdpdmeetup.git`

Add heroku remote URL:
- `cd pdpdmeetup`
- `git remote add heroku https://git.heroku.com/pdpdmeetup.git`

Deploy! (Probably fail if you don't have permission on Heroku, please ask Matt for access)
- `git push heroku master`


Other useful info (especially for beginners)
============================================

Indent standard = tab

`project root` - This is the folder where all files relating to the project and its apps are stored.
Path = `/pdpdmeetup/`

`project app` - This is the core app for the project. Essentially its just the first app that got created and often contains core logic or shared files such as common templates.
Path = `/pdpdmeetup/pdpdmeetup/`

Templates are split into two locations.

1. Project templates which are shared amongst all apps are stored under the `project app`'s templates folder
Path = `/pdpdmeetup/pdpdmeetup/templates`

2. App templates which are app specific (where `app1` is the app name)
Path = `pdpdmeetup/app1/templates`

