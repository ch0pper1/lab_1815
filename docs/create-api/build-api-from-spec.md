---
title: Lab 1815 - Build the API from a Specifcation File
---
Once the API definitions have been created and documented, the API needs to be served online so that watsonx Assistant can access the endpoints and retrieve the information.  For the purposes of this lab, we will use `#!shell openapi-generator-cli` to create the stub code, then serve the code using [IBM's Code Engine](https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started).

## Create the Python code
### Install Node and the Generator
There are several ways to use the openapi generator. Online tools can be used as well as docker containers.  For the purposes of this lab, we will install the tool locally using the following steps:
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

### Create the code
Now that the tool is installed locally, we can generate the stub code and modify it as necessary.  To Generate the code, use the following command:

``` powershell
openapi-generator-cli generate -g python-flask -i .\Documents\project\openapi.json -o .\Documents\project\server
```

In the above command, there are a few things to note.  First, the `#!shell -g` flag defines the type of code that will be created.  This example chose `#!shell python-flask`, but there are several other server options that are listed [here](https://openapi-generator.tech/docs/generators#server-generators).  The `#!shell -i` flag defines the specification file that was previously created.  Finally, the `#!shell -o` flag sets where the code will be created.  This command will need to be modified based on the individual environment and file locations.

Congratulations, you now have working code that serves the APIs defined in the openapi specification file!  Once running, the service will respond to API requests, which can be tested with `#!shell curl` commands locally.  The next step wil be to deploy the service into IBM's Code Engine for testing with watsonx Assistant.
