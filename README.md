# Filament Review - Milestone 3 Project

[Live link](https://filament-review.herokuapp.com/)

[GitHub Repository](https://github.com/Gilleece/filament-review)

![](static/images/capture.png)

Filament Review is my milestone 3 project. This site is intended to be a community driven resource for reviews of various 3D printer materials. Users can view reviews for the material of their choice, and make an account to upload their own reviews which the can later edit and delete if they want. The site is built using HTML, CSS, Python, Flask and MongoDB. 

# Table of contents
1. [UX](#UX)
    1. [First Time Visitor Goals](#firsttime)
    2. [Returning Visitor Goals](#returning)
2. [Design](#design)
    1. [Colour Scheme](#colour)
    2. [Typography](#typo)
    3. [Layout](#layout)
    4. [Wireframes](#wireframes)
    5. [Database Schema](#schema)
3. [Features](#features)
    1. [Existing Features](#existing)
    2. [Future Features](#future)
4. [Technologies Used](#tech)
5. [Testing](#testing)
    1. [Manual Testing](#manual)
    2. [Automatic Testing](#auto)
    3. [Bugs](#bugs)
    4. [Known Issues](#issues)
6. [Deployment](#deployment)
    1. [Using Heroku](#heroku)
    2. [Building Upon This Project](#building)
7. [Credits](#credits)

## UX <a name="UX"></a>

The primary goal with the sites UX, in terms of UI, was to make the site easy to use and look appealing to the type of person that uses 3D printers, hence the graph paper theme to emulate a hobbyist work environment. The website is designed to clearly and simply present data to the user that they will find useful and help them acheive their goal of finding reviews.

### First Time Visitor Goals: <a name="firsttime"></a>
- As a first time visitor I need to be able to navigate the site easily and clearly understand how to use the function of the site.
- I want to be able to see a clear list of materials, along with a description of each material.
- I want to be able to search through reviews.
- I want to find a suitable product for my purposes.

### Returning Visitor Goals: <a name="returning"></a>
- I want to upload my own review.
- I want to edit/delete a review I made.
- I want to look at more reviews.

## Design: <a name="design"></a>

### Colour Scheme: <a name="colour"></a>
![](static/images/color.png)
- The site's primary colours are blue and white. I ended up really liking the "primary" blue in bootstrap and found it perfect as it was unobtrusive and helped users focus on the content.
- I wanted to deliberately avoid a variety of colour, keeping the site content and information focused. 

### Typography: <a name="typo"></a>
- Site wide, Helvetica Neue is used.

### Layout: <a name="layout"></a>
- The site uses a familiar and intuitive layout.
- Flask is used to present all content, along with flask forms for all forms on the site.

### Wireframes: <a name="wireframes"></a>

- The site's design changed slightly in production but the general idea and layout of the wireframe remains and was used to guide the design of the website as I made it.
- Here is the original wireframe: 

![](static/images/wireframe.png)

### Database Schema: <a name="schema"></a>

There are 3 collections in the database titled "materials", "reviews" and "users" respectively. 

#### Materials:
    material_name: string
    image: string
    path: string
    material_description: string
    example: string 

#### Reviews:
    material_name: string
    brand: string
    filament_name: string
    author: string
    rating: integer
    temperature: integer
    colour: string
    finish: string
    review_text: string
    image_url: string
    cost: integer
    likes: integer

#### Users:
    username: string
    email: string
    password: string
    admin: boolean





## Features <a name="features"></a>

### Existing Features <a name="existing"></a>
- Responsive on all devices.
- User accounts with passwords properly hashed and cookies for logged in users.
- Log in, log out and register functionality.
- Search Function
- Flask is used for the sites layout.
- Flask forms are used for all forms.
- Users can submit, edit and delete their reviews.
- Explanations of all material types present on the site. 
 

### Future Features <a name="future"></a>
- The reviews could have a like and dislike button, for users to give feedback on reviews and help avoid astroturfing.

## Technologies Used <a name="tech"></a>

1. [HTML:](https://www.w3.org/html/)
    - HTML was used for the content and structure of the site, with emphasis placed on semantic elements and text alternatives for screen readers.
1. [CSS:](https://www.w3.org/Style/CSS/)
    - Bootstrap was used to assist with the responsiveness and styling of the website. 
1. [Python:](https://www.python.org/)
    - All backend was built using Python and Pymongo.
1. [MongoDB:](https://www.mongodb.com/)
    - MongoDB was the database service for the site.
1. [Heroku:](https://www.heroku.com/)
    - Heroku was used to host the site and test it in a live environment.
1. [Bootstrap 5:](https://getbootstrap.com/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Flask:](https://flask.palletsprojects.com/en/1.1.x/)
    - This was used for the sites structure and for all forms.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.   
1. [Gitpod:](https://www.gitpod.io/)
    - This was my IDE for the project. 



## Testing <a name="testing"></a>

Testing was carried out both manually and automatically. 

### Manual Testing: <a name="manual"></a>

While building the site I had a preview open in my browser that I would check regularly to ensure that the results were as intended. I made use of developer tools within the browser constantly to check
across a number of things. I would use the console tools to try out different ideas, particularly styling, to see how it worked in real time and then implement the code written there into the project itself.
Responsiveness testing was done both through console tools, along with trying different browsers on different devices. 

My manual testing process was as follows:

#### For each page I performed the following checks:
    * Desktop and mobile
        - Make sure content loads properly, and timely.
        - No errors in console log, or IDE.
        - Try various potential user inputs and search parameters.
        - Try various things like refreshing the page in different sections.
        - Look for results that broke the styling in anyway.
        - Test different scenarios to see if the site continued worked (for example, I would input search parameters that return no results and see if the site continues functioning after this).
        - Emulate different errors like 404 to make sure they were being handled correctly.
    * Mobile only        
        - Try common gestures like pinch to zoom, rotating orientation.     

    All tests were performed across multiple browsers and OS.

Some examples of manual testing procedures are as follows:

#### Testing 1:

- Expected: User fills in the registration form and an account is created.
- Testing: Tested the feature by filling in the registration form and submitting it. 
- Result: The appropriate flash message appears, the cookie is created, and going to the profile page confirms that the account has indeed been created. Further more, manually checking the database shows the user present.

#### Testing 2:

- Expected: User, that has created an account, returns to the site and can log in.
- Testing: Tested the feature by filling in the login form and submitting it.
- Result: The appropriate flash message appears, the cookie is created, and the user is redirected to their profile page.

#### Testing 3:

- Expected: User, that has created a review, can edit their review.
- Testing: Tested the feature by going to the profile page, scrolling down to the user's reviews and clicking edit on one of them.
- Result: The user is redirected to the edit page where the edit form is generated, already populated by the relevant data from their review. Editing this data and clicking submit, then viewing the review on their profile page, confirms that the form is working as intended and the data is being correctly updated.
          
### Bugs: <a name="bugs"></a>

These are examples of some bugs that my manual testing uncovered, and how I fixed them.

#### Bug 1:

- Expected: User fills in the review form, clicks submit and the form is entered into the database.
- Testing: Tested the feature by filling in the review form and clicking submit.
- Result: Form appeared to behave as intended, however there was no new entry in the database.
- Fix: I set up console logs for errors to catch any problems, as a result I found that the form was not submitting due to a missing CSRF token. Ensuring that the token was being generated fixed the issue and the form submitted as intended.

#### Bug 2:

- Expected: When switching to mobile, all content should properly center and be displayed in an easily readible manner.
- Testing: Tested the feature by viewing the website on a mobile device, and also using the mobile device emulator built into the browser.
- Result: Most of the site appeared correctly, except for the titles of the review cards which were breaking to a second line and looked very messy. 
- Fix: I simply made the text smaller and this fixed it.

#### Bug 3:

- Expected: User clicks edit on their review and the form is generated with their review's content present.
- Testing: Tested the feature by logging in as a user with a review in the database, going to profile, and clicking edit under the review.
- Result: Form appeared and was functional, however the previous review's contents were not generating.
- Fix: I originally checked for any errors, however none were being presented. I tried posting the various form data to the console where I realized that it was coming up NULL. This lead me to finding the issue which was simply that I had mixed up two different app route variable names. Changing the variable name to the correct one in the app route fixed the issue. 

### Known issues: <a name="issues"></a>

Currently, there are no known issues.

### Automatic Testing: <a name="auto"></a>

[W3C Validator HTML result](assets/readme/w3chtml.png) (Shows no errors).

[W3C Validator CSS result](assets/readme/w3ccss.png) (Shows no errors).

Google Lighthouse results:

![](static/images/lighthouse.png)

## Deployment <a name="deployment"></a>

### Using Heroku: <a name="heroku"></a>

Hosting this project on Heroku required the following: - 
1. Make sure all project keys and secret values are placed in the heroku Config Vars for production.
2. Make sure requirements.txt is up to date with the following command: 	
		```
		pip3 freeze > requirements.txt
		```
3. Set up the Procfile - *A Procfile is required by Heroku .*
4. Set Flask's debugging to False.
5. Push all code to GitHub then use Heroku's GitHub function to deploy from GitHub to the production ready app.


**Upon successful deployment Heroku will give you the URL for your hosted app**

### Building upon this project: <a name="building"></a>

To get set up with a copy of my project you can do these multiple ways. 

**Via GitHub** -  
1. You can manually download locally to your machine and then upload to your preferred IDE. 
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few environment variables before we can run the app.
	1. `app.config["MONGO_DBNAME"] = "filament_review"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 app.py`

**Via the CLI** -
1. Clone my repo via Git using the following command `https://github.com/Gilleece/filament-review`
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few environment variables before we can run the app.
	1. `app.config["MONGO_DBNAME"] = "filament_review"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 app.py`

## Credits <a name="credits"></a>
- Thanks to [Reuben Ferrante](https://github.com/arex18), my Code Institute mentor, for his guidance and insight.

- Thanks to the Code Institute Slack community, it was a great resource for issues.

- Text examples explaining each filament from www.simplify3d.com

- Bootstrap, particularly their great documentation.

- W3Schools, for their fantastic explanations and useful examples.

- Flask form tutorial followed: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms

- Letter style credit to: https://codepen.io/mlms13/pen/LKFoy
