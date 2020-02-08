# These are libraries we need to use in our code, so we import them before we get started
from flask import Flask, request, jsonify
# from flask_cors import CORS

from uuid import uuid4
import json
from datetime import datetime

# Names the app as the filename
app = Flask(__name__)
# CORS(app)


# This function loads the database file into our working "memory"
def load_db():
# With this line we're saying we want to open the database.JSON file and make it available. We then decode the JSON file so we can use it in our python code.
	with open("mysite/database.JSON", "r") as f:
		database = json.load(f)
	return database

# This function saves our changes to the database file
def save_db(database):
# With this line, we're saving our database variable (an input to the save_db function) and then turn it into JSON format before overwriting our database to save it with the new data!
	with open("mysite/database.JSON", "w") as f:
		json.dump(database, f, indent=4)

# This creates our first API endpoint, which is a POST endpoint. A POST endpoint is used when you want to create a new entry. We are "posting" our new entry to the database to be stored. 

# This line defines our API endpoint, also know as the URL we will need to call when we want to invoke this endpoint in our own application
@app.route("/diaryentry", methods=["POST"])
# @cross_origin()
def create_diary_entry ():
	data = json.loads(request.data)
	db = load_db()

# The line below generates a random unique ID for our new entry to ensure it isn't duplicated.
	unique_id = str(uuid4())
	db[unique_id] = data
	db[unique_id]["createdat"] = str(datetime.now())
	save_db(db)

	response = {
		'message': 'Entry created!',
		'data': data,
		'id': unique_id
	}
	return jsonify(response), 201

# This creates a GET API endpoint. A GET endpoint is used when you want to retrieve a stored entry, we are "getting" something from the database. You typically need to give some unique identifier to retrieve the specific thing you want, in our case, this will be the unique id of our entry.
@app.route("/diaryentry/<entryid>", methods=["GET"])
# @cross_origin()
def get_diary_entry (entryid):
	db = load_db()
	data = db.get(entryid)
	success_response = {
		'message': 'Successfully got entry', 
		'data': data, 
		'id':entryid
	}
	if data is None:
		return jsonify({'message': f'Cannot find diary entry with id {entryid}'}), 404
	return jsonify(success_response), 200


# This endpoint is for when we retrieve all the items in our database. 
@app.route("/diaryentry", methods=["GET"])
# @cross_origin()
def get_all_diary_entries():
	db = load_db()
	n_entries = len(db)
	response = {
		'message': 'Successfully got diary entries',
		'count': n_entries,
		'entries': db,
	}
	return jsonify(response), 200

# Can you figure out how to make an endpoint that deletes a post...? 
