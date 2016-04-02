from factory import create_app, register_blueprints



app = create_app('app','config.DevConfig')
with app.app_context():
    pass

if __name__ == '__main__':
    app.run()
