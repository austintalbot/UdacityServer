import sys
activate_this = '/home/myapp/UdacityServer/env/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

sys.path.insert(0, "/home/myapp/UdacityServer")

from main import app as application
application.secret_key = ''.join(random.choice(
        string.ascii_uppercase + string.digits)for x in list(range(32)))
