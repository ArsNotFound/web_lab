BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 0a2195c73602

CREATE TABLE neural_category (
    id SERIAL NOT NULL, 
    name VARCHAR NOT NULL, 
    PRIMARY KEY (id)
);

CREATE TABLE neural (
    slug VARCHAR(128) NOT NULL, 
    name VARCHAR(255) NOT NULL, 
    category_id INTEGER NOT NULL, 
    img VARCHAR NOT NULL, 
    tasks VARCHAR NOT NULL, 
    field VARCHAR NOT NULL, 
    short_desc VARCHAR NOT NULL, 
    "desc" VARCHAR NOT NULL, 
    url VARCHAR NOT NULL, 
    PRIMARY KEY (slug), 
    FOREIGN KEY(category_id) REFERENCES neural_category (id), 
    UNIQUE (name)
);

INSERT INTO alembic_version (version_num) VALUES ('0a2195c73602') RETURNING alembic_version.version_num;

-- Running upgrade 0a2195c73602 -> 2361cb0b8cb0

CREATE TABLE news (
    id SERIAL NOT NULL, 
    name VARCHAR NOT NULL, 
    text VARCHAR NOT NULL, 
    img VARCHAR NOT NULL, 
    PRIMARY KEY (id)
);

UPDATE alembic_version SET version_num='2361cb0b8cb0' WHERE alembic_version.version_num = '0a2195c73602';

-- Running upgrade 2361cb0b8cb0 -> fb80a3f3cd0e

CREATE TABLE "user" (
    id SERIAL NOT NULL, 
    login VARCHAR NOT NULL, 
    password_hash BYTEA NOT NULL, 
    email VARCHAR NOT NULL, 
    PRIMARY KEY (id), 
    UNIQUE (email), 
    UNIQUE (login)
);

UPDATE alembic_version SET version_num='fb80a3f3cd0e' WHERE alembic_version.version_num = '2361cb0b8cb0';

COMMIT;

