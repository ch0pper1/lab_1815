---
title: Lab 1815 - Connect watsonx Assistant to your Business Data using Custom Extensions
---

# Overview
## Connect watsonx Assistant to your Business Data using Custom Extensions
This hands on lab is designed to show you how to create an API and document it so that it can be used by watsonx Assistant.  The lab will start by creating an OpenAPI specification and generating code from it.  After local testing is complete, the API will be connected to the Assistant and tested.
These advanced techniques can be used for any situation or customization of an existing API.  At the end of the lab, users can incorporate this knowledge into their custom demonstrations, POCs, and MVPs. 
General programming skills and watsonx Assistant Action skills necessary. 

We will discuss three key areas:

  - [Building the OpenAPI Specification](create-api/build-api-from-spec.md)
  - [Deploy the API service](create-api/deploy-to-code-engine.md)
  - [Connecting your API to watsonx Assistant](connect-wa/connect-wa.md)

### Creating an API
This can be anything that can provide information to your conversational AI platforrm.  From a third-party weather API to the latest LLM for generative AI capabilities.  The API can also be built in any desired programming language.

For the purposes of this lab, we will focus on using Python and LangChain to connect to a [watsonx.ai](https://www.ibm.com/products/watsonx-ai){:target="_blank"} foundation model.

### Building an OpenAPI Specification
watsonx Assistant requires OpenAPI spec version 3.0.  This lab will will cover the tools to use in order to create a valid specification that watsonx Assistant will be able to ingest.

### Connect to watsonx Assistant
Once everything is created and working, it is time to connect to watsonx Assistant to test the API by building an Action that calls the extension and displays the returned data.