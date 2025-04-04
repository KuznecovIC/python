-- Задание 1
--SELECT ALIVE, count(*) 
--FROM MarvelCharacters
--GROUP BY ALIVE


-- Задание 2
--SELECT EYE, avg(APPEARANCES)
--FROM MarvelCharacters
--GROUP BY EYE


-- Задание 3
--SELECT EYE, max(APPEARANCES)
--FROM MarvelCharacters
--GROUP BY EYE

-- Задание 4
--SELECT identify, min(APPEARANCES)
--FROM MarvelCharacters
--WHERE identify = 'Public Identity'
--GROUP BY identify


-- Задание 5
--SELECT SEX, count(*)
--FROM MarvelCharacters
--GROUP BY SEX


-- Задание 6
--SELECT identify, avg(Year)
--FROM MarvelCharacters
--GROUP BY identify


-- Задание 7
--SELECT EYE, count(*)
--FROM MarvelCharacters
--WHERE ALIVE = 'Yes'
--GROUP BY EYE, ALIVE

-- Задание 8
--SELECT HAIR, max(APPEARANCES), min(APPEARANCES)
--FROM MarvelCharacters
--GROUP BY HAIR


-- Задание 9
--SELECT identify, count(*)
--FROM MarvelCharacters
--WHERE ALIVE = 'No'
--GROUP BY identify


-- Задание 10
--SELECT EYE, avg(Year)
--FROM MarvelCharacters
--GROUP BY EYE


-- Подзапрос 1
--SELECT name, APPEARANCES
--FROM MarvelCharacters
--WHERE APPEARANCES = (SELECT max(APPEARANCES) FROM MarvelCharacters)


-- Подзапрос 2
--SELECT name, Year
--FROM MarvelCharacters
--WHERE Year = (SELECT Year FROM MarvelCharacters WHERE APPEARANCES = (SELECT max(APPEARANCES) FROM MarvelCharacters))


-- Подзапрос 3
--SELECT name, APPEARANCES
--FROM MarvelCharacters
--WHERE ALIVE = 'Yes' AND APPEARANCES = (SELECT min(APPEARANCES) FROM MarvelCharacters WHERE ALIVE = 'Yes')


-- Задание 4
--SELECT identify, min(APPEARANCES)
--FROM MarvelCharacters
--WHERE identify = 'Public Identity'
--GROUP BY identify

-- Подзапрос 5
--SELECT name, identify, APPEARANCES
--FROM MarvelCharacters
--WHERE identify = 'Public Identify' AND APPEARANCES = (SELECT min(APPEARANCES) FROM MarvelCharacters WHERE identify = 'Public Identify')
