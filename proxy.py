# Author Joey Whelan
""" FastAPI implementation of an API proxy.  Proxies REST calls into a SOAP service.
"""
from fastapi import FastAPI, HTTPException
from zeep import Client
import logging

logging.getLogger('zeep').setLevel(logging.ERROR)
client = Client('https://www.w3schools.com/xml/tempconvert.asmx?wsdl')
app = FastAPI()

@app.get("/CelsiusToFahrenheit")
async def celsiusToFahrenheit(temp: int): 
    try:
        soapResponse = client.service.CelsiusToFahrenheit(temp)
        fahrenheit = int(round(float(soapResponse),0))
    except:
        raise HTTPException(status_code=400, detail="SOAP request error")
    else:
        return {"temp": fahrenheit}


@app.get("/FahrenheitToCelsius")
async def fahrenheitToCelsius(temp: int): 
    try:
        soapResponse = client.service.FahrenheitToCelsius(temp)
        celsius = int(round(float(soapResponse),0))
    except:
        raise HTTPException(status_code=400, detail="SOAP request error")
    else:
        return {"temp": celsius}