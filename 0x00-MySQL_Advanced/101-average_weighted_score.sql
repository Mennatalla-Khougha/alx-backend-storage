-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE w_score FLOAT;
    DECLARE t_weight INT;
    DECLARE u_id INT;

    DECLARE user_c CURSOR FOR SELECT id FROM users;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET u_id = NULL;

    OPEN user_c;

    user_loop: LOOP 
        FETCH user_c INTO u_id;

        IF u_id IS NULL THEN 
            LEAVE user_loop;
        END IF;

        SELECT SUM(corrections.score * projects.weight),
                SUM(projects.weight)
        INTO 
            w_score,
            t_weight
        FROM corrections 
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = u_id;

        IF t_weight > 0 THEN
            UPDATE users
            SET average_score = w_score / t_weight
            WHERE id = u_id;
        END IF;
    END LOOP;
    CLOSE user_c;
END;
//
DELIMITER ;