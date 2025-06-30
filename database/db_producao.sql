CREATE DATABASE  IF NOT EXISTS `db_producao` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db_producao`;
-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: db_producao
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `funcionario_id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `setor` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`funcionario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'Ana Souza','Produção'),(2,'Carlos Lima','Manutenção'),(3,'Juliana Silva','Qualidade'),(5,'Fernanda Dias','Logística'),(6,'Marcos Melo','Manutenção'),(8,'Simone Alves','RH'),(9,'Thiago Martins','TI'),(10,'Laura Campos','Produção');
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `maquinas`
--

DROP TABLE IF EXISTS `maquinas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `maquinas` (
  `maquina_id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(100) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`maquina_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `maquinas`
--

LOCK TABLES `maquinas` WRITE;
/*!40000 ALTER TABLE `maquinas` DISABLE KEYS */;
INSERT INTO `maquinas` VALUES (1,'Prensa Hidráulica 500T','Ativa'),(2,'Torno CNC T-200','Parada'),(3,'Injetora Plástica IP-300','Ativa'),(4,'Esteira Transportadora 10m','Manutenção'),(5,'Furadeira Industrial F-90','Ativa'),(6,'Máquina de Corte Laser LZ-700','Ativa'),(7,'Compressor de Ar CA-50','Parada'),(8,'Moinho de Martelo MM-150','Ativa'),(9,'Empacotadora Automática EA-20','Ativa'),(10,'Caldeira Térmica CT-3000','Manutenção');
/*!40000 ALTER TABLE `maquinas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordens_producao`
--

DROP TABLE IF EXISTS `ordens_producao`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordens_producao` (
  `ordem_id` int NOT NULL AUTO_INCREMENT,
  `funcionario_id` int DEFAULT NULL,
  `maquina_id` int DEFAULT NULL,
  `produto` varchar(50) NOT NULL,
  `quantidade` int NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ordem_id`),
  KEY `funcionario_id` (`funcionario_id`),
  KEY `maquina_id` (`maquina_id`),
  CONSTRAINT `ordem_producao_ibfk_1` FOREIGN KEY (`funcionario_id`) REFERENCES `funcionarios` (`funcionario_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ordem_producao_ibfk_2` FOREIGN KEY (`maquina_id`) REFERENCES `maquinas` (`maquina_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordens_producao`
--

LOCK TABLES `ordens_producao` WRITE;
/*!40000 ALTER TABLE `ordens_producao` DISABLE KEYS */;
INSERT INTO `ordens_producao` VALUES (1,1,1,'Peça A',100,'Em produção'),(2,2,2,'Peça B',50,'Pendente'),(3,3,3,'Componente C',200,'Finalizada'),(5,5,5,'Produto E',80,'Finalizada'),(6,6,6,'Componente F',60,'Pendente'),(8,8,8,'Produto H',30,'Cancelada'),(9,9,9,'Peça I',75,'Finalizada'),(10,10,10,'Produto J',90,'Em produção');
/*!40000 ALTER TABLE `ordens_producao` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-06-30 16:08:15
