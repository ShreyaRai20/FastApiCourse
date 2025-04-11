from fastapi import FastAPI


# Instance
app = FastAPI()


@app.get('/') # pathOperationDecorator.operation(path/route)
def index(): # path operation function
    return {'data': {'name':'Shreya'}}

@app.get('/about')
def about():
    return {'data': 'about page'}
