-- MySQL dump 10.13  Distrib 9.1.0, for Win64 (x86_64)
--
-- Host: localhost    Database: bowling
-- ------------------------------------------------------
-- Server version	9.1.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `allframes`
--

DROP TABLE IF EXISTS `allframes`;
/*!50001 DROP VIEW IF EXISTS `allframes`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `allframes` AS SELECT 
 1 AS `frame`,
 1 AS `gameID`,
 1 AS `attempt`,
 1 AS `score`,
 1 AS `score_type`,
 1 AS `shot_type`,
 1 AS `pin_setup`,
 1 AS `ball_speed`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `bowling_balls`
--

DROP TABLE IF EXISTS `bowling_balls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bowling_balls` (
  `bID` int NOT NULL AUTO_INCREMENT,
  `color` varchar(30) NOT NULL,
  `weight` int NOT NULL,
  `coverstock` varchar(20) DEFAULT NULL,
  `core` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`bID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bowling_balls`
--

LOCK TABLES `bowling_balls` WRITE;
/*!40000 ALTER TABLE `bowling_balls` DISABLE KEYS */;
INSERT INTO `bowling_balls` VALUES (1,'Orange',14,'Urethane','Symmetrical'),(4,'White',15,'Reactive','Pancake'),(7,'Icy Blue',16,'Reactive','Pancake');
/*!40000 ALTER TABLE `bowling_balls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frames`
--

DROP TABLE IF EXISTS `frames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frames` (
  `frame` int NOT NULL,
  `gameID` int NOT NULL,
  `playerID` int NOT NULL,
  `attempt` int NOT NULL,
  `score` int NOT NULL,
  `score_type` varchar(10) NOT NULL,
  `shot_type` varchar(30) NOT NULL,
  `pin_setup` varchar(5) NOT NULL,
  `ball_speed` double DEFAULT NULL,
  PRIMARY KEY (`frame`,`gameID`,`playerID`,`attempt`),
  KEY `frames_ibfk_1` (`gameID`),
  KEY `frames_ibfk_2` (`playerID`),
  CONSTRAINT `frames_ibfk_1` FOREIGN KEY (`gameID`) REFERENCES `games` (`gameID`) ON DELETE CASCADE,
  CONSTRAINT `frames_ibfk_2` FOREIGN KEY (`playerID`) REFERENCES `players` (`playerID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frames`
--

LOCK TABLES `frames` WRITE;
/*!40000 ALTER TABLE `frames` DISABLE KEYS */;
INSERT INTO `frames` VALUES (1,1,1,1,9,'Leftover','Curve','FH',15.78),(1,1,1,2,1,'Spare','Straight','DR',12.2),(1,2,2,1,10,'Strike','Straight','FH',17.54),(2,1,1,1,10,'Strike','Curve','FH',14.54),(2,2,2,1,8,'Leftover','Straight','FH',17.01),(2,2,2,2,2,'Spare','Straight-Curve','DL',17.01),(3,1,1,1,7,'Leftover','Straight-Curve','FH',16.09),(3,1,1,2,2,'Leftover','Hard-Curve','LD',13.77),(3,2,2,1,10,'Strike','Straight','FH',17.23),(4,1,1,1,8,'Leftover','Straight-Curve','FH',14.11),(4,1,1,2,1,'Leftover','Straight','HS',11.93),(4,2,2,1,9,'Leftover','Straight','FH',17.23),(4,2,2,2,1,'Spare','Straight-Curve','L',17.77),(5,1,1,1,10,'Strike','Curve','FH',14.61),(5,2,2,1,10,'Strike','Straight','FH',17.09),(6,1,1,1,10,'Strike','Straight-Curve','FH',15.04),(6,2,2,1,10,'Strike','Straight','FH',17.85),(7,1,1,1,9,'Leftover','Straight','FH',14.48),(7,1,1,2,0,'Leftover','Hard-Curve','DL',13.99),(7,2,2,1,8,'Leftover','Straight','FH',17.9),(7,2,2,2,2,'Spare','Straight-Curve','DL',17),(8,1,1,1,8,'Leftover','Straight-Curve','FH',15.25),(8,1,1,2,2,'Spare','Straight-Curve','R',13.82),(8,2,2,1,7,'Leftover','Straight','FH',17.58),(8,2,2,2,3,'Spare','Straight-Curve','MP',17.64),(9,1,1,1,5,'Leftover','Straight','FH',16.01),(9,1,1,2,4,'Leftover','Hard-Curve','MP',11.99),(9,2,2,1,5,'Leftover','Straight','FH',17.33),(9,2,2,2,5,'Spare','Straight-Curve','MP',17.69),(10,1,1,1,10,'Strike','Straight-Curve','FH',15.78),(10,1,1,2,6,'Leftover','Curve','FH',15.78),(10,1,1,3,3,'Leftover','Straight','M',15.78),(10,2,2,1,10,'Strike','Straight','FH',17.04),(10,2,2,2,9,'Leftover','Straight','FH',17.42),(10,2,2,3,1,'Spare','Straight-Curve','M',17.08);
/*!40000 ALTER TABLE `frames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `gameID` int NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `location` text,
  PRIMARY KEY (`gameID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES (1,'2023-06-24','Europa'),(2,'2024-12-01','Antarctica'),(3,'2024-12-02','Antarctica');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_ball_jt`
--

DROP TABLE IF EXISTS `player_ball_jt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_ball_jt` (
  `playerID` int NOT NULL,
  `bID` int NOT NULL,
  PRIMARY KEY (`playerID`,`bID`),
  KEY `player_ball_jt_ibfk_2` (`bID`),
  CONSTRAINT `player_ball_jt_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `players` (`playerID`) ON DELETE CASCADE,
  CONSTRAINT `player_ball_jt_ibfk_2` FOREIGN KEY (`bID`) REFERENCES `bowling_balls` (`bID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_ball_jt`
--

LOCK TABLES `player_ball_jt` WRITE;
/*!40000 ALTER TABLE `player_ball_jt` DISABLE KEYS */;
INSERT INTO `player_ball_jt` VALUES (1,1),(2,4),(4,7);
/*!40000 ALTER TABLE `player_ball_jt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `player_game_jt`
--

DROP TABLE IF EXISTS `player_game_jt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `player_game_jt` (
  `playerID` int NOT NULL,
  `gameID` int NOT NULL,
  `final_score` int NOT NULL,
  PRIMARY KEY (`playerID`,`gameID`),
  KEY `player_game_jt_ibfk_2` (`gameID`),
  CONSTRAINT `player_game_jt_ibfk_1` FOREIGN KEY (`playerID`) REFERENCES `players` (`playerID`) ON DELETE CASCADE,
  CONSTRAINT `player_game_jt_ibfk_2` FOREIGN KEY (`gameID`) REFERENCES `games` (`gameID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `player_game_jt`
--

LOCK TABLES `player_game_jt` WRITE;
/*!40000 ALTER TABLE `player_game_jt` DISABLE KEYS */;
INSERT INTO `player_game_jt` VALUES (1,1,157),(2,2,200),(2,3,208),(4,1,169),(4,3,176);
/*!40000 ALTER TABLE `player_game_jt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `players`
--

DROP TABLE IF EXISTS `players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `players` (
  `playerID` int NOT NULL AUTO_INCREMENT,
  `team_name` varchar(100) NOT NULL,
  `first_name` text NOT NULL,
  `last_name` text,
  `email` text NOT NULL,
  PRIMARY KEY (`playerID`),
  KEY `players_ibfk_1` (`team_name`),
  CONSTRAINT `players_ibfk_1` FOREIGN KEY (`team_name`) REFERENCES `teams` (`team_name`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `players`
--

LOCK TABLES `players` WRITE;
/*!40000 ALTER TABLE `players` DISABLE KEYS */;
INSERT INTO `players` VALUES (1,'Baller','Chops','Fleefo','choppa@ECmail.org'),(2,'SnowBallas','Snow','Gangsta','snowg@balla.com'),(4,'SnowBallas','Ice','Gangsta','iceg@balla.com');
/*!40000 ALTER TABLE `players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teams`
--

DROP TABLE IF EXISTS `teams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teams` (
  `team_name` varchar(100) NOT NULL,
  `num_players` int NOT NULL,
  `team_type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`team_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teams`
--

LOCK TABLES `teams` WRITE;
/*!40000 ALTER TABLE `teams` DISABLE KEYS */;
INSERT INTO `teams` VALUES ('Baller',1,'Solo'),('Decker',1,'Solo'),('Double Trouble',2,'Other'),('SnowBallas',4,'Private');
/*!40000 ALTER TABLE `teams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `allframes`
--

/*!50001 DROP VIEW IF EXISTS `allframes`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `allframes` AS select `frames`.`frame` AS `frame`,`frames`.`gameID` AS `gameID`,`frames`.`attempt` AS `attempt`,`frames`.`score` AS `score`,`frames`.`score_type` AS `score_type`,`frames`.`shot_type` AS `shot_type`,`frames`.`pin_setup` AS `pin_setup`,`frames`.`ball_speed` AS `ball_speed` from `frames` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-11 18:47:15
