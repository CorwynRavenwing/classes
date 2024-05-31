CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE N_minus_1 int signed DEFAULT N - 1;
  RETURN (
    # Write your MySQL query statement below.
    select
        case
        when count(distinct salary) < N
        then null
        else (
            select distinct salary as SecondHighestSalary
            from Employee
            order by salary DESC
            limit 1
            offset N_minus_1
        ) end as SecondHighestSalary
    from Employee
  );
END

