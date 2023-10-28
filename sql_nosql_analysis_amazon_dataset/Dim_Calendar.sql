-- Cleansing DIMDate Table 								--Taske Of 03/19/2023
SELECT
   [DateKey],
   [FullDateAlternateKey] AS DATE,
   --,[DayNumberOfWeek],
   [EnglishDayNameOfWeek] AS DAY,
   --,[SpanishDayNameOfWeek]
   --,[FrenchDayNameOfWeek]
   --,[DayNumberOfMonth]
   --,[DayNumberOfYear],
   [WeekNumberOfYear] AS WeekNo,
   [EnglishMonthName] AS MONTH,
   LEFT([EnglishMonthName], 3) AS MonthShort,
   --,[SpanishMonthName]
   --,[FrenchMonthName],
   [MonthNumberOfYear] AS MonthNo,
   [CalendarQuarter] AS Quarter,
   [CalendarYear] AS Year --,[CalendarSemester]
   --,[FiscalQuarter]
   --,[FiscalYear]
   --,[FiscalSemester]
FROM
   [AdventureWorksDW2019].[dbo].[DimDate]
WHERE
   CalendarYear > 2012;