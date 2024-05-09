select * from Users as U
where mail LIKE "%@leetcode.com"
and mail REGEXP "^[A-Za-z][-_.A-Za-z0-9]*@leetcode.com$"

