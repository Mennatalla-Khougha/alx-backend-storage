-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

-- creating the trigger and updating the quantity with each order
DELIMITER //

CREATE TRIGGER track_quantity
AFTER INSERT ON orders FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;