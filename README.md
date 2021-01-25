# devgrid-openweather
API that collects Open Weather data and store it as a .json file

# How to run

### Create OpenWeather Account
https://openweathermap.org/home/sign_up

### Rename api key
https://home.openweathermap.org/api_keys

> Rename it to API_KEY

### Create the api .json file
> In the line
```
credentials = {'API_KEY': ''}
```
> replace empty quotes w/ your key.

> Execute line below in terminal.
```
python3 creds.py
```

### Create two empty databases .json
```
with open(DATA_FILENAME, mode='w', encoding='utf-8') as f:
    json.dump([], f)

```

### add to list with this command
```
with open(DATA_FILENAME, mode='w', encoding='utf-8') as feedsjson:
    entry = {'name': args.name, 'url': args.url}
    feeds.append(entry)
    json.dump(feeds, feedsjson)

```

