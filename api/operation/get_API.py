from typing import Union
import requests

from fastapi import FastAPI

app = FastAPI()


@app.get("/densidad-demografica")
def read_root():
    getAllContries = consumeCountriesRest()
    
    countriesFormated = filterDataContries(getAllContries)
    
    return top5populationDensity(countriesFormated)


def consumeCountriesRest():
    return requests.get('https://restcountries.com/v3.1/all').json()


def filterDataContries(countries):
    countriesFormated = []
    
    for i in countries:
        country = {}
        country['name'] = i['name']['common']
        country['area'] = i['area']
        country['population'] = i['population']
        country['populationDensity'] = country['population'] / country['area']
        
        countriesFormated.append(country)
        
    return countriesFormated
        

def top5populationDensity(countries):
    contriesSort = sorted(countries, key=lambda x: x['populationDensity'], reverse=True)
    return contriesSort[:5]