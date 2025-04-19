-- SQLite


--SELECT id, page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, Year
--FROM MarvelCharacters;


-- 1 задание
--SELECT name, first_appearance, COUNT(*) as appearances
--FROM MarvelCharacters
--WHERE hair = 'Bald' 
--AND alignment = 'Bad Characters'
--AND first_appearance BETWEEN 1990 AND 1999
--GROUP BY name, first_appearance;


-- 2 задание
--SELECT name, first_appearance, eye_color
--FROM MarvelCharacters
--WHERE secret_identity = 'Secret Identity'
--AND eye_color NOT IN ('Blue', 'Brown', 'Green')
--AND first_appearance IS NOT NULL;


-- 3 задание
--SELECT name, hair_color
--FROM MarvelCharacters
--WHERE hair = 'Variable Hair';


-- 4 задание
--SELECT name, eye_color
--FROM MarvelCharacters
--WHERE gender = 'Female'
--AND eye_color IN ('Gold', 'Amber');


-- 5 задание
--SELECT name, first_appearance
--FROM MarvelCharacters
--WHERE dual_identity = 'No Dual Identity'
--ORDER BY first_appearance DESC;



--6 задание
--SELECT name, alignment, hair_color
--FROM MarvelCharacters
--WHERE hair_color NOT IN ('Brown', 'Black', 'Blond', 'Red')
--AND alignment IN ('Good Characters', 'Bad Characters');


--7 задание
--SELECT name, first_appearance
--FROM MarvelCharacters
--WHERE first_appearance BETWEEN 1960 AND 1969;


--8 задание
--SELECT name, eye_color, hair_color
--FROM MarvelCharacters
--WHERE eye_color = 'Yellow' AND hair_color = 'Red';



-- 9 задание
--SELECT name, COUNT(*) as appearances
--FROM MarvelCharacters
--GROUP BY name
--HAVING COUNT(*) < 10;


-- 10 задание 
SELECT name, COUNT(*) as appearances
FROM MarvelCharacters
GROUP BY name
ORDER BY appearances DESC
LIMIT 5;
