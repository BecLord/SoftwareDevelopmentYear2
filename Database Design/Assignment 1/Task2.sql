-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: assignement1
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cardetails`
--

DROP TABLE IF EXISTS `cardetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardetails` (
  `carReg` varchar(8) NOT NULL,
  `make` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`carReg`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardetails`
--

LOCK TABLES `cardetails` WRITE;
/*!40000 ALTER TABLE `cardetails` DISABLE KEYS */;
INSERT INTO `cardetails` VALUES ('M134 BRP','Ford','Escort'),('M565 0GD','Ford','Fiesta'),('M611 0PQ','Nissan','Sunny'),('N734 TPR','Nissan','Sunny');
/*!40000 ALTER TABLE `cardetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carhire`
--

DROP TABLE IF EXISTS `carhire`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carhire` (
  `hireNo` int NOT NULL AUTO_INCREMENT,
  `hireDate` date DEFAULT NULL,
  `outletNo` int NOT NULL,
  `custNo` varchar(4) NOT NULL,
  `carReg` varchar(8) NOT NULL,
  PRIMARY KEY (`hireNo`),
  KEY `FKCarHire137469` (`outletNo`),
  KEY `FKCarHire403692` (`custNo`),
  KEY `FKCarHire883328` (`carReg`),
  CONSTRAINT `FKCarHire137469` FOREIGN KEY (`outletNo`) REFERENCES `outlet` (`outletNo`),
  CONSTRAINT `FKCarHire403692` FOREIGN KEY (`custNo`) REFERENCES `customer` (`custNo`),
  CONSTRAINT `FKCarHire883328` FOREIGN KEY (`carReg`) REFERENCES `cardetails` (`carReg`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carhire`
--

LOCK TABLES `carhire` WRITE;
/*!40000 ALTER TABLE `carhire` DISABLE KEYS */;
INSERT INTO `carhire` VALUES (58,'2024-05-14',1,'C100','M565 0GD'),(59,'2024-05-15',1,'C201','M565 0GD'),(60,'2024-05-16',1,'C100','M565 0GD'),(61,'2024-05-14',2,'C313','M134 BRP'),(62,'2024-05-20',2,'C100','M134 BRP'),(63,'2024-05-20',2,'C295','M611 0PQ');
/*!40000 ALTER TABLE `carhire` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `custNo` varchar(4) NOT NULL,
  `custName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`custNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('C100','Smith, J'),('C201','Hen, P'),('C295','Pen, T'),('C313','Blatt, O');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outlet`
--

DROP TABLE IF EXISTS `outlet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outlet` (
  `outletNo` int NOT NULL AUTO_INCREMENT,
  `outletLoc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`outletNo`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outlet`
--

LOCK TABLES `outlet` WRITE;
/*!40000 ALTER TABLE `outlet` DISABLE KEYS */;
INSERT INTO `outlet` VALUES (1,'Killarney'),(2,'Tralee');
/*!40000 ALTER TABLE `outlet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed
