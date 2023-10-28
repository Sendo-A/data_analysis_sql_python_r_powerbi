-- Cleaning Customer Table							--Taske Of 03/19/2023
SELECT
   c.customerkey AS customerkey,
   --,[GeographyKey]
   --,[CustomerAlternateKey]
   --,[Title]
   c.firstname AS [FirstName],
   --,[MiddleName],
   c.lastname AS [LastName],
   c.firstname + ' ' + lastname AS [FULL_Name],
   -- Merge First and Last Name
   --[NameStyle]
   --,[BirthDate]
   --,[MaritalStatus]
   --,[Suffix]
   CASE
      c.gender
      WHEN 'M' THEN 'Male'
      WHEN 'F' THEN 'Female'
   END AS gender,
   --,[EmailAddress]
   --,[YearlyIncome]
   --,[TotalChildren]
   --,[NumberChildrenAtHome]
   --,[EnglishEducation]
   --,[SpanishEducation]
   --,[FrenchEducation]
   --,[EnglishOccupation]
   --,[SpanishOccupation]
   --,[FrenchOccupation]
   --,[HouseOwnerFlag]
   --,[NumberCarsOwned]
   --,[AddressLine1]
   --,[AddressLine2]
   --,[Phone]
   c.datefirstpurchase AS Date_First_Purchase,
   --,[CommuteDistance]
   g.city AS [Customer City] -- joined in customer City from Geography Table
FROM
   dbo.dimcustomer AS c
   LEFT JOIN dbo.dimgeography AS g ON g.geographykey = c.geographykey
ORDER BY
   customerkey ASC --order list by customer