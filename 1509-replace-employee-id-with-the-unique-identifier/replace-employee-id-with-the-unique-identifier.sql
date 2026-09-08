# Write your MySQL query statement below
select EmployeeUNI.unique_id, employees.name from employees left join employeeuni on employees.id=employeeuni.id;