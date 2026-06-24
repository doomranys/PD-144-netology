-- Создание таблицы с жанрами
CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

-- Создание таблицы с исполнителями
CREATE TABLE artists (
    artist_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE
);

-- Таблица исполнители - жанры (многие-ко-многим)
CREATE TABLE artist_genres (
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    genre_id INTEGER NOT NULL REFERENCES genres(genre_id) ON DELETE CASCADE,
    PRIMARY KEY (artist_id, genre_id)
);

-- Создание таблицы с альбомами
CREATE TABLE albums (
    album_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    release_year INTEGER CHECK (release_year > 1900 AND release_year <= EXTRACT(YEAR FROM CURRENT_DATE))
);

-- Таблица альбомы - исполнители (многие-ко-многим)
CREATE TABLE album_artists (
    album_id INTEGER NOT NULL REFERENCES albums(album_id) ON DELETE CASCADE,
    artist_id INTEGER NOT NULL REFERENCES artists(artist_id) ON DELETE CASCADE,
    PRIMARY KEY (album_id, artist_id)
);

-- Создание таблицы с треками
CREATE TABLE tracks (
    track_id SERIAL PRIMARY KEY,
    album_id INTEGER NOT NULL REFERENCES albums(album_id) ON DELETE CASCADE,
    title VARCHAR(200) NOT NULL,
    duration_seconds INTEGER CHECK (duration_seconds > 0)
);

-- Создание таблицы со сборниками
CREATE TABLE collections (
    collection_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    release_year INTEGER CHECK (release_year > 1900 AND release_year <= EXTRACT(YEAR FROM CURRENT_DATE))
);

-- Связующая таблица многие-ко-многим (сборники - треки)
CREATE TABLE collection_tracks (
    collection_id INTEGER NOT NULL REFERENCES collections(collection_id) ON DELETE CASCADE,
    track_id INTEGER NOT NULL REFERENCES tracks(track_id) ON DELETE CASCADE,
    PRIMARY KEY (collection_id, track_id)
);
