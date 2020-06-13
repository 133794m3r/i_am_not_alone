import os
DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#not used right now.
CSRF_ENABLED    = True
#Same here for session cookies.
SECRET_KEY = os.getenv("SECRET_KEY")
SESSION_TYPE="filesystem"
SECRET=os.getenv("SECRET")
MONGO_URI="mongodb+srv://{0}:{1}@mlh-summer-hacks-dqi2z.gcp.mongodb.net/geo_ip_data?retryWrites=true&w=majority".format(os.getenv('mdb_user'),os.getenv('mdb_pass'))