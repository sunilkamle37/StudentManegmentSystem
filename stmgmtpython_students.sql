-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: stmgmtpython
-- ------------------------------------------------------
-- Server version	8.0.27

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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `roll_no` int NOT NULL,
  `name` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(100) NOT NULL,
  PRIMARY KEY (`roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Abhishek','abhi@gmail.com','Male','8602768216','1999-02-21','Sangavi\n\n'),(2,'Jain','jainnancy@gmail.com','Male','7566011114','2001-05-05','Bhosari\n\n'),(3,'ashok','ashok@gmail.com','Male','7655011111','2000-07-12','Wakad\r '),(4,'sunil Kamle','sunil37@gmail.com','Male','9881796526','1998-01-02','Baner\n\n'),(5,'zishan','zishan@','Male','7775452588','1995-12-08','kaij\n'),(6,'Inamdar','inamdar@123','Male','888888888','1997-06-23','Pune\n\n'),(7,'Raj ','raj123@gmail.com','Male','7894561230','1996-11-10','Pimpri gurav\n'),(8,'Gajanan','gajanan@gmail.com','Male','9922851267','1992-02-18','Katraj\n'),(9,'Govind','govind@gmail.com','Male','9881545321','1990-05-15','Katraj\n'),(10,'Vidhu','vidhu@gmail.com','Female','9922851267','2019-09-20','Kotharud,Pune\n'),(11,'Gabbar','gabbar@gmail.com','Male','8855584455','2021-10-30','Gadchiroli	\n'),(12,'Ankit','ankit@gmail.com','Male','9966551122','1998-10-30','Nashik\n'),(13,'Anand','anand@gmail.com','Male','7788445599','1984-07-20','Satara\n'),(14,'Rajesh','rajesh@gmail.com','Male','8844779966','1997-08-12','Belgao\n'),(15,'Dipak','dipak@gmail.com','Male','7715514466','1997-09-30','Karad\n'),(16,'Suraj','suraj@gmail.com','Male','8998788755','1997-07-09','Kagal,Kolhapur\n'),(17,'Sinnu','sinnu@gmail.com','Male','9382711758','1994-07-13','Andhrapradesh\n'),(18,'Rahul','rahul@gmail.com','Male','7987898789','1992-07-09','Jalgaon\n'),(19,'vivek','vivek@gmail.com','Male','8799887755','1992-07-14','Pune\n'),(20,'sunita','sunita@gmail.com','Female','8877995588','1994-07-07','Hinjawadi,Pune\n'),(21,'Harshal','harshal@gmail.com','Female','8338838833','1994-08-30','Baner\n'),(22,'Komal','komal@gmail.com','Female','7885548898','2001-03-01','Ahamadnagar\n'),(23,'Sakashi','sakshi@gmail.com','Female','9632587410','2001-03-01','Shirdi,Nagar\n'),(24,'Nehal','nehal@gmail.com','Male','987894565','2022-02-06','Beed\n'),(25,'Sameer ','sameer@gmail.com','Male','9889789858','2003-02-12','Ankulga\n'),(26,'Dipak','dipak@gmail.com','Male','9888887898','2000-02-08','Kokalgaonwadi\n');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-09 18:00:56
