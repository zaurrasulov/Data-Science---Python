SELECT *,
ISNULL(Daily_vaccinations, SELECT
								(
								(SELECT MAX(daily_vaccinations) FROM
								(SELECT TOP 50 PERCENT daily_vaccinations FROM COVID_table GROUP BY Country) AS BottomHalf)
									+
								(SELECT MIN(daily_vaccinations) FROM
								(SELECT TOP 50 PERCENT daily_vaccinations FROM COVID_Table GROUP BY Country) AS TopHalf)
								) / 2 AS Median)
FROM COVID_Table