CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(25) NOT NULL,
    user_email VARCHAR(50) NOT NULL,
    user_password CHAR(64) NOT NULL,
    is_deleted BOOLEAN DEFAULT FALSE
) ENGINE = INNODB;

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    weighted_rating REAL NOT NULL
) ENGINE = INNODB;

CREATE TABLE genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre VARCHAR(100) NOT NULL
) ENGINE = INNODB;

CREATE TABLE links (
    movie_id INT PRIMARY KEY,
    imdb_id VARCHAR(20),
    tmdb_id VARCHAR(20),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

CREATE TABLE movie_genre (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

CREATE TABLE ratings (
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    rating REAL NOT NULL,
    time_entered DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (movie_id, user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

CREATE TABLE tags (
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    tag VARCHAR(500) NOT NULL,
    time_entered DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (movie_id, user_id, tag(255)),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

CREATE TABLE movie_similarity (
    movie_id INT NOT NULL,
    similar_movie_id INT NOT NULL,
    ranking INT NOT NULL,
    similarity_score REAL NOT NULL,
    PRIMARY KEY (movie_id, similar_movie_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (similar_movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB;

CREATE TABLE watch_list (
    movie_id INT NOT NULL,
    user_id INT NOT NULL,
    watched TINYINT(1) DEFAULT 0,
    is_deleted TINYINT(1) DEFAULT 0,
    PRIMARY KEY (movie_id, user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = INNODB