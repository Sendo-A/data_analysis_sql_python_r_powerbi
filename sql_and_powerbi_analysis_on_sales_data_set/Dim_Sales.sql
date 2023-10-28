	-- Cleaning Product Table							--Taske Of 03/19/2023
	SELECT
	   [ProductKey],
	   [OrderDateKey],
	   [DueDateKey],
	   [ShipDateKey],
	   [CustomerKey],
	   --,[PromotionKey]
	   --,[CurrencyKey]
	   --,[SalesTerritoryKey]
	   [SalesOrderNumber],
	   --,[SalesOrderLineNumber]
	   --,[RevisionNumber]
	   --,[OrderQuantity]
	   --,[UnitPrice]
	   --,[ExtendedAmount]
	   --,[UnitPriceDiscountPct]
	   --,[DiscountAmount]
	   --,[ProductStandardCost]
	   --,[TotalProductCost]
	   [SalesAmount] --,[TaxAmt]
	   --,[Freight]
	   --,[CarrierTrackingNumber]
	   --,[CustomerPONumber]
	   --,[OrderDate]
	   --,[DueDate]
	   --,[ShipDate]
	FROM
	   [AdventureWorksDW2019].[dbo].[FactInternetSales]
	WHERE
	   LEFT (orderDateKey, 4) > 2012 -- s'assurer
	ORDER BY
	   orderDateKey asc