# Сериалайзер

* Пример html для красивого сообщения.
```python
class Serializer:

    @staticmethod
    def serialize_event(email_message: Event):
        html = (
            f'''
            <html>
                <body>
                    <h1>{email_message.txt}</h1>
                    <h3>{email_message.desc}</h3>
                </body>
            </html>
        '''
        )
        return html
```

## Полезные ссылки
1. [HTML](http://htmlbook.ru/)