from demo_project.application.dto import Event


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
