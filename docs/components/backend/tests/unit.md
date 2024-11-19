# Юнит-тестирование


* Модульное тестирование, иногда блочное тестирование или юнит-тестирование — процесс в программировании, позволяющий проверить на корректность отдельные модули исходного кода программы, наборы из одного или более программных модулей вместе с соответствующими управляющими данными, процедурами использования и обработки.

---

* Пример взят из сервиса МатМодели, где тестируется прибыль от сторонних организаций.
```python
def test_income_contractors(
    economic_carrier_service, 
    contract_vehicle, 
    get_constant_mock
):
    etc_service: services.EconomicTransportCarrier = economic_carrier_service

    default_id = 1
    etc_service.etc_repo.get_constant = get_constant_mock
    etc_service.etc_repo.get_contract_vehicle.return_value = contract_vehicle
    etc_service._Lpp = 20 # KM
    etc_service.etc_repo.get_hourly_cost_contract_vehicle_from_nomenclature_group.return_value = 3000

    result, im_result = etc_service.get_income_contractors(vehicle_id=default_id, application_id=default_id)

    expected_result = -9400
    assert result == expected_result, f'''
        Фактический - {result}
        Ожидаемый - {expected_result}

        Промежуточный результат = {im_result}
    '''
```


---

## Полезные ссылки
1. [Python MOCK](https://docs.python.org/3/library/unittest.mock.html)
2. [pytest documentation](https://docs.pytest.org/_/downloads/en/stable/pdf/)
3. [unittest documentation](https://docs.python.org/3/library/unittest.html)