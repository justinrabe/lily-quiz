CREATE TABLE answers
(
id INT unsigned NOT NULL AUTO_INCREMENT,
name VARCHAR (255) NOT NULL,
questionID INT NOT NULL,
isCorrect BIT NOT NULL,
addDate DATETIME DEFAULT CURRENT_TIMESTAMP,
updateDate DATETIME ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY(id, questionID)
);
    
CREATE TABLE questions
(
id INT unsigned NOT NULL AUTO_INCREMENT,
question VARCHAR (255) NOT NULL,
addDate DATETIME DEFAULT CURRENT_TIMESTAMP,
updateDate DATETIME ON UPDATE CURRENT_TIMESTAMP,
primary key (ID)
)


INSERT INTO questions (question) VALUES
('Who is the GOAT support?'),
('Who is our fave cowboy hat wearing IT teacher?'),
('fave ramen shop?'),
('Who is Lily''s favorite character in Arcane?')
;
SELECT * FROM questions
INSERT INTO answers 
(name, questionID, isCorrect) VALUES
	('Vandermundo???', 6, 0),
    ('Caitlyn!!', 6, 1),
    ('Vi!!', 6, 0),
    ('Jayce xD', 6, 0)
;
SELECT COUNT(*) FROM questions q


SELECT * FROM answers WHERE questionID = 1

UPDATE answers
SET name = 'August 26 2020'
WHERE ID = 1;
UPDATE answers
SET name = 'July 30 2020'
WHERE ID = 2;
UPDATE answers
SET name = 'September 23 2020'
WHERE ID = 3;
UPDATE answers
SET name = 'May 8 2020'
WHERE ID = 4;

