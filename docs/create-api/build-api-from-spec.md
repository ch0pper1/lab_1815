---
title: Lab 1815 - Build the API from a Specifcation File
---
# Todo: replace this first sentence
Once the API definitions have been created and documented, the API needs to be served online so that watsonx Assistant can access the endpoints and retrieve the information.  For the purposes of this lab, we will use `#!shell openapi-generator-cli` to create the stub code, then serve the code using [IBM's Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started).

## Create the Python code
### Install Node and the Generator
To create the stub code, the OpenAPI team has provided an online generator tool that can be used to supply your JSON file and create the code.  We can also install the tool locally using the following steps:
#### Using scoop
1. Install scoop
``` powershell 
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
```
2. Install dependencies and application
``` powershell
scoop install git
scoop bucket add java
scoop install java/openjdk
scoop install openapi-generator-cli
```

#### Using WSL
There is also a nodejs application that can be installed locally.  To do this, open the command prompt to run the command `#!shell wsl --install -d Debian` to install a Debian based image under the Windows Subsystem for Linux (WSL).  Add a username and password to complete the install process.

Now that there is a linux terminal to use, we can go through the process of install nodejs and the openapi generator.  Perform the following steps to do so:

1. `#!shell sudo apt update && sudo apt upgrade -y`
2. `#!shell sudo apt install -y nodejs npm`
3. `#!shell npm install @openapitools/openapi-generator-cli -g`

### Create the code
Now that the tool is installed locally, we can generate the stub code and modify it as necessary.  To Generate the code, use the following command:

``` powershell
openapi-generator-cli generate -g python-flask -i .\Documents\project\openapi.json -o .\Documents\project\server
```

In the above command, there are a few things to note.  First, the `#!shell -g` flag defines the type of code that will be created.  This example chose `#!shell python-flask`, but there are several other server options that are listed [here](https://openapi-generator.tech/docs/generators#server-generators).  The `#!shell -i` flag defines the specification file that was previously created.  Finally, the `#!shell -i` flag sets where the code will be created.  This command will need to be modified based on the individual environment and file locations.

Congratulations, you now have working code that serves the APIs defined in the openapi specification file!  Once running, the service will respond to API requests, which can be tested with `#!shell curl` commands locally.  The next step wil be to deploy the service into IBM's Code Engine for testing with watsonx Assistant.
