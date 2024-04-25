CREATE TABLE stg.P_departments
(
    department_id INT,
    department_name VARCHAR(255) NOT NULL
 CONSTRAINT [pk_department_id] PRIMARY KEY NONCLUSTERED 
	(
		[department_id] ASC
	) NOT ENFORCED 
)
WITH
(
	DISTRIBUTION = ROUND_ROBIN,
	CLUSTERED COLUMNSTORE INDEX
);

CREATE TABLE stg.P_positions (
    position_id INT,
    position_name VARCHAR(255) NOT NULL
 CONSTRAINT [pk_position_id] PRIMARY KEY NONCLUSTERED 
	(
		[position_id] ASC
	) NOT ENFORCED 
)
WITH
(
	DISTRIBUTION = ROUND_ROBIN,
	CLUSTERED COLUMNSTORE INDEX
);

CREATE TABLE stg.P_employees (
    employee_id INT,
    employee_name VARCHAR(255) NOT NULL,
    department_id INT,
    position_id INT,
    hire_date DATE
 CONSTRAINT [pk_employee_id] PRIMARY KEY NONCLUSTERED 
	(
		[employee_id] ASC
	) NOT ENFORCED 
)
WITH
(
	DISTRIBUTION = ROUND_ROBIN,
	CLUSTERED COLUMNSTORE INDEX
);
