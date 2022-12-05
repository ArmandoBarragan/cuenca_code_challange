\c eight_queens

CREATE TABLE solutions (
    id SERIAL PRIMARY KEY,
    table_size INTEGER NOT NULL
);

CREATE TABLE positions (
    id SERIAL PRIMARY KEY ,
    x_position INTEGER NOT NULL,
    y_position INTEGER NOT NULL,
    solution_pk INTEGER NOT NULL,

    CONSTRAINT solution_fk FOREIGN KEY (solution_pk)
        REFERENCES solutions ON DELETE CASCADE
);