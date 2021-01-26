# devgrid-openweather

> WIP -- Development ongoing

Program that collects Open Weather API data and store it as a .json file
https://hub.docker.com/repository/docker/brunodpoliveira/devgrid-openweather

# How to Run

### Create OpenWeather Account
https://openweathermap.org/home/sign_up

### Collect API key
https://home.openweathermap.org/api_keys

> Rename it to API_KEY
> Be aware of the 2-hour cooldown on new API keys

### Update api.json 
> In the line
```
credentials = {'API_KEY': ''}
```
> Replace empty quotes w/ your key.

### Docker Initialization

> Copy+paste the following on terminal
```
docker container run devgrid-openweather
```
> It'll run the program in http://0.0.0.0:5000/

### Alternate Initialization

> Type the following commands on terminal
```
cd (folder where you saved devgrid here)
cd src
python3 app.py
```
> it'll run the program in http://127.0.0.1:5000


# How to Test (WIP)

### Run testing_code.py

> as of this commit, testing_code.py is a placeholder script. It won't work

# Tools Used + Reason

### Requested by Supervisor

> python,docker,github,asyncio

### Personal Preference

> ubuntu

### Version Control

> gitkraken (github), kitematic (docker)

### Reusability of Code from Previous Project

> flask






