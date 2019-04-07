DROP DATABASE IF EXISTS projekty_gminne;
CREATE DATABASE IF NOT EXISTS projekty_gminne CHARACTER SET utf8 COLLATE utf8_polish_ci;
GRANT ALL PRIVILEGES ON projekty_gminne.* TO 'projekty_gminne_user'@'localhost' IDENTIFIED BY 'your_P@ssw0rd_here';
