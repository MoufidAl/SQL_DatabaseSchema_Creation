CREATE TABLE "Orders" (
  "row_id" integer PRIMARY KEY,
  "order_id" varchar(10),
  "order_time" datetime,
  "category" varchar(50),
  "item_id" integer,
  "quantity" integer,
  "customer_id" integer,
  "delivery_order" boolean,
  "address_id" integer
);

CREATE TABLE "Customers" (
  "customer_id" integer PRIMARY KEY,
  "firstname" varchar(50),
  "lastname" varchar(50)
);

CREATE TABLE "Address" (
  "address_id" integer PRIMARY KEY,
  "delivery_address" varchar(50),
  "delivery_address2" varchar(50),
  "delivery_city" varchar(50),
  "delivery_zipcode" varchar(50)
);

CREATE TABLE "Items" (
  "item_id" integer PRIMARY KEY,
  "sku" varchar(20),
  "item_name" varchar(50),
  "item_price" decimal(5,2),
  "item_size" varchar(20)
);

CREATE TABLE "Recipe" (
  "row_id" integer PRIMARY KEY,
  "recipe_id" varchar(20),
  "ingredient_id" varchar(20),
  "quantity" integer
);

CREATE TABLE "Ingredients" (
  "ingredient_id" integer PRIMARY KEY,
  "ingredient_name" varchar(50),
  "ingredient_measure" varchar(50),
  "ingredient_weight" integer,
  "ingredient_price" decimal(5,2)
);

CREATE TABLE "Inventory" (
  "inventory_id" integer PRIMARY KEY,
  "item_id" integer,
  "quantity" integer
);

CREATE TABLE "Staff" (
  "staff_id" integer PRIMARY KEY,
  "first_name" varchar(30),
  "last_name" varchar(30),
  "position" varchar(50),
  "hourly_rate" decimal(5,2)
);

CREATE TABLE "Shift" (
  "shift_id" integer PRIMARY KEY,
  "day_of_week" varchar(20),
  "start_time" time,
  "end_time" time
);

CREATE TABLE "Rotation" (
  "row_id" integer PRIMARY KEY,
  "rotation_id" integer,
  "date" datetime,
  "shift_id" integer,
  "staff_id" integer
);

ALTER TABLE "Recipe" ADD FOREIGN KEY ("recipe_id") REFERENCES "Items" ("sku");

ALTER TABLE "Orders" ADD FOREIGN KEY ("item_id") REFERENCES "Items" ("item_id");

ALTER TABLE "Orders" ADD FOREIGN KEY ("address_id") REFERENCES "Address" ("address_id");

ALTER TABLE "Orders" ADD FOREIGN KEY ("customer_id") REFERENCES "Customers" ("customer_id");

ALTER TABLE "Recipe" ADD FOREIGN KEY ("ingredient_id") REFERENCES "Ingredients" ("ingredient_id");

ALTER TABLE "Recipe" ADD FOREIGN KEY ("ingredient_id") REFERENCES "Inventory" ("item_id");

ALTER TABLE "Orders" ADD FOREIGN KEY ("order_time") REFERENCES "Rotation" ("date");

ALTER TABLE "Rotation" ADD FOREIGN KEY ("staff_id") REFERENCES "Staff" ("staff_id");

ALTER TABLE "Rotation" ADD FOREIGN KEY ("shift_id") REFERENCES "Shift" ("shift_id");
