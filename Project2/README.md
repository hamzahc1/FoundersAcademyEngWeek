# Project 2 - Python Data API 

This project is focused on building a data API in Python. This service will allow us to create, retrieve and delete posts for our journal. 

## Docs

### Get an entry

Get the details of a specific journal entry, given the *entryid*

**URL** : `/diaryentry/<entryid>`

**Method** : `GET`

### Get all entries

Get the details of all journal entries

**URL** : `/diaryentry`

**Method** : `GET`

### Create a new entry

Create a new diary entry in our journal

**URL** : `/diaryentry`

**Method** : `POST`

Provide details of entry to be created.

```json
{
    "title": "string",
    "description": "string"
}
```


## Deployment

We will deploy our API using pythonanywhere.com, which will allow us to easily expose our API to the public. 

Steps:
1. Sign up for an account with your email at https://www.pythonanywhere.com/registration/register/beginner/
2. Click on "End Tour"
3. Once you're in the main screen, click on the **Web** tab 
4. Click on Create new web app 
5. Click on Next
6. Select **Flask**
7. IMPORTANT: Select Python 3.8 
8. Rename the file to **app.py**
9. You should now have a basic Flask API setup! 
10. Upload/overwrite the app.py file with our Sublime text files from our computers 
11. Upload the database.JSON file to your file list
12. Hit Save + Click the little refresh button
13. Test the API!!!
14. Create a Bash Console from the Pythonanywhere page (Way to interact with a computer through typing)
15. Create a virtual environment using: `mkvirtualenv venv --python=/usr/bin/python3.8`
16. Once you're in your virtual environment, run `pip install flask-cors`
17. Update your virtualenv in the **Web** tab as `/home/{username}/.virtualenvs/venv` 
18. Uncomment the lines related to CORS in app.py
19. Save, Refresh and then reload web app 
20. Test the API! You're done!
