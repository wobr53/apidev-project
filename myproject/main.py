# nog aanpassen

import os
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import engine, SessionLocal

if not os.path.exists('sqlitedb'):
    os.makedirs('sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
# Start the database, if there is an error -> close it
def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# GET /players/?skip=&limit=
@app.get("/players", response_model=list[schemas.Player])
def read_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):  # async weg
    users = crud.get_players(db=db, skip=skip, limit=limit)
    return users


# POST /players
@app.post("/players", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db_session)):
    db_player = crud.get_player_by_email(db, email=player.email)
    if db_player:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_player(db, player=player)


# GET /player/{username}
@app.get("/players/{username}", response_model=schemas.Player)
def read_player(username: str, db: Session = Depends(get_db_session)):
    db_player = crud.get_player_by_username(db, username=username)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Username not found")
    return db_player


# GET /games/?skip=&limit=
@app.get("/games", response_model=list[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games


# POST /games
@app.get("/games", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db_session)):
    db_game_title = crud.get_game_by_title(db, title=game.title)
    if db_game_title:
        if db_game_title.release_date == game.release_date:
            raise HTTPException(status_code=400, detail="Game already registered")
    return crud.create_game(db, game)


# GET /progress/?skip=&limit=
@app.get("/progress", response_model=list[schemas.Progress])
def read_progress(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_session)):
    progress = crud.get_progress(db, skip=skip, limit=limit)
    return progress


# POST /progress
@app.post("/progress", response_model=schemas.Progress)
def create_progress(progress: schemas.ProgressCreate, db: Session = Depends(get_db_session)):
    db_player = crud.get_player(db, player_id=progress.player_id)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    db_game = crud.get_game(db, game_id=progress.game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    existing_progress = crud.get_progress_by_player_and_game(db, progress.player_id, progress.game_id)
    if existing_progress:
        raise HTTPException(status_code=400, detail="Progress entry already exists")

    return crud.create_progress(db, progress=progress)
