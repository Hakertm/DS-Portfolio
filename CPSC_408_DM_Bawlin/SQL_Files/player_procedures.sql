-- Display Players
DELIMITER $
CREATE PROCEDURE display_players()
    BEGIN

        -- Select all records from the players table.
        SELECT team_name, first_name, last_name, email
        FROM players;

    END $

-- Find Player
DELIMITER $
CREATE PROCEDURE find_player(IN pEmail TEXT)
    BEGIN

        -- Select the player record of the input email.
        SELECT team_name, first_name, last_name, email
        FROM players
        WHERE email = pEmail;

    END $

-- Delete Player
DELIMITER $
CREATE PROCEDURE  delete_player(IN pEmail TEXT)
    BEGIN

        -- Delete the player of the input email. NOTE: Deletes records associated
        -- with this player across all other tables due to CASCADE DELETE.
        DELETE FROM players WHERE email = pEmail;

    END $

-- Add Player
DELIMITER $
CREATE PROCEDURE add_player(IN teamName VARCHAR(100),
                            firstName TEXT,
                            lastName TEXT,
                            pEmail TEXT)

    BEGIN

        -- Insert a record into players given the inputs.
        INSERT INTO players VALUES (NULL,
                                    teamName,
                                    firstName,
                                    lastName,
                                    pEmail);

    END $

-- Update Player Attribute
DELIMITER $
CREATE PROCEDURE update_player_attribute(IN searchEmail TEXT,
                                        teamName VARCHAR(100),
                                        firstName TEXT,
                                        lastName TEXT,
                                        pEmail TEXT,
                                        val VARCHAR(30))

    BEGIN

        -- Determines which attribute to update given the val input.
        -- Update the team name.
        IF val = 'Update Team Name' THEN
            UPDATE players SET team_name = teamName WHERE email = searchEmail;

        -- Update the first name.
        ELSEIF val = 'Update First Name' THEN
            UPDATE players SET first_name = firstName WHERE email = searchEmail;

        -- Update the last name.
        ELSEIF val = 'Update Last Name' THEN
            UPDATE players SET last_name = lastName WHERE email = searchEmail;

        -- Update the email.
        ELSEIF val = 'Update Email' THEN
            UPDATE players SET email = pEmail WHERE email = searchEmail;
        END IF;

    END $

-- Aggregate Operations
-- Count of Each Score Type
DELIMITER $
CREATE PROCEDURE count_player_score_type(IN pEmail TEXT)
    BEGIN

        -- Get the count of each score type for a specific player.
        SELECT score_type, COUNT(score_type) as ScoreTypeCount
        FROM (SELECT playerID, score_type
              FROM frames
              INNER JOIN players USING (playerID)) as PlayerFrames
              WHERE playerID = (SELECT playerID
                                FROM players
                                WHERE email = pEmail)
        GROUP BY score_type;

    END $

-- Count of Each Shot Type
DELIMITER $
CREATE PROCEDURE count_player_shot_type(IN pEmail TEXT)
    BEGIN

        -- Get the count of each shot type for a specific player.
        SELECT shot_type, COUNT(shot_type) as ScoreTypeCount
        FROM (SELECT playerID, shot_type
              FROM frames
              INNER JOIN players USING (playerID)) as PlayerFrames
              WHERE playerID = (SELECT playerID
                                FROM players
                                WHERE email = pEmail)
        GROUP BY shot_type;

    END $

-- Average Score
DELIMITER $
CREATE PROCEDURE average_player_score(IN pEmail TEXT)
    BEGIN

        -- Get the average final score for a specific player.
        SELECT ROUND(AVG(final_score), 2) as AvgScore
        FROM player_game_jt
        WHERE playerID = (SELECT playerID
                          FROM players
                          WHERE email = pEmail);

    END $
