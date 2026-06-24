-- =========
-- ЗАДАНИЕ 2
-- =========

-- 1. Название и продолжительность самого длительного трека
SELECT title, duration_seconds
FROM tracks
WHERE duration_seconds = (SELECT MAX(duration_seconds) FROM tracks);

-- 2. Название треков, продолжительность которых не менее 3,5 минут (210 секунд)
SELECT title, duration_seconds
FROM tracks
WHERE duration_seconds >= 210
ORDER BY duration_seconds DESC;

-- 3. Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT name, release_year
FROM collections
WHERE release_year BETWEEN 2018 AND 2020
ORDER BY release_year;

-- 4. Исполнители, чьё имя состоит из одного слова
SELECT name
FROM artists
WHERE name NOT LIKE '% %';

-- 5. ДОРАБОТАН: Название треков, которые содержат слово «мой» или «my» (решил через регулярку)
SELECT title
FROM tracks
WHERE title ~* '(^|\s)my(\s|$)' OR title ~* '(^|\s)мой(\s|$)';

-- =========
-- ЗАДАНИЕ 3
-- =========

-- 1. Количество исполнителей в каждом жанре
SELECT 
    g.name AS genre,
    COUNT(ag.artist_id) AS artists_count
FROM genres g
LEFT JOIN artist_genres ag ON g.genre_id = ag.genre_id
GROUP BY g.genre_id, g.name
ORDER BY artists_count DESC;

-- 2. Количество треков, вошедших в альбомы 2019–2020 годов
SELECT 
    COUNT(t.track_id) AS tracks_count
FROM tracks t
JOIN albums a ON t.album_id = a.album_id
WHERE a.release_year BETWEEN 2019 AND 2020;

-- 3. Средняя продолжительность треков по каждому альбому
SELECT 
    a.title AS album,
    AVG(t.duration_seconds) AS avg_duration_seconds
FROM albums a
JOIN tracks t ON a.album_id = t.album_id
GROUP BY a.album_id, a.title
ORDER BY avg_duration_seconds DESC;

-- 4. ДОРАБОТАН: Все исполнители, которые не выпустили альбомы в 2020 году (вариант с NOT EXISTS)
SELECT name
FROM artists ar
WHERE NOT EXISTS (
    SELECT 1
    FROM album_artists aa
    JOIN albums a ON aa.album_id = a.album_id
    WHERE aa.artist_id = ar.artist_id
    AND a.release_year = 2020
)
ORDER BY name;

-- 5. Названия сборников, в которых присутствует конкретный исполнитель (например, Queen)
SELECT DISTINCT c.name AS collection_name
FROM collections c
JOIN collection_tracks ct ON c.collection_id = ct.collection_id
JOIN tracks t ON ct.track_id = t.track_id
JOIN albums a ON t.album_id = a.album_id
JOIN album_artists aa ON a.album_id = aa.album_id
JOIN artists ar ON aa.artist_id = ar.artist_id
WHERE ar.name = 'Queen'
ORDER BY c.name;
