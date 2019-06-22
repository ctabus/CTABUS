## CTABUS
#### readme coded by [bkcenik](https://wwww.github.com/bkcenik)

CTABUS is the second project for **Northwestern data science bootcamp**.

The main goal of the project was to create a tracker app for [CTA buses](www.ctabustracker.com/). The title of the project comes from Hayao Miyazaki's film ** My Neighbor Totoro**, which features the catbus:

![catbus](https://www.johnnytimes.com/wp-content/uploads/2016/11/totoro-catbus-nekobasu-1024x574.jpg)

This project utilizes `HTML`, `bootstrap`, and flask-powered API.

Workflow:
* We used the [CTA's public API](https://www.transitchicago.com/developers/bustracker/) to track bus arrival times. The query is built by including the API key, route ID (ie bus name), stop ID (ie a number assigned to the bus stop's name). More information on how the query is structured can be found [here](https://www.transitchicago.com/assets/1/6/cta_Bus_Tracker_API_Developer_Guide_and_Documentation_20160929.pdf).

* The visualization was made by customizing a free `bootstrap theme`, [bizpage](https://bootstrapmade.com/bizpage-bootstrap-business-template/).