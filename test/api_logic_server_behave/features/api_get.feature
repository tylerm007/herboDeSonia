#this is the api_test.feature
Feature: API GET Testing

  Scenario: GET Cliente Endpoint
    Given GET Cliente endpoint
    When GET Cliente API
    Then Cliente retrieved

  Scenario: GET ComprasCAB Endpoint
    Given GET ComprasCAB endpoint
    When GET ComprasCAB API
    Then ComprasCAB retrieved

  Scenario: GET ComprasLIN Endpoint
    Given GET ComprasLIN endpoint
    When GET ComprasLIN API
    Then ComprasLIN retrieved

  Scenario: GET Producto Endpoint
    Given GET Producto endpoint
    When GET Producto API
    Then Producto retrieved

  Scenario: GET Proveedor Endpoint
    Given GET Proveedor endpoint
    When GET Proveedor API
    Then Proveedor retrieved

  Scenario: GET StockTienda Endpoint
    Given GET StockTienda endpoint
    When GET StockTienda API
    Then StockTienda retrieved

  Scenario: GET Tienda Endpoint
    Given GET Tienda endpoint
    When GET Tienda API
    Then Tienda retrieved

  Scenario: GET TraspasosLIN Endpoint
    Given GET TraspasosLIN endpoint
    When GET TraspasosLIN API
    Then TraspasosLIN retrieved

  Scenario: GET VentasCAB Endpoint
    Given GET VentasCAB endpoint
    When GET VentasCAB API
    Then VentasCAB retrieved

  Scenario: GET VentasLIN Endpoint
    Given GET VentasLIN endpoint
    When GET VentasLIN API
    Then VentasLIN retrieved

