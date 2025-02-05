-- Display Games
DELIMITER $
CREATE PROCEDURE display_games()
    BEGIN

        -- Select all records from the games table and player game JT.
        SELECT gameID, final_score, date, location, email
        FROM (SELECT *
              FROM player_game_jt
              INNER JOIN games USING(gameID)) AS PlayerGame
        INNER JOIN players USING (playerID);

    END $

-- Find Games associated with a specific player.
DELIMITER $
CREATE PROCEDURE find_games(IN pEmail TEXT)
    BEGIN

        -- Select all records from the games table and player game JT associated
        -- with a specific email.
        SELECT gameID, final_score, date, location, email
        FROM (SELECT *
              FROM player_game_jt
              INNER JOIN games USING(gameID)) AS PlayerGame
        INNER JOIN players USING (playerID)
        WHERE email = pEmail;

    END $

-- Add a Bowling Game Record
DELIMITER $
CREATE PROCEDURE add_game(IN gScore INT, IN gDate DATE, IN gLoc TEXT, IN pEmail TEXT)
    BEGIN

        -- Insert a record into the games table given the inputs.
        INSERT INTO games VALUES (NULL,
                                  gDate,
                                  gLoc);

        -- Insert the IDs of the game and player into the join table.
        INSERT INTO player_game_jt VALUES ((SELECT playerID
                                            FROM players
                                            WHERE email = pEmail),
                                            LAST_INSERT_ID(),
                                            gScore);


    END $

-- Display all Unique Game Locations
DELIMITER $
CREATE PROCEDURE show_game_locations()
    BEGIN

        -- Return all unique locations games were played at.
        SELECT DISTINCT location
        FROM games;

    END $

-- Add to Player Game JT
DELIMITER $
CREATE PROCEDURE add_final_score(IN pEmail TEXT, IN pScore INT, IN gID INT)
    BEGIN

        -- Insert a record into the player game JT given the inputs.
        INSERT INTO player_game_jt VALUES ((SELECT playerID
                                            FROM players
                                            WHERE email = pEmail),
                                           gID,
                                           pScore);

    END $

-- Show all Games+Player Info for Specific Player
DELIMITER $
CREATE PROCEDURE show_player_games_info(IN pEmail TEXT)
    BEGIN

        -- Select all game information and specific personal information of the input email.
        SELECT email, first_name, last_name, team_name, team_type,
               gameID, final_score, date, location
        FROM games
        INNER JOIN player_game_jt USING (gameID)
        INNER JOIN players USING (playerID)
        INNER JOIN teams USING (team_name)
        WHERE email = pEmail;

    END $
