# Hack Collect API
* This is the API of Hack Collect. A React app used to post and rate Life Hacks. The live link for the API can be found here: [Hack Collect API](https://pp5-hack-collect-drf-f277d220324f.herokuapp.com/)
<br>
The GitHub repository for the frontend can be found here: [Hack Collect React App](https://github.com/CI-Dominik/pp5-hack-collect)

## **TABLE OF CONTENTS**

[**DEVELOPMENT GOAL**](#development-goal)

[**AGILE PLANING**](#agile-planing)
* [Epics](#epics)
* [User Stories](#user-stories)

[**API ENDPOINTS**](#api-endpoints)

[**DATABASE**](#database)

[**TECHNOLOGIES**](#technologies)
* [Python](#python)
* [Django REST Framework](#django-rest-framework)
* [Cloudinary](#cloudinary)
* [Visual Studio Code](#visual-studio-code)
* [GitHub](#github)
* [Heroku](#heroku)

[**TESTING**](#testing)

[**DEPLOYMENT**](#deployment)
* [TEXT](#xxxxxxxxxxxxxxxx)
* [TEXT](#xxxxxxxxxxxxxxxx)
* [TEXT](#xxxxxxxxxxxxxxxx)
* [TEXT](#xxxxxxxxxxxxxxxx)
* [TEXT](#xxxxxxxxxxxxxxxx)
* [TEXT](#xxxxxxxxxxxxxxxx)
* [TEXT](#xxxxxxxxxxxxxxxx)

[**CREDITS**](#credits)
* [Flake8 Extension](#flake8-extension)
* [Visual Studio Code](#visual-studio-code-1)
* [YouTube](#youtube)
* [Special thanks](#special-thanks)

---

## DEVELOPMENT GOAL
* PLACEHOLDER

---

## AGILE PLANING
* Here, a list of Epics and User Stories is displayed. A full list of the implemented features can be found in the [frontend's readme file](https://github.com/CI-Dominik/pp5-hack-collect/blob/main/README.md)

## Epics
* PLACEHOLDER

## User Stories
* PLACEHOLDER

---

## API ENDPOINTS

### `/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/categories/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/categories/id/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/comments/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/comments/id/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/followers/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/followers/id/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/hacks/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/hacks/id/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/profiles/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/profiles/id/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/ratings/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/ratings/id/`

**Methods**:
  * GET

**Implementation**:
* PLACEHOLDER

<br>

### `/dj-rest-auth/login/`

**Methods**:
  * POST

**Implementation**:
* PLACEHOLDER

<br>

### `/dj-rest-auth/logout/`

**Methods**:
  * POST

**Implementation**:
* PLACEHOLDER

<br>

### `/dj-rest-auth/registration/`

**Methods**:
  * POST

**Implementation**:
* PLACEHOLDER

<br>

---

## DATABASE

## Database structure
![Image of the database structure](docs/database.jpg)

---

## TECHNOLOGIES

### Python
* Python was used as a programming language for editing backend code.

### Django REST Framework
* Django REST Framework was used as a to manage views, URLs, models and serializers.

### Cloudinary
* Cloudinary was used to store the image files uploaded by users.

### Visual Studio Code
* Visual Studio Code was used to clone the GitHub repository, edit the homepage's code and commit / push the results to GitHub. In addition, plugins were used to verify the code structure and best practices.

### GitHub
* GitHub was used to store the homepage's files, the user stories and epics.

### Heroku
* Heroku was used to host the API which is accessed by the React app.

---

## TESTING
* All endpoints were tested for their correct JSON response. In-depth testing can be viewed in the [frontend's testing file](https://github.com/CI-Dominik/pp5-hack-collect/blob/main/TESTING.md).

## Flake8 testing
* Every folder was checked using the Flake8 checker. Only files that were automatically created via `python makemigrations` or not altered by me (admin.py, tests.py) threw errors. Those do not impact the usability of the API in any way and were just too long lines or unused imports.

### Categories

![Image of the checked folder](docs/flake8/categories.jpg)

### Comments

![Image of the checked folder](docs/flake8/comments.jpg)

### Followers

![Image of the checked folder](docs/flake8/followers.jpg)

### Hacks

![Image of the checked folder](docs/flake8/hacks.jpg)

### Profiles

![Image of the checked folder](docs/flake8/profiles.jpg)

### Ratings

![Image of the checked folder](docs/flake8/ratings.jpg)

---

## DEPLOYMENT

## GitHub
* PLACEHOLDER

## Heroku
* PLACEHOLDER

---

## **CREDITS**

## [Flake8 Extension](https://flake8.pycqa.org/en/latest/)
* Used to verify Python code.

## [YouTube](https://youtube.com)
* Videos for understanding some code areas.

## [Visual Studio Code](https://code.visualstudio.com/)
* Used to generate HTML boilerplate code and code editing.

## Special thanks
* A special thank you to my mentor Gareth McGirr who helped me along my journey and also to my best friend Frederic, who provided me with helpful insights and assisted me with many testing scenarios.