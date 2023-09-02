---
title: Lab 1815 - Creating the API
---

## What you will need

* Your choice of API.  This can be one of the following:
    * Python
    * Node JS
    * PHP
    * Go
    * Other*
* Knowledge of REST API requests
* A text editor or Programming IDE
  
??? note "A note on programming languages"
    Any programming language that provides REST modules can be used.  The ones listed above are just the languages that can be used with IBM's Cloud Functions

## Getting Started
There are several methods to create a REST API and each programming language will provide its own methodologies.  This lab will cover how to setup a basic API that will return a JSON object that can be used by watsonx Assistant for context data.  The key is to create a well defined API that can then be used to create the openapi documentation which WA will use.

### Build the API
For the purposes of this lab, the API will be built using python with the Flask module for http communication.  This module will need to be installed and then imported into the program.

``` bash title="install Flask"
pip install flask
```
This will install the necessary module files for the application to run.

``` py title="server.py" linenums="1"
from flask import Flask,jsonify
```
The import command will associate the modules needed for responding to API requests and return JSON objects in the response.

### Instantiate the Flask application and add an endpoint
Now that the necessary modules are installed and imported, it is time to create the application to serve the API. Here is the basic structure to the API application:
```py title="server.py" linenums="3"
app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def test():
    return jsonify({ "response": "yes, this worked." })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001)
```

This simple application exposes a single url, or route, to return a JSON object with a response element.  From here, you can test this by running a curl command `curl -X GET http://localhost:9001/test` to ensure it is working.  The response should look like this:
```py
{
  "response": "yes, this worked."
}
```

Now that data can be returned via API, the next step is to document the API and test it using IBM Code Engine and watsonx Assistant.