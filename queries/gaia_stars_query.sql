SELECT TOP 1000
       source_id,
       ra,
       dec,
       parallax,
       designation,
       phot_g_mean_mag,
       designation
FROM gaiadr3.gaia_source
WHERE phot_g_mean_mag < 17
  AND parallax > 0