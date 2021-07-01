BEGIN TRANSACTION;
DROP TABLE IF EXISTS "doc_header";
CREATE TABLE IF NOT EXISTS "doc_header" (
	"h_id"	INTEGER,
	"client_name"	TEXT,
	"client_class"	TEXT,
	"category"	TEXT,
	"apply_date"	TEXT,
	"person"	TEXT,
	"doc_descript"	TEXT,
	"memo"	TEXT,
	PRIMARY KEY("h_id" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "doc_body";
CREATE TABLE IF NOT EXISTS "doc_body" (
	"h_id"	INTEGER,
	"b_id"	INTEGER,
	"item_num"	INTEGER,
	"p_name"	TEXT,
	"p_qty"	INTEGER,
	"p_price"	INTEGER,
	PRIMARY KEY("b_id" AUTOINCREMENT)
);
COMMIT;
