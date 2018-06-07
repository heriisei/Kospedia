-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: kospedia_db
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('292a3c2c3e9c');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `Cid` int(11) NOT NULL AUTO_INCREMENT,
  `kota` varchar(60) DEFAULT NULL,
  `provinsi` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`Cid`),
  KEY `ix_cities_kota` (`kota`),
  KEY `ix_cities_provinsi` (`provinsi`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities`
--

LOCK TABLES `cities` WRITE;
/*!40000 ALTER TABLE `cities` DISABLE KEYS */;
INSERT INTO `cities` VALUES (1,'Jakarta Pusat','DKI Jakarta'),(2,'Jakarta Barat','DKI Jakarta'),(3,'Jakarta Selatan','DKI Jakarta'),(4,'Jalarta Timur','DKI Jakarta'),(5,'Jakarta Utara','DKI Jakarta'),(6,'Kepulauan Seribu','DKI Jakarta'),(7,'Tangerang Selatan','Banten');
/*!40000 ALTER TABLE `cities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kosts`
--

DROP TABLE IF EXISTS `kosts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `kosts` (
  `Kid` int(11) NOT NULL AUTO_INCREMENT,
  `Kname` varchar(60) DEFAULT NULL,
  `Kaddress` varchar(100) DEFAULT NULL,
  `Kphone` varchar(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `Kverified` tinyint(1) DEFAULT NULL,
  `Klat` decimal(10,8) DEFAULT NULL,
  `Klng` decimal(11,8) DEFAULT NULL,
  `city_Cid` int(11) DEFAULT NULL,
  `Kprice` int(11) DEFAULT NULL,
  `Ktype` varchar(20) DEFAULT NULL,
  `Kprice_range` int(11) DEFAULT NULL,
  PRIMARY KEY (`Kid`),
  KEY `user_id` (`user_id`),
  KEY `city_Cid` (`city_Cid`),
  KEY `ix_kosts_Kaddress` (`Kaddress`),
  KEY `ix_kosts_Kname` (`Kname`),
  CONSTRAINT `kosts_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `kosts_ibfk_3` FOREIGN KEY (`city_Cid`) REFERENCES `cities` (`Cid`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kosts`
--

LOCK TABLES `kosts` WRITE;
/*!40000 ALTER TABLE `kosts` DISABLE KEYS */;
INSERT INTO `kosts` VALUES (16,'Baru','Mampang Prapatan','08988988410',1,0,NULL,NULL,3,500000,NULL,2),(19,'Kost Wartawan','Jl. Antara','021111111',2,1,-6.17000000,106.84000000,1,200000,'Kost Laki-Laki',1),(20,'Kost Engkoh','Jl. Mangga Dua','021222222',2,1,-6.15000000,106.81000000,1,200000,'Kost Laki-Laki',1),(21,'Kost Lumba-Lumba','Jl. Lodan Raya','021333333',2,1,-6.16000000,106.83000000,5,300000,'Kost Perempuan',1),(22,'Kost Hidayah','Jl. Taman Mini','021444444',2,1,-6.31000000,106.87000000,4,400000,'Kost Pasutri',2),(23,'Kost Indo','Jl. TMII','021555555',2,1,-6.29000000,106.89000000,4,450000,'Kost Perempuan',2),(24,'Kost Pilot','Jl. Halim','021666666',2,1,-6.28000000,106.90000000,4,350000,'Kost Laki-Laki',2),(25,'Kost Mahal','Jl. Mh. Thamrin','021777777',2,1,-6.19000000,106.82000000,1,800000,'Kost Pasutri',3),(26,'Kost Kapolri','Jl. Gatot Subroto','021888888',2,1,-6.22000000,106.81000000,3,1000000,'Kost Laki-Laki',4),(27,'Kost Setnov','Jl. Gatot Subroto','021888888',2,1,-6.21000000,106.79000000,3,100000,'Kost Laki-Laki',1),(28,'Kost Presiden','Jl. Medan Merdeka Utara','021999999',2,1,-6.17000000,106.83000000,1,2000000,'Kost Pasutri',5),(30,'Kost Pulau','Jl. Pantai','500000',2,1,-5.98000000,106.71000000,6,400000,'Kost Pasutri',2),(31,'Kost Pinggiran','Mampang Prapatan','500000',1,1,-6.24678400,106.82714300,3,800000,'Kost Pasutri',3),(32,'Baru Banget','Jl. Pondok Gede','08988988410',1,1,-6.28302500,106.91118900,4,1000000,'Kost Laki-Laki',4),(33,'Kost Murah','Jl. MH. Thamrin','090999210',7,1,-6.19721620,106.81969230,1,250000,'Kost Pasutri',1);
/*!40000 ALTER TABLE `kosts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(60) DEFAULT NULL,
  `username` varchar(60) DEFAULT NULL,
  `nama_depan` varchar(60) DEFAULT NULL,
  `nama_belakang` varchar(60) DEFAULT NULL,
  `tanggal_lahir` date DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `is_kost_owner` tinyint(1) DEFAULT NULL,
  `kota_Cid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`),
  KEY `ix_users_nama_belakang` (`nama_belakang`),
  KEY `ix_users_nama_depan` (`nama_depan`),
  KEY `ix_users_tanggal_lahir` (`tanggal_lahir`),
  KEY `kota_Cid` (`kota_Cid`),
  CONSTRAINT `users_ibfk_1` FOREIGN KEY (`kota_Cid`) REFERENCES `cities` (`Cid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'heri@heri.com','heriisei','Heri','Risnanto','1995-01-14','pbkdf2:sha256:50000$SFwarHyj$3d4361a3de21f805233cb38340034df93fd94ebb673f02cdb4fa409dd95a87ca',0,0,3),(2,'super@admin.com','superadmin','super','admin',NULL,'pbkdf2:sha256:50000$LABXTAKL$77ac434946517b6a60109c286d69fea4e3bf8419603616a50a93da977c83e674',1,0,1),(3,'ferdi@ferdi.com','ferdi','ferdi','an','1995-03-07','pbkdf2:sha256:50000$UUTmpdMb$a1ef927f844e1822d498af768bb998ffe73b4d4027b210149cecf4993956c825',0,0,4),(4,'tania@nur.com','tania','tania','nur','1993-07-31','pbkdf2:sha256:50000$2usT7C8H$f41f3b743f5288a877d8d7fb883adbf00272983bb69593def21441da878848b5',0,0,2),(5,'joko@joko.com','joko','Joko','Joko','1990-07-21','pbkdf2:sha256:50000$aVWnP4Mn$7ef2d305cb1073a3741c2414a0c694c750f759d0522d0217d9c4058090ffeb8a',0,0,5),(6,'adminheri@heri.com','adminheri',NULL,NULL,NULL,'pbkdf2:sha256:50000$zBgIH9Zs$911d464e964653531b29cb5c0e3ddbb5e977fda3e733e0022a09da1f79bc5ab7',1,0,NULL),(7,'tamu@tamu.com','tamu','Guest','tamu','1992-04-29','pbkdf2:sha256:50000$khrq7unA$de357d2abc767e66504442b6d67dd3f25ebe9c1bd54114c1abf01fa67fffca01',0,0,2);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-08  3:38:15
