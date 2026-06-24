-- Заполнение таблицы жанров
INSERT INTO genres (name) VALUES
('Рок'),
('Поп'),
('Джаз'),
('Электронная музыка');

-- Заполнение таблицы исполнителей
INSERT INTO artists (name) VALUES
('The Beatles'),
('Queen'),
('Madonna'),
('Daft Punk'),
('Eminem');

-- Заполнение связей исполнителей и жанров
INSERT INTO artist_genres (artist_id, genre_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 4),
(4, 2),
(5, 2);

-- Заполнение таблицы альбомов
INSERT INTO albums (title, release_year) VALUES
('Abbey Road', 1969),
('A Night at the Opera', 1975),
('Like a Prayer', 1989),
('Random Access Memories', 2013),
('The Eminem Show', 2002);

-- Заполнение связей альбомов и исполнителей
INSERT INTO album_artists (album_id, artist_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- Заполнение таблицы треков
INSERT INTO tracks (album_id, title, duration_seconds) VALUES
(1, 'Come Together', 259),
(1, 'Something', 182),
(1, 'Here Comes the Sun', 185),
(2, 'Bohemian Rhapsody', 354),
(2, 'Love of My Life', 219),
(3, 'Like a Prayer', 332),
(3, 'Express Yourself', 277),
(4, 'Get Lucky', 368),
(4, 'Instant Crush', 337),
(5, 'Without Me', 290),
(5, 'Sing for the Moment', 337);

-- Заполнение таблицы сборников
INSERT INTO collections (name, release_year) VALUES
('The Greatest Hits of Rock', 2010),
('Pop Legends', 2015),
('Dance Classics', 2018),
('The Best of 2000s', 2020),
('Timeless Melodies', 2022);

-- Заполнение связей сборников и треков
-- Сборник The Greatest Hits of Rock
INSERT INTO collection_tracks (collection_id, track_id) VALUES
(1, 1),
(1, 2),
(1, 4),
(1, 5);

-- Сборник Pop Legends
INSERT INTO collection_tracks (collection_id, track_id) VALUES
(2, 6),
(2, 7),
(2, 3),
(2, 10);

-- Сборник Dance Classics
INSERT INTO collection_tracks (collection_id, track_id) VALUES
(3, 8),
(3, 9),
(3, 7);

-- Сборник The Best of 2000s
INSERT INTO collection_tracks (collection_id, track_id) VALUES
(4, 10),
(4, 11),
(4, 8);

-- Сборник Timeless Melodies
INSERT INTO collection_tracks (collection_id, track_id) VALUES
(5, 2),
(5, 5),
(5, 6),
(5, 11);
