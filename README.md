# pychallenge

I'm including just a really basic app which I want you to use as a base to improve on. I can't stress this enough - it's not about how much you can do and how fast or what fancy tricks you know, the real payoff for this is when we sit down together and you talk me through your decisions. 

Therefore - don't try to finish everything on this list. It is intentionally long. Pick what you think is important to make the app more robust. Feel free to go off list. Ping me with any questions. Feel free to spend as much or as little time as you want - 1-2 hrs is probably good, just do enough that we can talk through the decisions you made and how you approached it.

Please start a git repo with this so I can look at your history (create a repo on github and add me - `sbussetti` ). Check in the entire project first before you start making changes, then commit your changes as you go.  Add a good gitignore and replace this file with a more informative readme too.  Make sure to include your `sqlite.db` file.

Tests are written using pytest.  You can run tests by running `pytest` from the first `pychallenge` directory.

_DROPBOX LINK_

### Here are the tasks you can work through:

- Implement user authentication.  The site has several login protected pages, but no method for users to log into the site.
  - You can create users via the admin.  Bonus points if you include a self-serve user registration flow.
- Add a new section to the site titled 'About Me'.  It should pull information about yourself from the database that can be entered via the admin and be linked from the homepage.
  - Bonus points if you add one or more of:
    - The ability to author via a rich text editor
    - The ability to upload images to be displayed along with your personal info
    - Write some tests for the new section
- Add a Model to the articles app called Links.  It should be able to store an arbitrary URL.  Each article can have many links associated with it.  Update the Article view to display the list of links associated with it.
  - Bonus points for writing tests
- Fix a section of the site.  This project is incomplete and parts of it don't work.  Check the main urls.py for site sections, find one with issues, and fix it.
  - Bonus points for writing tests
- Apply pep8 or pylint to the repo and fix any style or static analysis errors.
- Find some existing code not covered by tests and write code coverage for it.
