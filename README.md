# Empty Thoughts
[Empty Thoughts](https://empty-thoughts-071e97396088.herokuapp.com/) is a platform where you can freely express and share those fleeting thoughts that occur late at night before falling asleep, in the shower, or during that long daily commute.
Many of these daily thoughts go unused or unspoken, yet they often hold a certain charm and potential.
Empty Thoughts provides you with a canvas to voice these ideas, whether it's a profound insight, a small giggle-worthy joke or simply an empty thought.

![Am-I-Responsive mockup](static/images/readme/pp4-responsive.png)

## Table of Contents
+ [UX](#ux)
  + [User Demographic](#user-demographic)
  + [User Stories](#user-stories)
+ [Design](#design)
  + [Colour Scheme](#colour-scheme)
  + [Typography](#typography)
+ [Wireframes](#wireframes)
+ [Database Schema](#database-schema)
+ [Features](#features)
  + [Existing Features](#existing-features)
    + [Navigation](#navigation)
    + [Main Page](#main-page)
    + [Thought Detail Page](#thought-detail-page)
  + [Future Features](#future-features)
+ [Testing](#testing)
  + [Discovered Bugs](#discovered-bugs)
  + [Validator Testing](#validator-testing)
  + [Unfixed Bugs](#unfixed-bugs)
+ [Technologies Used](#technologies-used)
+ [Deployment](#deployment)
+ [Credits](#credits)

## UX

### User Demographic

Empty Thoughts was built to give a voice to unspoken ideas and untapped ideas that otherwise would have been lost to time.
Meant for anyone with the capacity to dream but lacking a creative outlet, think of it as a chaotic collective diary where drifting thoughts can find a home.
With the freedom to post anonymously, even the extraordinarily silly or embarrassing can be shared without fear.

### User Stories

#### As a visitor
  - I can login to an account so I can view/post/like thoughts
  - I can view a list of thoughts so I can read interesting thoughts
  - I can leave comments so I can interact with those sharing similar interests/thoughts
  - I can like/unlike individual posts so I can show which ones I enjoy
  - I can search by category/author so I can find thoughts relevant to my interests
  - I can mark my posts as anonymous so I can post private thoughts without fear of judgement

#### As an admin
  - I can edit/delete posts so that I can moderate the website
  - I can manage tags so I can adjust for future content
  - I can sort through the admin menu so I can quickly find what I'm looking for

## Design

### Colour Scheme:
As the tags attached to posts showcase a plethora of colors the rest of the page has been given a mostly monochrome look as to not make the vibrant colors overbearing.
Both the header and footer are a darker shade of gray with white text, while the rest of the page is plain white with black text providing ample contrast.
Clickable links such as thought titles or authors are in the traditional hyperlink blue as to promote intuitive user interaction.

### Typography:
The following fonts were obtained from the Google Fonts Library:
- Header logo - 'Roboto Condensed' by Christian Robertson
- Navigation and site content - 'Nunito Sans' by Vernon Adams, Jacques Le Bailly, Manvel Shmavonyan and Alexei Vanyashin

## Wireframes
- Home page<br>
![Home page](static/images/readme/pp4-wireframe-index.png)
- About page<br>
![About page](static/images/readme/pp4-wireframe-about.png)
- Search page<br>
![Search page](static/images/readme/pp4-wireframe-search.png)
- Thought Details page<br>
![Thought Details page](static/images/readme/pp4-wireframe-thought-detail.png)
- User Details page<br>
![User Details page](static/images/readme/pp4-wireframe-user-detail.png)

- As users are unlikely to visit the 'About' page a second time around and the 'Search' page was simply too similar to the Home page, these two pages both ended up being merged into the Home page during development. 

## Database Schema

![Database Schema](static/images/readme/pp4-erd.png)

## Features

### Existing Features

#### Navigation
![Navbar logged in](static/images/readme/pp4-nav-logged-in.png)<br>
- Header logo
  - Brings user to the home page on click
- Home
  - Same functionality as clicking on the header, brings user to home page
  - Is highlighted as active while on the home page, turns inactive when searching for posts or while on a different page
- Search
  - The 'Search' button in the navigation bar opens up a sidebar where the user can search for posts by their title, content, author and tags.<br>
  ![Search sidebar](static/images/readme/pp4-nav-search-bar.png)
  - The search function is accessible from all pages, and the search results are displayed on the home page.
  - During a search the 'Search' navbar element will be highlighted as active
- Log in / Sign up<br>
  ![Navbar logged out](static/images/readme/pp4-nav-logged-out.png)
  - When not logged in displays a link to log in or sign up
- Profile Name<br>
  ![Navbar dropdown](static/images/readme/pp4-nav-user-dropdown.png)
  - When logged in displays a dropdown menu where your user profile and log out button can be found
  - If logged in as a superuser the Admin Menu can be reached from here as well

#### Main Page
- About
  - On first visit the user will be presented with a short introduction to the website and the options to log in / sign up.<br>
  ![Home page - About](static/images/readme/pp4-about.png)
  - Once logged in this will be replaced with a simple hello, 'create thought' button and suggestion for the user to share whatever is on their mind.<br>
  ![Home page - Share](static/images/readme/pp4-first-page.png)
- Thoughts<br>
![User-submitted thought](static/images/readme/pp4-thought.png)
  - Can be liked by clicking on the heart icon, comments can be read by clicking on the comment icon or title of the thought.
  - If the author chooses to post anonymously their name will be shown as 'Anonymous'.
  - If submitted with a time entered, it will appear next to the author name.
  - If the user is the owner of a post '(You)' will be added to the author name, and buttons to edit or delete the post will be visible.
  - On attempting to delete the post, a confirmation window will be displayed before final deletion.<br>
  ![Delete confirmation modal](static/images/readme/pp4-delete-modal.png)

- Tags
  - Tags are pre-made are used to categorize posts and can be searched for using the search function.
  - Clicking on a tag will automatically start a search using that tag to find similar content.<br>
  ![Tags](static/images/readme/pp4-tags.png)
  - Admins can freely change text and background color from the admin menu.

- Pagination
  - To ensure consistant performance, user-submitted content has been split into pages as to not load everything at once.<br>
  ![Pagination](static/images/readme/pp4-pagination.png)
  - Page selection allows the following:
    - Jump one page forward / back
    - Jump to the first / last page
    - Jump to a page within 3 pages of the current one

#### User Account
- User Profile
  - Displays signup date and some basic feats of the user (Posts, comments, likes)
  - Also provides the option to search for all of their public posts<br>
  ![User details](static/images/readme/pp4-user-details.png)
- Sign in<br>
![Sign in page](static/images/readme/pp4-sign-in.png)
- Sign up<br>
![Sign up page](static/images/readme/pp4-sign-up.png)
- Sign out<br>
![Sign out page](static/images/readme/pp4-sign-out.png)

#### Thought Detail Page
A larger view of specific thought, has exact same functionality as when viewed from the home page. <br>
![Thought details page](static/images/readme/pp4-thought-details.png)
- Comment form
  - A simple text input with the option to post anonymously.
- Comments
  - Comments can be liked by clicking the heart icon, similar to liking a posted thought.
  - Can be deleted by the owner of the comment or a superuser.

### Future Features
- Password resets
- User site preferences (Dark mode, Search results per page, etc.)
- Customizing user profile
- Commenting on user profiles

## Testing

### Discovered Bugs
- When viewing post details, the author(user) and logged in user would overlap in the context
  - This would end up displaying the author of the post as the user currently logged in which ended up difficult to notice during development before introducing a second account
  - Resolved by changing 'user' to 'author' in the view context to avoid conflicts

- When attempting to like another user's comment when logged in as a non-superuser you would be redirected to the login page with the message "Must be logged in to leave likes"
  - This was caused by a misplaced safety check, rather than checking if user was authenticated it would check if user was a superuser
  - Resolved by replacing the function user_is_owner_or_superuser with the function user_is_logged_in in the corresponding view

- When searching by multiple tags it could return duplicates if posts had multiple matching tags
  - Resolved by filtering posts by each tag individually (loop -> for tag in search)

- Setting the date of a model to current time using (models.DateField(auto_now_add=True)) threw an exception
  - Resolved by changing it to (models.DateTimeField(default=timezone.now))

- Heroku not using cloudinary static files during development
  - Heroku attempts to serve static files by itself if debug is set to true in settings
  - Resolved by setting Debug=false in settings.py

- When checking for ownership of an object it would come back false if not a superuser
  - This was due to a faulty comparison in the function user_is_owner_or_superuser
  - Resolved by replacing (user is object_owner) with (user == object_owner)

- Refreshing a page after submitting a comment sent another identical comment
  - This was caused by the comment form context being included on refresh
  - Resolved by redirecting without the comment context upon succesfully submitting a comment

- In the admin menu, searching by author would throw an exception
  - Changed search_field from 'author' to 'author__username' to return a string rather than a user object

- On deleting a comment the deletion modal would display "Delete null?"
  - This was due to the delete button missing a title attribute required by the JS handling the confirmation modal.
  - Resolved by adding the missing attribute data-delete-title to the delete button

### Validator Testing
- Html
  - All html pages pass through the [W3C Validator](https://validator.w3.org/) without issues
- CSS
  - CSS files pass through the [W3C jigsaw validator](https://jigsaw.w3.org/css-validator/) without errors<br>
  ![w3C Validator](static/images/readme/pp4-W3C-CSS.png)
- JS
  - All JS files pass through the [JSHint Validator](https://jshint.com/) without issues
- Python
  - Python files pass through the [CI Python linter](https://pep8ci.herokuapp.com/) without issues
- Lighthouse audit<br>
  ![Lighthouse Audit](static/images/readme/pp4-lighthouse.png)
- The website has been tested to work in the following browsers:
  - Google Chrome
  - Mozilla Firefox
  - Microsoft Edge
  - Opera
- All external links open in a separate tab as intended.

### Unfixed Bugs

## Technologies Used

### Main Languages Used
- HTML5
- CSS3
- Javascript
- Python
- SQL - Postgres

### Frameworks, Libraries & Programs Used
GitHub
Visual Studio Code
Django
Bootstrap
JQuery
Font Awesome
Google Fonts
Balsamiq
DrawSQL
Paint.NET
Favicon.io

### Installed Packages
Django
django-allauth
psycopg2-binary
gunicorn
django-crispy-forms
crispy-bootstrap5 
django-colorfield 
django-select2 
django-filter
django-bootstrap-datepicker-plus
dj3-cloudinary-storage

## Deployment

## Credits
