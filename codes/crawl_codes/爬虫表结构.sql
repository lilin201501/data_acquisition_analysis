CREATE TABLE `qidian` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(200) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `information` varchar(200) DEFAULT NULL,
  `introduction` varchar(1000) DEFAULT NULL,
  `word_num` varchar(45) DEFAULT NULL,
  `clicks_num` varchar(45) DEFAULT NULL,
  `recommended_num` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `zhihu` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `author` varchar(45) DEFAULT NULL,
  `headline` varchar(45) DEFAULT NULL,
  `url` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci