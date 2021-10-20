# Currency Exchange API
This directory contains an example of Python script to create a web server to provide REST API for Currency Exchange<br />
- Python Web Framework: Flask <br />

Using Currency Exchange API developed by fyhao.

<hr />

## Usage
### To get currency exchange by specifying the quotes of source and destination.
Parameters:<br />
- source: string, Source currency. <br />
- destination: string, Destination currency.<br />
- value: string, Response from Currency Exchange API. If success it will return float number for the currency exchange rate.<br />
Example request:
```
GET http://localhost:8080/exchange?source=EUR&destination=JPY&value=123.4
```

<hr />

## Setup
### Prerequisites
- Python 3.9.7
- pip

### Setup for local running 
1. Set important environment variables in currency_exchange_api/run.ps1
2. Open powershell then run the command this below command to setup and start web server 
```
$ run.ps1
```
3. Now web server is ready on localhost:8080

<hr />

## Additional Information 
How to get Rapid API Application key 
1. Browse to https://rapidapi.com and create new user or login with exist user account. 
2. Browse to https://rapidapi.com/fyhao/api/currency-exchange or search for API called "Currency Exchange" by fyhao. RapidAPI will automatically create a new app for this API. 
3. Browse to https://rapidapi.com/developer/, select new app that created under My apps then select Security menu. The Application Key will be shown on the screen.

<hr />

## References
- https://flask.palletsprojects.com/en/1.1.x/
- https://rapidapi.com/fyhao/api/currency-exchange