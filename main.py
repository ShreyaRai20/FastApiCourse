from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


# Instance
app = FastAPI()

# published: bool - returns string so need to specify this


@app.get('/blog') # pathOperationDecorator.operation(path/route)
def index(limit=10, published: bool=True, sort: Optional[str]=None): # path operation function
    # Only get 10 published bogs
    if published:
        return {'data': f'{limit} blogs from the db'}
    else:
        return {'data': f'published false'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comments with blog with id = id
    return {'data': ['1','2', limit]}


class Blog(BaseModel):
    id: int
    title: str
    body: str
    published_at: Optional[bool] = True


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'published blog with {blog.title}'}