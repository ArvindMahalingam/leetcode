# Write your MySQL query statement below
select x,y,z ,Case
    when x+y>z and x+z>y and y+z>x
    Then 'Yes'
    Else 'No'
    end
 as triangle from Triangle