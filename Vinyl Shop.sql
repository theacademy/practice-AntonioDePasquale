-- Vinyl Record Shop

DROP database if EXISTS vinylRecordShop;
CREATE database vinylRecordShop;
USE vinylRecordShop;

CREATE table band(
	bandID int primary key auto_increment,
    bandName varchar(50)
);

CREATE table album(
	albumID int auto_increment,
    albumTitle varchar(100),
    label varchar(50),
    releaseDate date,
    price decimal(5,2),
    constraint primary key(albumID)
);

CREATE table artist(
	artistID int primary key auto_increment,
	fName varchar(20),
    lName varchar(20)
);

CREATE table song(
	songID int primary key auto_increment,
    songTitle varchar(100),
    videoURL varchar(255),
    bandID int not null,
    constraint fk_song_band foreign key (bandID) references band(bandID)
);

CREATE table songAlbum(
	songID int,
    albumID int,
    constraint fk_songAlbum_song foreign key(songID) references song(songID),
    constraint fk_songAlbum_album foreign key(albumID) references album(albumID),
    primary key (songID, albumID)
);

CREATE table bandArtist(
	bandID int,
    artistID int,
    constraint fk_bandArtist_band foreign key(bandID) references band(bandID),
    constraint fk_bandArtist_artist foreign key(artistID) references artist(artistID),
    primary key(bandID, artistID)
);