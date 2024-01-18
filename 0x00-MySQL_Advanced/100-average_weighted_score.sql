-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(u_id INT)
BEGIN
    DECLARE w_score FLOAT;
    DECLARE t_weight INT;

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
END;
//
DELIMITER ;