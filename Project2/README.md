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
2. End tour 
3. Open Web Tab 
4. Create new Web App
5. Click Next
6. Click on Flask 
7. IMPORTANT: Python 3.8 
8. rename to app.py
9. Should create your API. 
10. Upload/overwrite the app.py file with our Sublime text file on our computers 
11. Upload the database.JSON file to your file list
12. Hit Save + Refresh
13. 
