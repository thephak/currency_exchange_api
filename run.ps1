<# Install required packages #> 
pip install -r requirements.txt

<# Set Enviroment variables for the project here #> 
$env:FLASK_ENV   = "development"
$env:HOST_IP     = "localhost"
$env:HOST_PORT   = "8080"
$env:API_TOKEN   = "" <# !!! REQUIRED !!! #>
$env:API_HOST    = "currency-exchange.p.rapidapi.com"
$env:API_URL     = "https://currency-exchange.p.rapidapi.com/exchange"
$env:LIST_CURRENCY  = "EUR,USD,JPY"
<#################################################> 

<# Start python web server #> 
python ./app/server.py