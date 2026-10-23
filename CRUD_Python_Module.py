
# ============================================================
# CS 340 - Project Two
# Grazioso Salvare Animal Shelter Database
# CRUD Python Module
#
# Author: Demetre Parker
#
# This module provides Create, Read, Update, and Delete
# operations for the Austin Animal Center MongoDB database.
# ============================================================

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId


class AnimalShelter(object):
    """CRUD operations for the AAC animals collection."""

    # --------------------------------------------------------
    # INITIALIZE DATABASE CONNECTION
    # --------------------------------------------------------

    def __init__(self, username, password):
        """
        Connect to the MongoDB database using credentials
        supplied by the dashboard notebook.
        """

        HOST = "localhost"
        PORT = 27017
        DB = "aac"
        COL = "animals"

        try:
            # Connect to MongoDB.
            # The authentication database is admin.
            self.client = MongoClient(
                host=HOST,
                port=PORT,
                username=username,
                password=password,
                authSource="admin",
                serverSelectionTimeoutMS=5000
            )

            # Select the AAC database.
            self.database = self.client[DB]

            # Select the animals collection.
            self.collection = self.database[COL]

            # Verify the database connection.
            self.client.admin.command("ping")

            print("MongoDB connection successful!")

        except PyMongoError as e:
            print("MongoDB connection failed:", e)
            raise

    # --------------------------------------------------------
    # CREATE
    # --------------------------------------------------------

    def create(self, data):
        """
        Insert a new animal document.

        Returns True if successful.
        Returns False if unsuccessful.
        """

        if data is None or not isinstance(data, dict):
            return False

        try:
            self.collection.insert_one(data)
            return True

        except PyMongoError as e:
            print("Error creating animal record:", e)
            return False

    # --------------------------------------------------------
    # READ
    # --------------------------------------------------------

    def read(self, query, projection=None):
        """
        Retrieve animal records matching the query.

        Returns a list of MongoDB documents.
        """

        if query is None or not isinstance(query, dict):
            return []

        try:
            results = self.collection.find(
                query,
                projection
            )

            return list(results)

        except PyMongoError as e:
            print("Error reading animal records:", e)
            return []

    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    def update(self, query, new_values):
        """
        Update animal records matching the query.

        Returns the number of modified documents.
        """

        if (
            query is None
            or new_values is None
            or not isinstance(query, dict)
            or not isinstance(new_values, dict)
        ):
            return 0

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )

            return result.modified_count

        except PyMongoError as e:
            print("Error updating animal records:", e)
            return 0

    # --------------------------------------------------------
    # DELETE
    # --------------------------------------------------------

    def delete(self, query):
        """
        Delete animal records matching the query.

        Returns the number of deleted documents.
        """

        if query is None or not isinstance(query, dict):
            return 0

        try:
            result = self.collection.delete_many(query)

            return result.deleted_count

        except PyMongoError as e:
            print("Error deleting animal records:", e)
            return 0

    # --------------------------------------------------------
    # COUNT
    # --------------------------------------------------------

    def count(self, query=None):
        """
        Count animal records matching the query.

        Returns the number of matching documents.
        """

        if query is None:
            query = {}

        try:
            return self.collection.count_documents(query)

        except PyMongoError as e:
            print("Error counting animal records:", e)
            return 0

    # --------------------------------------------------------
    # CLOSE CONNECTION
    # --------------------------------------------------------

    def close(self):
        """Close the MongoDB connection."""

        self.client.close()
        print("MongoDB connection closed.")
