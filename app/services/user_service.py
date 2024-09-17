from app import mongo
from app.models import user_schema, users_schema

class UserService:
    def get_all_users(self):
        users = mongo.db.users.find()
        return users_schema.dump(users)

    def get_user_by_id(self, user_id):
        user = mongo.db.users.find_one_or_404({"id": user_id})
        return user_schema.dump(user)

    def create_user(self, data):
        user = {
            'id': data['id'],
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }
        mongo.db.users.insert_one(user)
        return user_schema.dump(user)

    def update_user(self, user_id, data):
        mongo.db.users.update_one(
            {'id': user_id},
            {'$set': {
                'name': data['name'],
                'email': data['email'],
                'password': data['password']
            }}
        )
        user = mongo.db.users.find_one_or_404({"id": user_id})
        return user_schema.dump(user)

    def delete_user(self, user_id):
        mongo.db.users.delete_one({'id': user_id})



