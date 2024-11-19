# Интеграционное тестирование


* Интеграцио́нное тести́рование  — одна из фаз тестирования программного обеспечения, при которой отдельные программные модули объединяются и тестируются в группе. Обычно интеграционное тестирование проводится после модульного тестирования и предшествует системному тестированию.


---
* Для интеграционного тестирования разворачивается своя база данных в
памяти компьютера. Далее происходит наполнение тестовыми данными.
* (Пример взят из мат.модели)
```python
@pytest.fixture(scope='session')
def engine(): 
    engine = create_engine('sqlite://')
    for key, value in SQLModel.metadata.tables.items():
        value.schema = None
    SQLModel.metadata.create_all(engine)

    emulate_migration = TransactionContext(bind=engine)

    emulate_migration_session = emulate_migration.current_session
    emulate_migration_session.commit()

    weep = WEEP(context=emulate_migration)
    weep.start()

    return engine
```

---
## Полезные ссылки
1. [Python MOCK](https://docs.python.org/3/library/unittest.mock.html)
2. [Интеграционное тестирование](https://habr.com/ru/articles/556002/)
3. [pytest documentation](https://docs.pytest.org/_/downloads/en/stable/pdf/)