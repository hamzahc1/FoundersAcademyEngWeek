from flask import Flask, request, jsonify
from uuid import uuid4
import json
from datetime import datetime

# Names the app as the filename
app = Flask(__name__)

def load_db():
	with open("database.JSON", "r") as f:
		database = json.load(f)
	return database

def save_db(database):
	with open("database.JSON", "w") as f:
		json.dump(database, f, indent=4)

@app.route("/diaryentry", methods=["POST"])
def create_diary_entry ():
	data = json.loads(request.data)
	db = load_db()

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


@app.route("/diaryentry/<entryid>", methods=["GET"])
def get_diary_entry (entryid):
	db = load_db()
	data = db.get(entryid)
	if data is None:
		return jsonify({'message': f'Cannot find diary entry with id {entryid}'}), 404
	return jsonify({'message':'Successfully got entry', 'data': data, 'id':entryid}), 200


@app.route("/diaryentry", methods=["GET"])
def get_all_diary_entries():
	db = load_db()
	n_entries = len(db)
	response = {
		'message': 'Successfully got diary entries',
		'count': n_entries,
		'entries': data,
	}
	return jsonify(response), 200