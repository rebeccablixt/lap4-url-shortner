# URL Shorties

24 hour challenge. Users should be able to enter a url into an input box on the website's front page. The backend will then generate a shortened path at which a User can access their url. If User tries to access the website with a path stored in the database, they should get rerouted to the URL it relates to. If User tries to access the website with a path not stored in the database, they should get rerouted to the homepage where they can create a new short URL.

Live project: [URL Shorties](https://url--shorties.herokuapp.com/)

## Contact

- [Layla Southcombe](https://github.com/LaylaSouthcombe)
- [Rebecca Blixt](https://github.com/rebeccablixt)

## Installation

- Clone the repo and cd into the project folder
- Enter the pipenv shell in a way that works with your machine
- `pipenv install`

## Usage

- To start app: `pipenv run dev`

## Technologies

- Python
- Flask
- PostgreSQL
- Waitress

## Process

1. Basic setup
2. Create API routes
3. Setup deployment and deploy to Heroku
4. Create, style, and add templates to routes
5. Setup database

## Bugs

Deployed version: cannot query the shortened URL from database.
Development version: none that we can see. Please let us know if you find any.

## Wins & Challenges

### Wins

- Backend and frontend work locally

### Challenges

- Getting the database to work in the deployed website
