# Redshift-As-A-Service

I've been implementing for Service based architecture recently and I wanted to make a model version of Redshift as a service.  The idea is to allow other services to interact with a big data repo.  This can be for either storage within a service, or integration between services.

A client service requests RAAS to create a space for it in the staging area and gets back an id associated with this space.  The client can then specify what should happen to this data in the form of SQL queries and instruct RAAS when their is new data to process.  The interchange takes place over REST for simplicity

## Useage

To request a new space, make a REST POST call to "/".  In the body of the request, specify the columns you want the space to have.  This should be an array of arrays, where the first column of an array is a column name and the second column if the type.  E.g.

```
{
	"cols": [
      	["id", "int"]
     ]
}
```

You can also specify continuations at this step by adding a continuation key to the json (see below)

The request will return something like:

```
{
"schema": "Tests",
"status": "Success",
"table_name": "GIuYPHToK"
}
```

Where the table_name value is the id of your new space in the staging area

### Continuations

To add a continuation, send a post request to "/continuation" with a body something like:

```
{
	"table_name": "GIuYPHToK",
  "continuations": 
  [
      	"TRUNCATE TABLE Tests.GIuYPHToK"
  ]
}
```

Note that this adds all of the queries in the continuations key rather than replaces the existing continuations.

### Triggers

When you have updated data in the staging area and want to trigger the continuations, you can trigger the query execution by sending a post request to "/trigger/<<TABLE_NAME>>.  So in our example you would POST to "/trigger/GIuYPHToK".  This will run all of the continuations in turn and return the overall status code.  In our example, the staging area table will be truncated



