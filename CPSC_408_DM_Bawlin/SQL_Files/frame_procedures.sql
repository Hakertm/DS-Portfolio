-- Display Frames
DELIMITER $
CREATE PROCEDURE display_frames()
    BEGIN

        -- Select all records from the frames table (specific attributes, see below).
        CREATE OR REPLACE VIEW AllFrames AS
        SELECT frame, gameID, attempt, score, score_type, shot_type, pin_setup, ball_speed
        FROM frames;

        SELECT *
        FROM allframes;

    END $

-- Find Frames
DELIMITER $
CREATE PROCEDURE find_frames(IN gID INT, IN pEmail TEXT)
    BEGIN

        -- Returns all records associated with a specific player and game.
        SELECT frame, gameID, attempt, score, score_type, shot_type, pin_setup, ball_speed
        FROM frames
        WHERE gameID = gID AND playerID = (SELECT playerID
                                           FROM players
                                           WHERE email = pEmail);

    END $

-- Add Frames
DELIMITER $
CREATE PROCEDURE add_frame(IN fNumber INT, IN gID INT, IN pEmail TEXT, IN fAttempt INT,
                           IN fScore INT, IN fScoreT VARCHAR(10), IN fShotT VARCHAR(30),
                           IN fPinSetup VARCHAR(5), IN fBallSpeed DOUBLE)
    BEGIN

        -- Insert a frame record into the frames table.
        INSERT INTO frames VALUES (fNumber,
                                   gID,
                                   (SELECT playerID FROM players WHERE email = pEmail),
                                   fAttempt,
                                   fScore,
                                   fScoreT,
                                   fShotT,
                                   fPinSetup,
                                   fBallSpeed);

    END $
