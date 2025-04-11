from fastapi import FastAPI


# Instance
app = FastAPI()


@app.get('/') # decorator
def index():
    return {'data': {'name':'Shreya'}}

@app.get('/about')
def about():
    return {'data': 'about page'}
