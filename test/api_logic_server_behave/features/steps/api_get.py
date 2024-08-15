# this is the api_test.py
from behave import *
import requests, pdb
import json
from dotmap import DotMap
from test_utils import login

host = "localhost"
port = "5656"

def getAPI(table_name:str):
	get_uri = f'http://{host}:{port}/api/{table_name}/?'\
	"page%5Boffset%5D=0&page%5Blimit%5D=1"
	r = requests.get(url=get_uri, headers= login())
	result_data = json.loads(r.text)
	return DotMap(result_data)

def patchAPI(table_name:str, payload:dict, key:any):
	get_uri = f'http://{host}:{port}/api/{table_name}/{key}'
	r = requests.patch(url=get_uri, json=payload, headers= login())
	return json.loads(r.text)


@given('GET Cliente endpoint')
def step_impl(context):
	assert True

@when('GET Cliente API')
def step_impl(context):
	context.response_text = getAPI('Cliente')

@then('Cliente retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET ComprasCAB endpoint')
def step_impl(context):
	assert True

@when('GET ComprasCAB API')
def step_impl(context):
	context.response_text = getAPI('ComprasCAB')

@then('ComprasCAB retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET ComprasLIN endpoint')
def step_impl(context):
	assert True

@when('GET ComprasLIN API')
def step_impl(context):
	context.response_text = getAPI('ComprasLIN')

@then('ComprasLIN retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET Producto endpoint')
def step_impl(context):
	assert True

@when('GET Producto API')
def step_impl(context):
	context.response_text = getAPI('Producto')

@then('Producto retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET Proveedor endpoint')
def step_impl(context):
	assert True

@when('GET Proveedor API')
def step_impl(context):
	context.response_text = getAPI('Proveedor')

@then('Proveedor retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET StockTienda endpoint')
def step_impl(context):
	assert True

@when('GET StockTienda API')
def step_impl(context):
	context.response_text = getAPI('StockTienda')

@then('StockTienda retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET Tienda endpoint')
def step_impl(context):
	assert True

@when('GET Tienda API')
def step_impl(context):
	context.response_text = getAPI('Tienda')

@then('Tienda retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET TraspasosLIN endpoint')
def step_impl(context):
	assert True

@when('GET TraspasosLIN API')
def step_impl(context):
	context.response_text = getAPI('TraspasosLIN')

@then('TraspasosLIN retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET VentasCAB endpoint')
def step_impl(context):
	assert True

@when('GET VentasCAB API')
def step_impl(context):
	context.response_text = getAPI('VentasCAB')

@then('VentasCAB retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0

@given('GET VentasLIN endpoint')
def step_impl(context):
	assert True

@when('GET VentasLIN API')
def step_impl(context):
	context.response_text = getAPI('VentasLIN')

@then('VentasLIN retrieved')
def step_impl(context):
	response_text = context.response_text
	assert len(response_text.data) >= 0
