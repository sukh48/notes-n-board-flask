CREATE TABLE users (
        uid serial PRIMARY KEY NOT NULL,
        username VARCHAR(32) NOT NULL,
        password CHAR(32) NOT NULL,
        email VARCHAR(64),
        admin boolean
);

CREATE TABLE notes (
        uid serial PRIMARY KEY NOT NULL,
        stored_as VARCHAR(64),
        file_name VARCHAR(32),
        owner integer REFERENCES users(uid),
        contents TEXT,
        rating integer
);

CREATE TABLE note_ratings (
        noteID integer NOT NULL REFERENCES notes(uid),
        userID integer NOT NULL REFERENCES users(uid),
        rating integer,
        UNIQUE (noteID, userID)
);

CREATE TABLE tags_to_notes (
        tag VARCHAR(32) NOT NULL,
        noteID integer NOT NULL REFERENCES notes(noteID),
        UNIQUE (noteID, tag)
);

CREATE TABLE courses (
        courseID serial PRIMARY KEY,
        name VARCHAR(9),
        alt_name VARCHAR(255),
        professor integer REFERENCES users(uid)
);

CREATE TABLE messages (
        messageID serial PRIMARY KEY,
        title VARCHAR(455) NOT NULL,
        message TEXT NOT NULL,
        postTime TIMESTAMP NOT NULL,
        courseID integer NOT NULL REFERENCES courses(courseID),
        userID integer NOT NULL REFERENCES users(uid)
);

CREATE TABLE subscriptions (
        userID integer NOT NULL REFERENCES users(uid),
        courseID integer NOT NULL REFERENCES courses(courseID),
        UNIQUE (userID, courseID)
);

CREATE TABLE dates (
        eventID serial PRIMARY KEY,
        courseID integer REFERENCES courses(courseID),
        startDate TIMESTAMP,
        endDate TIMESTAMP,
        title VARCHAR(32),
        description VARCHAR(255)
);

CREATE TABLE todo (
        itemID serial PRIMARY KEY,
        userID integer REFERENCES users(uid),
        description VARCHAR(255)
);

CREATE TABLE comments (
        commentID serial PRIMARY KEY,
        comment TEXT,
        postTime TIMESTAMP NOT NULL,
        userID integer NOT NULL REFERENCES users(uid),
        messageID integer NOT NULL REFERENCES messages(messageID)
);