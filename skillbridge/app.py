import os
from flask import Flask
import db
from routes import facultyroute, department_route, project_route, ratingroute, studentroute, notification_route,user_role_route, transact_route, skillexchnageroute, skillsroute, user_skill_route
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


app.register_blueprint(facultyroute.faculty_endpoint, url_prefix='/api/faculties')
app.register_blueprint(department_route.department_endpoint, url_prefix='/api/departments')
app.register_blueprint(project_route.project_endpoint, url_prefix='/api/projects')
app.register_blueprint(ratingroute.rating_endpoint, url_prefix='/api/ratings')
app.register_blueprint(studentroute.student_endpoint, url_prefix='/api/students')
app.register_blueprint(notification_route.notification_service_endpoint, url_prefix='/api/notification')
app.register_blueprint(user_role_route.user_role_endpoint, url_prefix='/api/user_role')
app.register_blueprint(transact_route.transaction_endpoint, url_prefix='/api/transaction')
app.register_blueprint(skillexchnageroute.skill_exchange_endpoint, url_prefix='/api/skillexchange')
app.register_blueprint(skillsroute.skills_endpoint, url_prefix='/api/skill')
app.register_blueprint(user_skill_route.user_skill_endpoint, url_prefix='/api/userskill')
if __name__ == "__main__":
    app.run()
