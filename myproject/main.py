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
    players = crud.get_players(db=db, skip=skip, limit=limit)
    return players


# POST /players
@app.post("/players", response_model=schemas.Player)
def create_player(player: schemas.PlayerCreate, db: Session = Depends(get_db_session)):
    db_player_email = crud.get_player_by_email(db, email=player.email)
    if db_player_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_player_username = crud.get_player_by_username(db, username=player.username)
    if db_player_username:
        raise HTTPException(status_code=400, detail="Username already registered")
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
@app.post("/games", response_model=schemas.Game)
def create_game(game: schemas.GameCreate, db: Session = Depends(get_db_session)):
    db_game_title = crud.get_game_by_title(db, title=game.title)
    if db_game_title is not None:
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


# PUT /progress
# @app.put("/progress", response_model=schemas.Progress)
# def update_progress(progress: schemas.ProgressCreate, db: Session = Depends(get_db_session)):
#     db_player = crud.get_player(db, player_id=progress.player_id)
#     if db_player is None:
#         raise HTTPException(status_code=404, detail="Player not found")
#
#     db_game = crud.get_game(db, game_id=progress.game_id)
#     if db_game is None:
#         raise HTTPException(status_code=404, detail="Game not found")
#
#     # existing_progress = crud.get_progress_by_player_and_game(db, progress.player_id, progress.game_id)
#     # if existing_progress:
#     #     raise HTTPException(status_code=400, detail="Progress entry already exists")
#
#     return crud.create_progress(db, progress=progress)


# DELETE /progress/?player=&game=
@app.delete("/progress/")
def delete_progress(player: int = -1, game: int = -1, db: Session = Depends(get_db_session)):
    db_player = crud.get_player(db, player_id=player)
    if db_player is None:
        raise HTTPException(status_code=404, detail="Player not found")

    db_game = crud.get_game(db, game_id=game)
    if db_game is None:
        raise HTTPException(status_code=404, detail="Game not found")

    db_progress = crud.get_progress_by_player_and_game(db, player, game)
    if db_progress is None:
        raise HTTPException(status_code=404, detail="Progress entry not found")

    crud.delete_progress(db, player, game)
    return {"detail": "Progress of player " + str(player) + " in game " + str(game) + " has been deleted."}


# DELETE /restart
@app.delete("/reset/")
def delete_all(db: Session = Depends(get_db_session)):
    crud.delete_all(db)
    return {"detail": "Reset successful, all data has been wiped."}
