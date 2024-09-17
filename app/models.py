from app import ma, mongo

# Define the User model as a schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
