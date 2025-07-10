from flask_pymongo import PyMongo

mongo = PyMongo()

def init_mongo(app):
    app.config["MONGO_URI"] = "mongodb://localhost:27017/your-db-name"
    mongo.init_app(app)
    with app.app_context():
        # Ensure the database is created
        mongo.db  # Accessing the db will create it if it doesn't exist
        print("MongoDB initialized and connected.")