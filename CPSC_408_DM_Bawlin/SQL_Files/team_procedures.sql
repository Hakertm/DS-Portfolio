-- Display Teams
DELIMITER $
CREATE PROCEDURE display_teams()
    BEGIN

        -- Select all records from the teams table.
        SELECT *
        FROM teams;

    END $

-- Find a Team
DELIMITER $
CREATE PROCEDURE find_team(IN teamName VARCHAR(100))
    BEGIN

        -- Select the team of the same input name.
        SELECT *
        FROM teams
        WHERE team_name = teamName;

    END $

-- Filter Teams
DELIMITER $
CREATE PROCEDURE filter_by_type(IN teamType VARCHAR(30))
    BEGIN

        -- Select all teams that are a specific type of team.
        SELECT *
        FROM teams
        WHERE team_type = teamType;

    END $

-- Create a New Team Record
DELIMITER $
CREATE PROCEDURE create_team(IN teamName VARCHAR(100), teamSize INT, teamType VARCHAR(30))
    BEGIN

        -- Insert a record into teams given the inputs.
        INSERT INTO teams VALUES (teamName,
                                  teamSize,
                                  teamType);

    END $

-- Update a Team's Attribute
DELIMITER $
CREATE PROCEDURE update_team_attribute(IN searchName VARCHAR(100),
                                        newName VARCHAR(100),
                                        newSize INT,
                                        newType VARCHAR(30),
                                        val VARCHAR(15))
    BEGIN

        -- Determines which attribute to update given the val input.
        -- Update the team name.
        IF val = 'Update Name' THEN
            UPDATE teams SET team_name = newName WHERE team_name = searchName;

        -- Update the number of players.
        ELSEIF val = 'Update Size' THEN
            UPDATE teams SET num_players = newSize WHERE team_name = searchName;

        -- Update the team type.
        ELSEIF val = 'Update Type' THEN
            UPDATE teams SET team_type = newType WHERE team_name = searchName;
        END IF;

    END $
