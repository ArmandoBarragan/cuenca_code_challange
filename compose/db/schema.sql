\c eight_queens

CREATE TABLE solutions (
    id SERIAL,
    CONSTRAINT solution_pk PRIMARY KEY (id)
);

CREATE TABLE positions (
    id SERIAL,
    x_position INTEGER NOT NULL,
    y_position INTEGER NOT NULL,
    solution_pk INTEGER NOT NULL,

    CONSTRAINT solution_fk FOREIGN KEY (solution_pk)
        REFERENCES solutions ON DELETE CASCADE,
    CONSTRAINT position_pk PRIMARY KEY (id)
);