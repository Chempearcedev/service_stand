# Service stand 

*Introduction* 

This app acts as a location for professionals in the TV and Film industry to connect for the purpose of film and tv making. 
The main purpose of the site is to offer a platform for individuals to display their profile and be easily found based on aspects such as location availability.

The ability to find professional within the tv/film industry near the location of
filming, can greatly help with the logistical planning of the filming process. This platform's intent is to help with this issue by
by enabling production companies to source crew members and staff based on locations and skill set.

The site includes profiles of professionals from lighting crew, sound engineers and location scouts to actors and production coordinators, 
who are able to login into the site, build a profile to display on the platform their location availability, skills, availability
to work and contact details.

## Table Of Contents

### 1. [ Goals ](#goals)  
### 2.  [ UX ](#goal)
### 3.  [ Design ](#goal)
### 4.  [ User Stories ](#goal)
### 5.  [ Features ](#goal)
### 6.  [ Technologies ](#goal)
### 7.  [ Testing ](#goal)
### 8.  [ Deployment ](#goal)

<a name="goals">
 Goals
</a>

---
To act as a platfrom for professionals in the TV/Film industy to connect for the purpose of work. 

To provide TV/Film makers a platform to source individuals based on locations and skill set, allowing them to employ people closer to the location of filming.

To allow users to create a profile showcasing their availability, skill set, locations availabiity and contact details, and update and delete their profile freely.

## UX

---

This app was created to work on mobile size first, the ease of navigation allows users to find what they need on the platform.

A simple palette has been used to avoid distraction form the functionality this app offers.

The main attaraction of the app is the profesional profiles listed to enable users to discover the right individual based on key words.

### User Stories 

- I am a production company making a TV or Film and would like to source crew members that are close to the area of filming.

- I am a professional who makes TV and Films and would like an app that allows me to search for crew members based on key words

- I am a user who would like an app that i can access from a mobile, iPad or laptop.

- I am a professional who works in TV and Film and would like to find a platform that allows me to connect with professionals within the TV and Film industry for the purpose of work.

- I am a crew member within the TV and Film industry that would like to showcase my skills on a platform and have the ability to update my details through a personal profile 

 - I am a user and i would like to delete my profile 

 - I am a user and i would like to change the image in my profile 

 - I am a user and i would like to show my telephone contact number ONLY if i am available for work offers now 

 - I am a user and i would like to view my profile on a personal profile page 

 - I am a user and i would like to search key words such as location, profession and skill in a search bar to find relevent profiles 

 ## Features 

---

<br />

## *Homepage* 

<br />


The base page shows a search bar at the top that invites users to search for key words so they are able to find only the profiles that are relevent to their search.

Below this there are profiles that have been created by users. Within the profile is a collapsible box that includes details of their skills, contact details, availability, location and an image.

<br />


![alt tag](https://images.pexels.com/photos/4672292/pexels-photo-4672292.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500 "Description goes here")

## *User Profile* 

<br />

Within the user profile page, users can see any profiles they have created. From herew they can tracvk how their professional skills and availability are progressing.

At the bottom of their profile, users are able to edit or delete their profile using button.

<br />

![alt tag](https://images.pexels.com/photos/4672292/pexels-photo-4672292.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500 "Description goes here")

##  *Create A Job*

<br />

If a user click on 'create a job' at the top of the page in the navigation bar, they are taken to a page that has a form they are able to fill out. The form hold all the details that will show within their personal profile.

<br />


![alt tag](https://images.pexels.com/photos/4672292/pexels-photo-4672292.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500 "Description goes here")

<br />


## Technologies 

---

* Dev Tools
  * This project used the Dev Tools to support responsiveness design.
* Heroku
  * Used for app hosting and deploying.
* GitHub
  *  This project uses GitHub to store and share the project remotely.
* Git
* MongoDB Atlas
   * Used to store data 
* Materialize 
  * Frameworks 
* Figma 
  *  Wireframe 
* W3 Validator 
* PEP8 test

### Languages

* HTML
* CSS
* JavaScript 
* Python

### Further Resources 
* Stack Overflow 
* Slack 
* W3 Schools 
* Font Awesome

## Deployment 

--- 
### Heroku 
- To make a requirements.txt file type -  pip3 freeze --local > requirements.txt into the command line.

- Firstly you need a requirements.txt file and a Procfile to tell Heroku the dependencies needed to run this project.
 

- Making a Procile you need type -  echo web: python run.py > Procfile

Now deploy to Heroku:


- Login to personal your account.

- Click on the new button.

- Select "create new app"


Now you need to connect the Github repository to our app on Heroku:

- Click on the Deploy tab on the dashboard.

- In the deployment method area, select to use GitHub.

- You will then be able to find the GitHub repository and to connect too.

- Enter the name of the repository for the project i want and click on the connect.

Include the environment variables.

- Click on the settings tab on the dashboard.

- Click reveal config vars button and then add:

*key*: IP, Value: 0.0.0.0 <br />
*key*: PORT, Value: 5000 <br />
*key*: MONGO_DBNAME, value: (Name of the database you are connecting too.) <br />
*key*: MONGO_URI, value: (Mongo Uri)
*key*: SECRET_KEY, value: (A custom secret key)

Go back to the Deploy tab again to enable the automatic deployment feature.

Click on the Deploy tab.

In the automatic deployment section, SELECT the branch you want to deploy and click on the Enable Automatic deploy button.

### Local copy
- Go to the workspace of your local copy. In the terminal window of your IDE type: *pip3 install -r requirements.txt*
 - Signup or login to your MongoDB account.
Create a cluster and a database.
- Create 4 collections: image_url, professions, jobs and users.
 - Create the environment variables:
    *  Create a .gitignore file in the root directory of the project.
    * Create the file env.py. This will contain all the envornment variables.
    * Add the env.py file to the .gitignore.



### Clone the app

To make a local clone, follow the following steps.

- Log in to GitHub and go to the repository.
 - Click on the green button with the text Code.
- Click on “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application.



















