SELECT AVG(s.energy)
FROM songs AS s
JOIN artists AS a ON s.artist_id = a.id
WHERE a.name = 'Drake';
