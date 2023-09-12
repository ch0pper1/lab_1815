---
title: Lab 1815 - Deploy the application to IBM Code Engine
---
Now that the application has been tested and ready to deploy, we can use IBM Code Engine to host the service.  To access the code engine CLI, we will need to install the ibmcloud CLI on the local system using Powershell.  Please run the following command to install it:

``` powershell
iex (New-Object Net.WebClient).DownloadString('https://clis.cloud.ibm.com/install/powershell')
```

Confirm the prompts, restart the Powershell window, and you should now have access to the `#!shell ibmcloud` cli.  Next, install the Code Engine plugin with the command: 

``` powershell
ibmcloud plugin install code-engine
```

This tool will allow you to build an image of the application and upload it to a project.  The following procedure will walk through the steps to take your local application code and deploy it as a service.

## Deploy the application
The first thing is to open the cloud shell, then set the resource group target.  Each student has been provided a resource group in the format of `#!shell itzwa-studentXX-<rand_str>`.  This can be found on the main resource list and each student will only have access to one group.  To select this run the commands: 

``` shell
ibmcloud login -u jason.leiby+studentXX@mail.test.ibm.com
ibmcloud target -g itzwa-studentXX-<rand_str>
ibmcloud ce project select -n itzwa-studentXX-<rand_str>-codeengine
```

The first line will will request the password provided to you for this lab, while the second will select the resource group created with the necessary resources.  The third line will select the project previously built.  Once all the necessary environment settings are selected, run the following commands to build an image of your source code and deploy the application.

``` shell
ibmcloud ce buld create --name itzwa-studentXX-<rand_str> --build-type local
ibmcloud ce buildrun submit --name itzwa-studentXX-<rand_str> --build itzwa-studentXX-<rand_str> --source .
```
From the second command, there will be an output provided that defines how to check on the build process.  Once the build is complete, the same command will provide the endpoint where the image is hosted.  This URL will be needed in the next command: 

``` shell
ibmcloud ce application create --name itzwa-studentXX-<rand_str>-app --image private.us.icr.io/<namespace_string>/build-itzwa-studentXX-<rand_str>  --registry-key lab1815-key
```

??? note
    A registry key has already been created for your convenience.  Please use this to authenticate the application build commands

You can now use the `#! shell ibmcloud ce app get` command (provided from the above command) to see the status of the deployment, and once finished, provide the URL details where the application can be reached.  Test the deployment with a `#!shell curl` command to ensure the service is running.  

## Conclusion
Now that the service is running, it is time to connect watsonx Assistant to the application and build an assistant!