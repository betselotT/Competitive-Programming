With MaxSalaryCTE AS
				   (
					select *,
						   dense_rank() Over(Partition By DepartmentId order by Salary Desc) RN
					from employee 
					)
Select 
      d.name Department,
      m.name Employee,
      m.salary Salary
From MaxSalaryCTE as m
Join Department as d
On m.DepartmentId =d.id
Where rn =1