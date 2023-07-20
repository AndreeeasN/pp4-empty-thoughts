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

## User Stories

### As a visitor
  - I can login to an account so I can view/post/like thoughts
  - I can view a list of thoughts so I can read interesting thoughts
  - I can leave comments so I can interact with those sharing similar interests/thoughts
  - I can like/unlike individual posts so I can show which ones I enjoy
  - I can search by category/author so I can find thoughts relevant to my interests
  - I can mark my posts as anonymous so I can post private thoughts without fear of judgement

### As an admin
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

## Database Schema

## Features

### Existing Features

#### Home Page

##### Introduction
##### Search
##### Tags
##### User Profile
##### Pagination

#### Navigation (Desktop/mobile?)

### Future Features

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
  - Resolved by simply changing 'user' to 'author' in the view context

- When searching by multiple tags it could return duplicates if posts had multiple matching tags
  - Resolved by filtering posts by each tag individually (for tag in search)

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
