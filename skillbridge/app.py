import os
from flask import Flask
import db
from routes import facultyroute
from flasgger import Swagger


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'skillbridge.db'),
        DEBUG=True
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    return app


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Skillbridge API by DevThrive'24",
        "description": "API for Skillbridge",
        "contact": {
            "responsibleOrganization": "Skillbridge",
            "responsibleDeveloper": "Your Name",
            "email": "info@skillbridge.com",
            "url": "www.skillbridge.com",
        },
        "termsOfService": "www.skillbridge.com/terms/",
        "version": "0.0.1"
    },
    "host": "localhost:5000",  # overrides localhost:500
    "basePath": "/api",  # base bash for blueprint registration
    "schemes": [
        "http",
    ],
    "operationId": "getmyData"
}
app = create_app()
swagger = Swagger(app, template=swagger_template)


@app.route('/')
def hello():
    return 'Hello, World!'


app.register_blueprint(facultyroute.api, url_prefix='/api/faculties')
if __name__ == "__main__":
    app.run()
