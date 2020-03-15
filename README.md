# Laturel Webpages

Laturel homepage for offering web design and website development services. Also includes car cost calculator to compare costs between different technologies (EV, gasoline, diesel engines).

## Built with
* Flask - Python webapp framework for backend
* Custom CSS - Frontend CSS framework with custom stylesheet
* SQLite - Database for storing the long-term data
* Nginx and Gunicorn - Deployed on Ubuntu 18.10 webserver

## WIP
This webapp is cosntantly under development and I'm adding features as it goes. Improvement suggestions and feedback is greatly appreciated!

# Setup

* Set up the MAIL_USERNAME, MAIL_PASSWORD and SECRET_KEY environment variables
* Build the container with docker-compose build
* Run the container with docker-compose up -d and navigate to localhost:5000 for development
* Run the container in production mode with docker-compose -f docker-compose.prod.yml up -d --build and navigate route traffic from your domain to the webapp

# TODO

- [x] Combine emobility and web to main site with emobility and web products
- [x] Refactor the templates folder to follow the combined route structure
- [ ] Separate customer sites as blueprints
- [ ] Prototype the website cost estimator
- [ ] Add Laturel logo to nav to signify where customer is
- [x] Implement cookie consent

# What visitors should be able to do on this site
- [x] Contact me
- [x] Know what services Lauturel offers
- [ ] Know what does it cost approximately to create a site
- [ ] See what completed projects I have done
