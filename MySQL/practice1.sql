SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY percentage asc;

SELECT countries.name, COUNT(cities.name)
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.name);

SELECT countries.name, cities.name
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population desc;

SELECT countries.name, languages.language
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage desc;

SELECT name
FROM countries
WHERE surface_area < 501 and population > 100000;

SELECT name
FROM countries
WHERE capital > 200 and government_form = 'Constitutional Monarchy' and life_expectancy > 75;

SELECT countries.name
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'







