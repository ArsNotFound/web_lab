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

COMMIT;

