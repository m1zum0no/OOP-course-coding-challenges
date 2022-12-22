class Application:

    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

class AppStore:

    apps = []

    def add_application(self, app):
        self.apps.append(app)

    def remove_application(self, app):
        self.apps.pop(self.apps.index(app))

    def block_application(self, app):
        app.blocked = True

    def total_apps(self):
        return len(self.apps)
