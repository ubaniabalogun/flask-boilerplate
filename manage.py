from flask.ext.script import Manager
from factory import create_app


app = create_app('app','config.DevConfig')

# Initialize Manager
manager = Manager(app)



if __name__ == '__main__':
    manager.run()
