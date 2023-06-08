from blog import app,db
from blog.models import User,Post

app.app_context().push()
db.create_all()
# db.drop_all()



