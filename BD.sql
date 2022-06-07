-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: proyecto001.cmu1nv4edpom.us-east-1.rds.amazonaws.com    Database: DonJuanTrading
-- ------------------------------------------------------
-- Server version	8.0.28

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '';

--
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `id_admin` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(40) DEFAULT NULL,
  `contrasena` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_admin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carrito_temp`
--

DROP TABLE IF EXISTS `carrito_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carrito_temp` (
  `id_carro` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `id_producto` int NOT NULL,
  `nombre_prod` varchar(40) NOT NULL,
  `cantidad` int NOT NULL,
  `precio` varchar(10) NOT NULL,
  `total` varchar(10) NOT NULL,
  PRIMARY KEY (`id_carro`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carrito_temp`
--

LOCK TABLES `carrito_temp` WRITE;
/*!40000 ALTER TABLE `carrito_temp` DISABLE KEYS */;
INSERT INTO `carrito_temp` VALUES (7,11,2,'Fantasma',2,'299.0','598.0'),(13,10,1,'Sangre de Indio',1,'499.0','499.0');
/*!40000 ALTER TABLE `carrito_temp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cat`
--

DROP TABLE IF EXISTS `cat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cat` (
  `id_cat` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) DEFAULT NULL,
  `descripcion` varchar(400) DEFAULT NULL,
  PRIMARY KEY (`id_cat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cat`
--

LOCK TABLES `cat` WRITE;
/*!40000 ALTER TABLE `cat` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `apellido` varchar(40) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `calle_num` varchar(40) NOT NULL,
  `colonia` varchar(40) NOT NULL,
  `c_p` varchar(5) NOT NULL,
  `ciudad` varchar(40) NOT NULL,
  `telefono` varchar(13) NOT NULL,
  `antiguedad` varchar(40) NOT NULL,
  `rfc` varchar(13) DEFAULT NULL,
  `contrasena` varchar(200) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  UNIQUE KEY `correo_UNIQUE` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (2,'Fernando Alonso','Torres','18041428@itasasd.com','virgo 204','Rinconada Sol','34228','Durango','6182907979','',NULL,'pbkdf2:sha256:260000$EeJTfGGjBbznV9NE$33629e3c3e2e5b499acdddc29e38ef5b7b05b5d0da25c09c3912d36ee9bc89f4'),(3,'Juan Carlos','Cueto','18041424@itdurango.edu.mx','','','','','','',NULL,'pbkdf2:sha256:260000$JDkwtd9WJ13muKVP$da156712f0d484350aa4a67a488c8384b76bdbcb44c96e13ad7c2ee29a475e0e'),(4,'pepe peres','Toño','asdasd@gmail.com','ecuador 506','el refugio','34229','tepehuanes','6185897979','2022-05-25',NULL,'pbkdf2:sha256:260000$LZSG77wMXWb2NlGW$478ce67d3b112923ab92a69c92bd71a839b50dc9c2ac523a0f5f7c9883d2c906'),(9,'pepe','Toño','gfhfghfghfg@gmail.com','ecuador 506','el refugio','12345','tepehuanes','1234567890','2022-05-25',NULL,'pbkdf2:sha256:260000$ZIZLTha2mQLW2bTQ$c397c9fca51b883d35d3b90e9b05cff35375af2ef753c8359f091edc30b0151d'),(10,'Juan','Carlos','juancarlos.cueto716@gmail.com','fasd','fs','34222','fads','8131400335','2022-05-30',NULL,'pbkdf2:sha256:260000$6XbC9rjH42d8Vt92$df2e3c9d55fa7b8ef9f850e940ddb5f79a6f0b534be8c0ebb38da3deebaefea4'),(11,'Ellen','Cueto','123456@gmail.com','fasd','ARTURO','12345','durango','6182091717','2022-05-31',NULL,'pbkdf2:sha256:260000$wSDgwmuSieMQ9rbJ$4ebfb789c3419b7d7d139148b6ac5df638875ee4f4317c797381f6508015b393'),(12,'Antonio','Perez Luche','Antonio@hotmail.pe','micasa 213','los aguaceros','8857','tepehuanes','6182907979','2022-06-01',NULL,'pbkdf2:sha256:260000$Lrrb6cXTJt5vYAhF$f57d42894b6e12ec74d6bf8b456260959b7ca8c7c15a0ecb2c964795fb39fc6f'),(13,'Admin','root','admin@donjuantrading.com','','','','','','',NULL,'pbkdf2:sha256:260000$Ayj8rfblSZiFcOq2$c49fbce4bf23620856a097dfc782a4a7f54954c181ba2634615b21fd77a5e1dc');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cli` int NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `cna` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_cli`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'18041428@itdurango.edu.mx','1234');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuentabanco`
--

DROP TABLE IF EXISTS `cuentabanco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuentabanco` (
  `id_cuenta` int NOT NULL AUTO_INCREMENT,
  `num_cuenta` int DEFAULT NULL,
  `nombre_banco` varchar(40) DEFAULT NULL,
  `nombre_benef` varchar(40) DEFAULT NULL,
  `tipo_cuenta` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_cuenta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuentabanco`
--

LOCK TABLES `cuentabanco` WRITE;
/*!40000 ALTER TABLE `cuentabanco` DISABLE KEYS */;
/*!40000 ALTER TABLE `cuentabanco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `detalleventa`
--

DROP TABLE IF EXISTS `detalleventa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `detalleventa` (
  `id_detalle` int NOT NULL AUTO_INCREMENT,
  `id_venta` int DEFAULT NULL,
  `id_prod` int DEFAULT NULL,
  `cantidad` varchar(10) DEFAULT NULL,
  `precio_vent` varchar(10) DEFAULT NULL,
  `estado_vent` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_detalle`)
) ENGINE=InnoDB AUTO_INCREMENT=1792 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `detalleventa`
--

LOCK TABLES `detalleventa` WRITE;
/*!40000 ALTER TABLE `detalleventa` DISABLE KEYS */;
INSERT INTO `detalleventa` VALUES (1790,45,1,'10','499.0','Pagado y Enviado'),(1791,46,3,'1','799.0','Pagado y Enviado');
/*!40000 ALTER TABLE `detalleventa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `envios`
--

DROP TABLE IF EXISTS `envios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `envios` (
  `id_envio` int NOT NULL AUTO_INCREMENT,
  `direccion` varchar(40) DEFAULT NULL,
  `ciudad` varchar(20) DEFAULT NULL,
  `calle_num` varchar(10) DEFAULT NULL,
  `c_p` int DEFAULT NULL,
  `nombre` varchar(20) DEFAULT NULL,
  `id_venta` int DEFAULT NULL,
  `id_detalle` int DEFAULT NULL,
  PRIMARY KEY (`id_envio`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `envios`
--

LOCK TABLES `envios` WRITE;
/*!40000 ALTER TABLE `envios` DISABLE KEYS */;
INSERT INTO `envios` VALUES (33,'Rinconada Sol','Durango','virgo 204',34228,'Fernando Alonso',45,1790),(34,'Rinconada Sol','Durango','virgo 204',34228,'Fernando Alonso',46,1791);
/*!40000 ALTER TABLE `envios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `id_inventario` int NOT NULL AUTO_INCREMENT,
  `id_prod` int DEFAULT NULL,
  `stock_max` varchar(10) DEFAULT NULL,
  `stock_min` varchar(10) DEFAULT NULL,
  `precio_prov` varchar(10) DEFAULT NULL,
  `precio_vent` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_inventario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos`
--

DROP TABLE IF EXISTS `pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos` (
  `id_pago` int NOT NULL AUTO_INCREMENT,
  `id_venta` int DEFAULT NULL,
  `id_cliente` int DEFAULT NULL,
  `num_tarjeta` varchar(40) DEFAULT NULL,
  `nombre_tarjeta` varchar(40) DEFAULT NULL,
  `fecha_tarjeta` varchar(5) DEFAULT NULL,
  `codigo_tarjeta` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id_pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos`
--

LOCK TABLES `pagos` WRITE;
/*!40000 ALTER TABLE `pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_prod` int NOT NULL AUTO_INCREMENT,
  `nombre_prod` varchar(40) NOT NULL,
  `descripcion` varchar(1000) NOT NULL,
  `cat` int DEFAULT NULL,
  `id_inv` int DEFAULT NULL,
  `precio` varchar(10) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `descripcion_corta` varchar(100) NOT NULL,
  `existencias` int NOT NULL,
  PRIMARY KEY (`id_prod`),
  UNIQUE KEY `nombre_prod_UNIQUE` (`nombre_prod`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Sangre de Indio','Mezcal tradicional, representativo de la región de Nombre de Dios, Durango, Mex.  El mejor para degustar solo, como un trago derecho, es un Mezcal dulce para el conocedor. El mejor para abrir la imaginación al intentar descifrar el origen de sus ricos aromas cítrico ahumados. Para el consumidor familiarizado en el tema es un Mezcal interesante por el juego y combinación de aromas distintivos de un proceso artesanal, así como de las materias primas y herramientas con las que se elabora que en conjunto crean un carácter extraordinario en el destilado. ',NULL,NULL,'499','mezcal_01.png','Retrogusto agradable con notas aromáticas de la madera, y agave dulce.',140),(2,'Fantasma','Dulce y rudo a la imaginación por su contenido en alcohol. Mezcal fantasma porque en él, no se percibe su alcohol sino su sabor avainillado, para paladares sabios que lo toman directo sin mezclar. Inimaginable para algunos, resulta ser un poco más suave gracias a su proceso artesanal.',NULL,NULL,'299','mezcal_02.png','Mezcal con ligeros aromas frutales y leves notas a quiote.',175),(3,'Plata','Suave,  refinado, avainillado y  muy sutil al paladar. Por su baja graduación en alcohol y su delicadez, es apto para aquellas personas que degustaran el Mezcal por primera vez. Es ligero en aromas y sabores, el mezcla ideal para la elaboración de cócteles, originando un sabor exquisito de alta calidad, versátil para crear bebidas.',NULL,NULL,'799','mezcal_03.png','Retrogusto suave, dulce, terminado con un buen fin de boca ligero a madera, agave y peron.',188);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provedor`
--

DROP TABLE IF EXISTS `provedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provedor` (
  `id_prov` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) DEFAULT NULL,
  `Direccion` varchar(50) DEFAULT NULL,
  `c_p` varchar(5) DEFAULT NULL,
  `telefono` varchar(13) DEFAULT NULL,
  `correo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_prov`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provedor`
--

LOCK TABLES `provedor` WRITE;
/*!40000 ALTER TABLE `provedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `provedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sesion`
--

DROP TABLE IF EXISTS `sesion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sesion` (
  `id_sesion` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int NOT NULL,
  `tipo` varchar(40) NOT NULL,
  PRIMARY KEY (`id_sesion`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sesion`
--

LOCK TABLES `sesion` WRITE;
/*!40000 ALTER TABLE `sesion` DISABLE KEYS */;
INSERT INTO `sesion` VALUES (1,2,'Cliente'),(2,3,'Cliente'),(3,4,'Cliente'),(4,9,'Cliente'),(5,10,'Cliente'),(6,11,'Cliente'),(7,12,'Cliente'),(8,13,'Admin');
/*!40000 ALTER TABLE `sesion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venta`
--

DROP TABLE IF EXISTS `venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venta` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_prod` int DEFAULT NULL,
  `fecha_vent` varchar(40) DEFAULT NULL,
  `telefono` varchar(13) DEFAULT NULL,
  `id_envio` int DEFAULT NULL,
  `comprobante` varchar(100) DEFAULT NULL,
  `calificacion` varchar(10) DEFAULT NULL,
  `id_detalle` int DEFAULT NULL,
  PRIMARY KEY (`id_venta`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venta`
--

LOCK TABLES `venta` WRITE;
/*!40000 ALTER TABLE `venta` DISABLE KEYS */;
INSERT INTO `venta` VALUES (45,2,1,'2022-05-28','6182907979',33,NULL,NULL,1790),(46,2,3,'2022-05-28','6182907979',34,NULL,NULL,1791);
/*!40000 ALTER TABLE `venta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_realizadas`
--

DROP TABLE IF EXISTS `ventas_realizadas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas_realizadas` (
  `id_venta_realizada` int NOT NULL AUTO_INCREMENT,
  `id_prod` int NOT NULL,
  `id_cliente` int NOT NULL,
  `fecha_venta` varchar(45) NOT NULL,
  `cantidad_de_producto` int NOT NULL,
  `total_de_venta` float NOT NULL,
  `estado_de_venta` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_venta_realizada`),
  UNIQUE KEY `id_venta_realizada_UNIQUE` (`id_venta_realizada`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_realizadas`
--

LOCK TABLES `ventas_realizadas` WRITE;
/*!40000 ALTER TABLE `ventas_realizadas` DISABLE KEYS */;
INSERT INTO `ventas_realizadas` VALUES (13,1,2,'2022-05-30',10,4990,'Enviado'),(14,3,2,'2022-05-30',1,799,'Enviado'),(15,2,10,'2022-05-31',8,2392,'Enviado'),(16,1,10,'2022-06-01',3,1497,'Enviado'),(17,2,12,'2022-06-01',10,2990,'Enviado'),(18,3,10,'2022-05-31',7,5593,'Enviado'),(19,2,10,'2022-05-31',7,2093,'Enviado'),(20,1,10,'2022-05-31',7,3493,'Enviado');
/*!40000 ALTER TABLE `ventas_realizadas` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-05 17:52:13
