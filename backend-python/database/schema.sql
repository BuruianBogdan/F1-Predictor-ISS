CREATE TABLE seasons(
    season_year integer primary key
);

create table drivers(
    driver_id integer primary key AUTOINCREMENT,
    driver_ref text unique ,
    number integer,
    code text,
    forname text,
    surname text,
    dob date,
    nationality text
);

create table constructors(
    constructor_id integer primary key AUTOINCREMENT,
    constructor_ref text unique ,
    name text,
    nationality text,
);

create table circuits(
    circuit_id integer primary key AUTOINCREMENT,
    circuit_ref text unique,
    name text,
    location text,
    country text,
    lat real,
    lng real
);

create table races(
    race_id integer primary key AUTOINCREMENT,
    seazon_year integer,
    round integer,
    circuit_id integer,
    race_name text,
    date date,
    is_completed integer default 0
);

create table race_results(
    results_id integer primary key AUTOINCREMENT,
    race_id integer,
    driver_id integer,
    constructor_id integer,
    grid integer,
    position integer,
    points real,
    status text
);