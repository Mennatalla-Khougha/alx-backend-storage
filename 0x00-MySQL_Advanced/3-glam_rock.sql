-- SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- calculate the life span of bands with glam rock style
SELECT band_name, IF (split IS NULL , 2022, split) - formed AS lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;