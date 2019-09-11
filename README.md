# EV3 Tank

## Install and run
#### Install Anaconda Environment
We are going to use Anaconda environment for running python in a closet environment, feel free to use your favourite. First, go to https://www.anaconda.com/distribution/ and get the right installer for your OS. When the installation is done, run the following commands.
This command will create the env with the name ev3-tank and python version 3.6
```bash
conda create --name=ev3-tank python=3.6
```
When conda asks you to proceed, type ``y``

Activate the Env 
```bash
conda activate ev3-tank
```
After this command has rann successfully your command line will have ``(ev3-tank)`` before the line.
Run the activate command every time you are going to use the program.

#### Install The Libraries
Use this command to install all the required libaries. (If you are not using Anconda, you need to make sure you are using Python version 3.6)
```bash
pip install -r requirements.txt
```
