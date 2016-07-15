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
