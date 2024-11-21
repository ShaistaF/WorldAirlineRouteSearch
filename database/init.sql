CREATE DATABASE aeropath;
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR(100),
    destination VARCHAR(100),
    route JSONB,
    distance VARCHAR(50)
);
