# Empty Thoughts (Name to be changed?)
[Empty Thoughts](https://empty-thoughts-071e97396088.herokuapp.com/) is a platform where you can freely express and share those fleeting thoughts that occur right before falling asleep, in the shower, or during that long daily commute.
Many of these thoughts go unused or unspoken, yet they often hold a certain charm and potential.
Empty Thoughts provides you with a canvas to voice these ideas, whether it's a profound insight, a small giggle-worthy joke or simply an empty thought.

[Responsive mockup]

## Table of Contents
+ [UX](#ux)
  + [User Demographic](#user-demographic)
+ [User Stories](#user-stories)
  + [Admin stories](#admin-stories)
  + [Visitor stories](#visitor-stories)
+ [Design](#design)
  + [Colour Scheme](#colour-scheme)
  + [Typography](#typography)
  + [Media](#media)
+ [Wireframes](#wireframes)
+ [Database Schema](#database-schema)
+ [Features](#features)
  + [Existing Features](#existing-features)
    + [Home Page](#home-page)
      + [Introduction](#introduction)
      + [Search](#search)
      + [Tags](#tags)
      + [User Profile](#user-profile)
      + [Pagination](#pagination)
    + [Navigation (Desktop/mobile?)](#navigation-desktopmobile)
    + [Account stuff](#account-stuff-login-signup)
  + [Future Features](#future-features)
+ [Testing](#testing)
  + [Validator Testing](#validator-testing)
  + [Fixed Bugs](#fixed-bugs)
  + [Unfixed Bugs](#unfixed-bugs)
+ [Technologies Used](#technologies-used)
  + [Main Languages Used](#main-languages-used)
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
  + [Installed Packages](#installed-packages)
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
- User site preferences (Dark mode, Search results per page)
- Customizing user profile
- Commenting on user profiles

## Testing

### Validator Testing
- Html - W3C validator
- CSS - Jigsaw validator
- JS - JSHint
- Python - PEP8 Online

- Lighthouse
- Other browsers
- Links?

### Fixed Bugs
- When viewing post details, the author(user) and logged in user would overlap in the context
  - Resolved by changing 'user' to 'author' in the view context

- When searching by multiple tags it could return duplicates if posts had multiple matching tags
  - Resolved by filtering posts by each tag individually (loop -> for tag in search)

- Setting the date of a model to current time with (models.DateField(auto_now_add=True)) threw an exception
  - Resolved by changing it to (models.DateTimeField(default=timezone.now))

- Heroku not using cloudinary static files during development
  - Resolved by setting Debug=false in settings.py, heroku attempts to serve static files by itself if debug is set to true
  
- Refreshing a page after submitting a comment sent another identical comment
  - Resolved by redirecting to current page without the comment context

- In the admin menu, searching by author would return an exception
  - Changed search_field from 'author' to 'author__username' to return a string rather than a user object

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
