SELECT
    strftime('%Y-%m', MAX(RecentDate)) AS Mes,
    COUNT(*) AS Cantidad_Etapa_1
FROM (
    SELECT
        ID,
        MAX(CASE
            WHEN strftime('%Y-%m', sal_date) = strftime('%Y-%m', MAX(sal_date)) THEN sal_date
            WHEN strftime('%Y-%m', sql_date) = strftime('%Y-%m', MAX(sql_date)) THEN sql_date
            -- Agrega más columnas de fecha aquí según sea necesario
            ELSE NULL
        END) AS RecentDate
    FROM
        Data
    GROUP BY
        ID, strftime('%Y-%m', sal_date)
) AS Subquery
GROUP BY
    Mes
ORDER BY
    Mes;