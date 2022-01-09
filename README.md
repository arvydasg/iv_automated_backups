# little bit about the project

Since I don't trust/understand automated backups of websites and I would rather backup things myself, know where they are stored and what is actually "backuped",
I create backups for my client sites manually. The procedure is:

* Open website
* Add username
* Add password
* .click Log in to client's hosting provider's dashboard panel
* .click on the needed server
* .click on directadmin panel
* .click on "atsargines kopijos"
* .click on "generuoti atsargine kopija"
* .close tab
* .click log out

REPEAT 3x times

10 clicks at least

And I prefer to have at least one backup for every client at least once or twice a week for general maintenance.

When I want to do more modifications during the week, I like to make backups more often. Same 10 click procedure every time...

# My thought

Since I have decided I want to slowly move away from Wordpress sites (the work itself is meh, drag and drop interfaces, have to learn php (when i prefer JS or Python), the competition is enormous (50 developers for one job), I don't get to type nothing, losing my EMACS skills..) to learn more of real programming. Learn what you like the most, not what is needed most, right? And after half a year or so I realized that I  prefer coding instead of drag and drop WordPress website building.

# Solution for real

For a while now I have been thinking how cool it would be to automate some tasks. A year ago that is why I started to learn coding, so I can automate boring tasks!

So why not use Python to automate the process described above? It should be quite simple, right?

After a looooong period of not touching text editors, I installed emacs, configured it to my liking once again (my muscle memory surprises me).

I then found out about selenium and it can be used to interact with websites.

First I installed it and configured by watching some YouTube videos and when it finally didn't work out as expected I directed all of my attention to the official docs - https://selenium-python.readthedocs.io/getting-started.html

Then I insalled python venv to organize my packages better? But I already had them installed in my whole system, so kind of not needed I guess, but good to remember from the Django times and to know for the future.

Got a correct chrome driver. In my version it was -  version 96.0.4664.45

Any deprecation errors were fixed by this - https://stackoverflow.com/questions/69875125/find-element-by-commands-are-deprecated-in-selenium

# What I learned

* What is a webdriver
* How to open a webpage with Selenium
* How to login into a page with Selenium
* How to scroll with selenium - https://stackoverflow.com/questions/20986631/how-can-i-scroll-a-web-page-using-selenium-webdriver-in-python
* how to click on all kinds of web elements with Selenium
* how to create a function with Python
* How to return a value from a function with Python
* How to reuse a returned function in another function with Python - https://www.youtube.com/watch?v=nuNXiEDnM44 (had to also go back to my CodeInPlace course for a reference)
* How to use an external config file to store values for a python function to use (so the passwords and usernames I use in a function wouldn't be visible to you ;> ) - https://www.youtube.com/watch?v=Gdw0-QGq-z0
* How to run multiple python scripts from one one bash file

# Known bugs

* Doesn't close browser windows after each script runs (not a biggie, everything still works, might fix later)