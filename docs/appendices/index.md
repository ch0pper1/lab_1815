### Other methods of generator installation
#### Using WSL
There is also a nodejs application that can be installed locally.  To do this, open the command prompt to run the command `#!shell wsl --install -d Debian` to install a Debian based image under the Windows Subsystem for Linux (WSL).  Add a username and password to complete the install process.

Now that there is a linux terminal to use, we can go through the process of install nodejs and the openapi generator.  Perform the following steps to do so:

1. `#!shell sudo apt update && sudo apt upgrade -y`
2. `#!shell sudo apt install -y nodejs npm`
3. `#!shell npm install @openapitools/openapi-generator-cli -g`
