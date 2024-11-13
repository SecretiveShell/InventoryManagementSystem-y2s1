@app.post("/api/authors", response_model=AuthorResponse)
def create_author(author: AuthorCreate):
    with Session() as session:
        db_author = Author(**author.dict())
        session.add(db_author)
        session.commit()
        session.refresh(db_author)
        return db_author

@app.get("/api/authors", response_model=list[AuthorResponse])
def get_authors():
    with Session() as session:
        authors = session.query(Author).all()
        return authors

@app.get("/api/authors/{author_id}", response_model=AuthorResponse)
def get_author(author_id: int):
    with Session() as session:
        author = session.query(Author).filter(Author.author_id == author_id).first()
        if author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        return author

@app.put("/api/authors/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author: AuthorCreate):
    with Session() as session:
        db_author = session.query(Author).filter(Author.author_id == author_id).first()
        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        for key, value in author.dict().items():
            setattr(db_author, key, value)
        session.commit()
        session.refresh(db_author)
        return db_author

@app.delete("/api/authors/{author_id}")
def delete_author(author_id: int):
    with Session() as session:
        db_author = session.query(Author).filter(Author.author_id == author_id).first()
        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        session.delete(db_author)
        session.commit()
        return {"detail": "Author deleted successfully"}