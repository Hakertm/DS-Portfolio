-- Create the Bowling database. Run only once.
CREATE DATABASE bowling;

-- Teams Table
CREATE TABLE teams(
    team_name VARCHAR(100) PRIMARY KEY NOT NULL,
    num_players INT NOT NULL,
    team_type VARCHAR(30));

-- Players Table
CREATE TABLE players(
    playerID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    team_name VARCHAR(100) NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email TEXT NOT NULL,
    FOREIGN KEY (team_name) REFERENCES teams(team_name) ON UPDATE CASCADE);

-- Bowling Ball Table
CREATE TABLE bowling_balls(
    bID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    color VARCHAR(30) NOT NULL,
    weight INT NOT NULL,
    coverstock VARCHAR(20),
    core VARCHAR(20));

-- Player and Bowling Ball Join Table
CREATE TABLE player_ball_JT(
    playerID INT NOT NULL,
    bID INT NOT NULL,
    PRIMARY KEY (playerID, bID),
    FOREIGN KEY (playerID) REFERENCES players(playerID) ON DELETE CASCADE,
    FOREIGN KEY (bID) REFERENCES bowling_balls(bID) ON DELETE CASCADE);

-- Bowling Games Table
CREATE TABLE games(
    gameID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    date DATE,
    location TEXT);

-- Player and Bowling Games Join Table
CREATE TABLE player_game_JT(
    playerID INT NOT NULL,
    gameID INT NOT NULL,
    final_score INT NOT NULL,
    PRIMARY KEY (playerID, gameID),
    FOREIGN KEY (playerID) REFERENCES players(playerID) ON DELETE CASCADE,
    FOREIGN KEY (gameID) REFERENCES games(gameID) ON DELETE CASCADE);

-- Frames Table
CREATE TABLE frames(
    frame INT NOT NULL,
    gameID INT NOT NULL,
    playerID INT NOT NULL,
    attempt INT NOT NULL,
    score INT NOT NULL,
    score_type VARCHAR(10) NOT NULL,
    shot_type VARCHAR(30) NOT NULL,
    pin_setup VARCHAR(5) NOT NULL,
    ball_speed REAL,
    PRIMARY KEY (frame, gameID, playerID, attempt),
    FOREIGN KEY (gameID) REFERENCES games(gameID) ON DELETE CASCADE,
    FOREIGN KEY (playerID) REFERENCES players(playerID) ON DELETE CASCADE);
