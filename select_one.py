from main import session 
from models import User

jona = session.query(User).filter_by(username = 'jona').first()
print(jona)