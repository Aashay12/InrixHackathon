# InrixHackathon

# Link to Devpost ![https://devpost.com/software/parking-npxt9j]

# Inspiration
In 2020, 168,323 vehicles were stolen in California, at an estimated total value of approximately $1.6 billion.1 This is a 19.6 percent increase from the 2019 total for vehicle thefts statewide. The average rate of theft in 2020 was one vehicle every 3 minutes. Apart from vehicle thefts, we also considered other crimes while building our model that would guide the user by a simple ranking system to a safer and more cost-efficient on-street parking spot.

# What it does?

parKING is a progressive web application designed to help city governments and communities analyze and identify the best open on-street parking lots. It utilizes multiple machine learning models trained on various datasets to provide rankings based on safety, rates, proximity to destinations, and availability of traffic cameras.

The application starts with city planners entering the latitude and longitude of the location they want to analyze. This data is then sent to the server, where a city-specific model and graphical user interface (GUI) are created. The GUI is built using training models and data from sources like INRIX Traffic Rules APIs, INRIX Segment Roads APIs, INRIX On-Street Parking APIs, and Google Maps APIs. The system also utilizes polyline to geocode locations and perform distance calculations.

The algorithm is trained on a dataset from San Francisco that includes crime rates and related attributes. By aggregating data from this dataset, the model learns how each road's safety affects the ranking. This allows the model to predict new rankings based on specific road features, cost, proximity, available spots, and presence of traffic cameras. The model used is a Random Forest classification algorithm, which outperformed other algorithms like Decision Trees and Logistic Regression.

The application serves various stakeholders. City governments can use it to analyze existing on-street parking plans and receive proposals from private contractors. Contractors can leverage parKING to analyze the city's infrastructure and communicate their proposals directly to the government through public forums. Additionally, community members can access detailed information about on-street parking, visualize parking lot rankings, and explore other relevant parameters.

In summary, parKING is a comprehensive web application that combines machine learning, data analysis, and visualization to assist city governments, contractors, and communities in making informed decisions about on-street parking.


# How it was built?

parKING is a web application that integrates various datasets and APIs to provide parking lot rankings based on factors like cost, safety, proximity, and traffic camera coverage. The application utilizes the Inrix Lots API for parking cost and overnight parking data, the Inrix Traffic Camera API for traffic camera locations, and third-party APIs for crime data and proximity from destinations. By merging these datasets, a comprehensive data frame is created with the necessary metrics.

Machine learning techniques were applied to train and test the data, achieving a 75% accuracy rate. The implementation involved programming languages and frameworks such as HTML, CSS, JavaScript, and Python. Google Cloud served as the backend and GUI platform, while INRIX APIs, Google Maps, and polyline functions were used to develop the interactive GUI.

The machine learning models were built using Sklearn and Keras, and the website hosting was done through Heroku and GitHub. Data collection was performed from various sources, including the SF Police Data website and other open-source platforms.

Overall, parKING combines data integration, machine learning, and interactive visualization to offer valuable parking lot rankings and information to city planners, private contractors, and community members.

# Challenges 

During our work on parKING, we encountered challenges related to data availability and the complexity of developing geographic models. The lack of latitude and longitude information in the Lots API data limited our insights. However, through thorough exploratory data analysis, we managed to gain a better understanding of the data and develop suitable models. Training these models was challenging due to the large data size, and deploying them was not feasible on free servers. Nonetheless, with access to more comprehensive data, we believe we can further improve our models and GUIs for governments.

# Future Scope

The parKING application is well-suited for implementation at the local and state government level, providing city planners and officials with a valuable tool for optimizing on-street parking lots. Deploying the models on the web and streamlining the data collection, model training, and GUI creation process would greatly enhance efficiency. Acquiring a high-capacity web server to handle computation needs is a priority, and refining the algorithms to incorporate additional traffic parameters and road features is a future goal.
