-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN u_id INT
)
BEGIN
    DECLARE average FLOAT;

    SELECT AVG(score) INTO average
    FROM corrections WHERE user_id = u_id;

    UPDATE users 
    SET average_score = average
    WHERE id = u_id;
END;
//
DELIMITER ;
