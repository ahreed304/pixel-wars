DROP TABLE IF EXISTS pixel_placement;

CREATE TABLE pixel_placement (
	pixel_placement_id SERIAL UNIQUE PRIMARY KEY,
	timestamp DATETIME NOT NULL,
	user_id VARCHAR NOT NULL,
	pixel_color VARCHAR NOT NULL,
	x INT NOT NULL,
	y INT NOT NULL
);