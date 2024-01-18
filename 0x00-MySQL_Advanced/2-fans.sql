-- SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans

-- group the no of fans by origin and order them by no of fans
SELECT origin, SUM(fans) AS nb_fans from metal_bands
GROUP BY origin ORDER BY nb_fans DESC;