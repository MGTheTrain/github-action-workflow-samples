# To leverage the functionalities offered by the common-lib pip package, access the 'Setup' view for it in CloudSmith and perform the following steps:
# 0. pip install --index-url=<> common-lib==0.1.0.dev9
# 1. Run the python app with `python utilize-common-lib-app.py`

# In order to remove the pip package from the filesystem
# 0. pip uninstall common-lib

from datetime import datetime
from domain.models.user import User

def valid_user():
    return User(
        userId="123",
        userName="ValidUserName123",
        userPassword="StrongPassword123!?§$%",
        email="test@example.com",
        dateTimeCreated=datetime.now(),
        dateTimeUpdated=datetime.now()
    )

def log_user_attributes(user):
    print("User Attributes:")
    print(f"User ID: {user.userId}")
    print(f"User Name: {user.userName}")
    print(f"User Password: {user.userPassword}")
    print(f"Email: {user.email}")
    print(f"Date Time Created: {user.dateTimeCreated}")
    print(f"Date Time Updated: {user.dateTimeUpdated}")

user = valid_user()
log_user_attributes(user)
