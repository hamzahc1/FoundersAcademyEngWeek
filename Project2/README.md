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
