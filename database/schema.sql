DROP TABLE IF EXISTS phone;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS component;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS "order";
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS phoneComponent;


CREATE TABLE company
(
    name                 TEXT NOT NULL,
    webside_name         TEXT NOT NULL,
    company_email        TEXT NOT NULL,
    company_phone_number TEXT NOT NULL,
    id_company           INTEGER PRIMARY KEY AUTOINCREMENT
);



CREATE TABLE component
(
    id_component           INTEGER PRIMARY KEY AUTOINCREMENT,
    price                  FLOAT   NOT NULL,
    availability           INTEGER NOT NULL,
    name                   TEXT    NOT NULL,
    component_id_component INTEGER,
    FOREIGN KEY (component_id_component) REFERENCES component (id_component)

);



CREATE TABLE users
(
    id_user            INTEGER PRIMARY KEY AUTOINCREMENT,
    position           TEXT   NOT NULL,
    first_name         TEXT   NOT NULL,
    last_name          TEXT   NOT NULL,
    phone_number       TEXT   NOT NULL,
    email              TEXT   NOT NULL,
    hourly_wage        FLOAT  NOT NULL,
    login_name         TEXT   NOT NULL UNIQUE,
    login_password     TEXT   NOT NULL,
    company_company_id NUMBER NOT NULL,
    active             BIT(1) default 0,
    FOREIGN KEY (company_company_id
        ) REFERENCES company (id_company)
);



CREATE TABLE "order"
(
    id_order      INTEGER PRIMARY KEY AUTOINCREMENT,
    price         INTEGER NOT NULL,
    shipping      TEXT    NOT NULL,
    delivery_date DATE    NOT NULL,
    user_id_user  INTEGER NOT NULL,
    payment       TEXT    NOT NULL,
    FOREIGN KEY (user_id_user) REFERENCES users (id_user)
);



CREATE TABLE phone
(
    id_phone           INTEGER PRIMARY KEY AUTOINCREMENT,
    img                img,
    workload           FLOAT  NOT NULL,
    type               TEXT   NOT NULL,
    name               TEXT   NOT NULL,
    order_id_order     INTEGER,
    company_company_id NUMBER NOT NULL,
    FOREIGN KEY (order_id_order) REFERENCES "order" (id_order),
    FOREIGN KEY (company_company_id) REFERENCES company (id_company)
);


CREATE TABLE phoneComponent
(

    phoneComponent_component_fk INTEGER NOT NULL,
    phoneComponent_phone_fk     INTEGER NOT NULL,
    FOREIGN KEY (phoneComponent_component_fk) REFERENCES component (id_component),
    FOREIGN KEY (phoneComponent_phone_fk) REFERENCES phone (id_phone)

);

INSERT INTO company (name, webside_name, company_email, company_phone_number)
VALUES ('Phone shop', 'www.phoneshop.com', 'phoneshop@gmail.com', '+420 411 555 654');

INSERT INTO users (position, first_name, last_name, phone_number, email, hourly_wage, login_name, login_password,
                   company_company_id,active)
VALUES ('Admin', 'Pepa', 'Slepice', '+420 787 845 977', 'slepicepepa@gmail.com', 200, 'xslepice',
        '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 1,1); /* password:admin */

INSERT INTO users (position, first_name, last_name, phone_number, email, hourly_wage, login_name, login_password,
                   company_company_id,active)
VALUES ('Customer', 'Londa', 'Honda', '+420 223 355 977', 'londaHonda@gmail.com', 1, 'xlondahonda',
        '5a06bff60299b613b18749ab742ef760b6a48e47417156cd6d4ce5f2e4f1c981', 1,0); /* password:londahonda */

INSERT INTO users (position, first_name, last_name, phone_number, email, hourly_wage, login_name, login_password,
                   company_company_id,active)
VALUES ('Employee', 'Tomy', 'Pomy', '+420 223 355 977', 'tomypomy@gmail.com', 666, 'xtomypomy',
        '92fac25f88970947bb90ff436c9cfd48be1bba63fd2502a9de3e3707458d420a', 1,1); /* password:tomypomy */


INSERT INTO component (price, availability, name)
VALUES (1500, 20, 'RAM 2GB');
INSERT INTO component (price, availability, name)
VALUES (500, 10, 'RAM 500MB');

INSERT INTO phone(workload, type, name, company_company_id,img)
VALUES (10, 'smartphone', 'first phone', 1,'https://cdn.alza.cz/ImgW.ashx?fd=f16&cd=SAMO0233b2');
INSERT INTO phone(workload, type, name, company_company_id,img)
VALUES (10, 'smartphone', 'the best phone', 1,'https://cdn.alza.cz/ImgW.ashx?fd=f16&cd=SAMO0215b4');
INSERT INTO phone(workload, type, name, company_company_id,img)
VALUES (10, 'feature phones', 'old phone', 1,'https://cdn.alza.cz/ImgW.ashx?fd=f16&cd=AL0321a2b');

INSERT INTO phoneComponent(PHONECOMPONENT_COMPONENT_FK, PHONECOMPONENT_PHONE_FK)
VALUES (1, 1);

INSERT INTO phoneComponent(PHONECOMPONENT_COMPONENT_FK, PHONECOMPONENT_PHONE_FK)
VALUES (2, 3);
end;