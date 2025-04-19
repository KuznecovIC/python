SELECT MIN(Year) AS "Самый ранний год появления", MAX(Year) AS "Самый поздний год появления" FROM MarvelCharacters

SELECT name,Year,APPEARANCES FROM MarvelCharacters where Year>=1939 and year<1990 AND APPEARANCES>100 ORDER BY APPEARANCES desc;