Project Overview

This project involves deploying machine learning models to predict fire weather indices in Algeria. It includes two versions: a Flask application and a Streamlit application, each utilizing a Ridge regression model trained on the Algerian forest fire dataset. Users can input weather and land conditions to receive fire weather index predictions.

Live Application Links

	•	Flask App: https://algerian-fire-endtoendprediction-1.onrender.com
	•	Streamlit App: https://algerianfire.streamlit.app/

	•	Flask App: Uses app.py for its operation.
	•	Streamlit App: Operates through main.py.


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

The Flask application provides a simple interface for entering weather and vegetation parameters, processed by a pre-trained Ridge regression model to predict the fire weather index.

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

![Algerian Fire Prediction Homepage](https://github.com/harshsinha-12/Algerian_Fire_EndtoEndPrediction/blob/main/Homepage.png)


<img src="https://github.com/harshsinha-12/Algerian_Fire_EndtoEndPrediction/blob/main/Pred.png" alt="Algerian Fire Prediction Screenshot" width="300" height="500"/>

Additional Notes

	•	Verify the correct placement of data files and model pickle files in their respective directories.
	•	Modify Flask host and port settings in application.py if necessary for deployment requirements.

Dependencies

	•	Flask
	•	Pandas
	•	Numpy
	•	Scikit-Learn
	•	Pickle

Techstack

<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a><a href="https://scikit-learn.org/" target="_blank" rel="noreferrer">
<img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="36" height="36" alt="Scikit-Learn" />
</a><a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/git-colored.svg" width="36" height="36" alt="Git" /></a><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/html5-colored.svg" width="36" height="36" alt="HTML5" /></a><a href="https://www.w3.org/TR/CSS/#css" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/css3-colored.svg" width="36" height="36" alt="CSS3" /></a><a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/flask-colored.svg" width="36" height="36" alt="Flask" /></a><a href="https://render.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/render-colored.svg" width="36" height="36" alt="Render" /></a><a href="https://aws.amazon.com" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/aws-colored.svg" width="36" height="36" alt="Amazon Web Services" /></a>
</p>

