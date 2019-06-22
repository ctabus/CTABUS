## CTABUS
#### readme coded by [bkcenik](https://wwww.github.com/bkcenik)

CTABUS is the second project for **Northwestern data science bootcamp**.

The main goal of the project was to create a tracker app for [CTA buses](www.ctabustracker.com/). The title of the project comes from Hayao Miyazaki's film **My Neighbor Totoro**, which features the catbus:

![catbus](https://www.johnnytimes.com/wp-content/uploads/2016/11/totoro-catbus-nekobasu-1024x574.jpg)

This project utilizes `HTML`, `bootstrap`, and flask-powered API.

Workflow:
* We used the [CTA's public API](https://www.transitchicago.com/developers/bustracker/) to track bus arrival times. The query is built by including the API key, route ID (ie bus name), stop ID (ie a number assigned to the bus stop's name). More information on how the query is structured can be found [here](https://www.transitchicago.com/assets/1/6/cta_Bus_Tracker_API_Developer_Guide_and_Documentation_20160929.pdf).

* The visualization was made by customizing a free `bootstrap theme`, [bizpage](https://bootstrapmade.com/bizpage-bootstrap-business-template/).

* the website is served through `flaskapp.py`. The API query is built by a separate `API.py` script, which is then fed into the main flask app.

* the route numbers and names, stop names and IDs, and lat/lons of the stops were loaded onto `mongodb`, from where they were extracted using the API query. 

* the main idea behind the query is:
    * ask the user to input route number
    * feed this into flask, retrieve the stop IDs that match this bus number.
    * return the bus stop list to user.
    * ask the user to input stop name.
    * feed back into flask, retrieve the stop ID that matches the stop name from mongodb.
    * add stop ID to query string.
    * feed the final query string into the API request.

* for displaying the timestamp, we used a DIY applet available from CTA's [developer tools](https://www.transitchicago.com/developers/.)

* the final product was hosted on `github.io`

Challenges:

* while the idea behind the app was fairly simple, there were several challenges we encountered:
    * bootstrap incompatibility with flask
    * building the query string by looping through stops
    * hosting on flask

#### Contributors: [Bercin Cenik](https://wwww.github.com/bkcenik), [Tina Huang](https://wwww.github.com/tinahuangyt), [Elias El Metannani](https://wwww.github.com/eliaselmet), and Geyang He.

