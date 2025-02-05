-- Display Bowling Balls
DELIMITER $
CREATE PROCEDURE display_balls()
    BEGIN

        -- Select all records from the bowling balls table and the player's
        -- email associated with it.
        SELECT color, weight, coverstock, core, email
        FROM (SELECT playerID, color, weight, coverstock, core
              FROM player_ball_jt
              INNER JOIN bowling_balls USING (bID)) AS PlayerBall
        INNER JOIN players USING (playerID);

    END $

-- Find Bowling Ball(s) associated with a specific player
DELIMITER $
CREATE PROCEDURE find_bowling_ball(IN pEmail TEXT)
    BEGIN

        -- Select the record(s) of bowling balls associated with a specific email.
        SELECT color, weight, coverstock, core, email
        FROM (SELECT playerID, color, weight, coverstock, core
              FROM player_ball_jt
              INNER JOIN bowling_balls USING (bID)) AS PlayerBall
        INNER JOIN players USING (playerID)
        WHERE email = pEmail;

    END $

-- Filter Bowling Balls by Coverstock
DELIMITER $
CREATE PROCEDURE filter_ball_by_cover(IN cover VARCHAR(20))
    BEGIN

        -- Select all records from the bowling balls table of a specific coverstock.
        SELECT color, weight, coverstock, core, email
        FROM (SELECT playerID, color, weight, coverstock, core
              FROM player_ball_jt
              INNER JOIN bowling_balls USING (bID)) AS PlayerBall
        INNER JOIN players USING (playerID)
        WHERE coverstock = cover;

    END $

-- Filter Bowling Balls by Core Type
DELIMITER $
CREATE PROCEDURE filter_ball_by_core(IN bCore VARCHAR(20))
    BEGIN

        -- Select all records from the bowling balls table of a specific core.
        SELECT color, weight, coverstock, core, email
        FROM (SELECT playerID, color, weight, coverstock, core
              FROM player_ball_jt
              INNER JOIN bowling_balls USING (bID)) AS PlayerBall
        INNER JOIN players USING (playerID)
        WHERE core = bCore;

    END $

-- Add a Bowling Ball
DELIMITER $
CREATE PROCEDURE add_ball(IN bColor VARCHAR(30),
                          bWeight INT,
                          bCover VARCHAR(20),
                          bCore VARCHAR(20),
                          pEmail TEXT)

    BEGIN

        -- Insert a record into the bowling balls table given the inputs.
        INSERT INTO bowling_balls VALUES (NULL,
                                          bColor,
                                          bWeight,
                                          bCover,
                                          bCore);

        -- Insert the IDs of the ball and player into the join table.
        INSERT INTO player_ball_jt VALUES ((SELECT playerID
                                            FROM players
                                            WHERE email = pEmail),
                                            LAST_INSERT_ID());

    END $

-- Sort by Weight (asc or desc)
DELIMITER $
CREATE PROCEDURE sort_by_ball_weight(IN asc_or_desc VARCHAR(20))
    BEGIN

        -- Return records sorted by ascending weight.
        IF asc_or_desc = 'Ascending' THEN
            SELECT color, weight, coverstock, core, email
            FROM (SELECT playerID, color, weight, coverstock, core
                  FROM player_ball_jt
                  INNER JOIN bowling_balls USING (bID)) AS PlayerBall
            INNER JOIN players USING (playerID)
            ORDER BY weight ASC;

        -- Return records sorted by descending weight.
        ELSEIF asc_or_desc = 'Descending' THEN
            SELECT color, weight, coverstock, core, email
            FROM (SELECT playerID, color, weight, coverstock, core
                  FROM player_ball_jt
                  INNER JOIN bowling_balls USING (bID)) AS PlayerBall
            INNER JOIN players USING (playerID)
            ORDER BY weight DESC;
        END IF;

    END $
