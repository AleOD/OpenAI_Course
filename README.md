I create a venv with conda and then a nested one with python.


to run:
-activate conda env: 
	conda activate

-activate python env (nested):
	source env/bin/activate

- activate flask:
	flask run

dependecies:
-flask
-python_dotenv
-openai


*Make sure to add your own OpenAI API key either directly to the code or as an external variable.
To use the code as it is just create a ".env" file and assign the key to a variable.
Example:
OPENAI_API_KEY ="key"

**Turn off firewall

