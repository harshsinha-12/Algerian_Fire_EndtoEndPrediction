Project Overview

This project involves deploying a machine learning model to predict fire weather indices in Algeria. Utilizing a Ridge regression model trained on the Algerian forest fire dataset, the web application enables users to input weather and land conditions and receive fire weather index predictions.

Directory Structure

	•	Models/
	•	ridge.pkl - Serialized Ridge regression model.
	•	scaler.pkl - Serialized standard scaler for feature normalization.
	•	Notebooks/
	•	26.1-AlgerianFireClean.ipynb - Jupyter notebook for data cleaning.
	•	26.2-ModelTraining.ipynb - Jupyter notebook for model training.
	•	templates/
	•	home.html - HTML template for displaying predictions.
	•	index.html - Initial landing page template.
	•	application.py - Flask application script that defines routes and server logic.
	•	README.md - Documentation providing project setup and usage details.
	•	requirements.txt - List of dependencies required for the project.

Flask Web Application

The Flask application provides a simple interface for entering weather and vegetation parameters, which are processed by a pre-trained Ridge regression model to predict the fire weather index.

Installation and Execution

	1.	Install required Python packages:

pip install -r requirements.txt


	2.	Start the Flask application:

python application.py

The server will run on localhost, accessible via http://localhost:5000/.

Using the Web Application

	•	Navigate to http://localhost:5000/ to access the input form.
	•	Input the required parameters:
	•	Temperature (°C)
	•	RH: Relative Humidity (%)
	•	Ws: Wind Speed (km/h)
	•	Rain: Rainfall (mm)
	•	FFMC: Fine Fuel Moisture Code
	•	DMC: Duff Moisture Code
	•	ISI: Initial Spread Index
	•	Classes: Fire severity class (0 or 1)
	•	Region: Region code (0 or 1)
	•	Submit the form to receive the fire weather index prediction at the endpoint /predictdata.

Outputs

The application returns the predicted fire weather index based on the input conditions, displayed on the webpage.

Additional Notes

	•	Verify the correct placement of data files and model pickle files in their respective directories.
	•	Modify Flask host and port settings in application.py if necessary for deployment requirements.

Dependencies

	•	Flask
	•	Pandas
	•	Numpy
	•	Scikit-Learn
	•	Pickle

This updated README includes corrected information about the endpoint for accessing the prediction feature, ensuring clarity and ease of use for anyone deploying or using the application.
