-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: python
-- ------------------------------------------------------
-- Server version	5.6.40-log

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'lesseruser'),(1,'poweruser');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,30),(31,1,31),(32,1,32),(33,1,33),(34,1,34),(35,1,35),(36,1,36),(37,1,37),(38,1,38),(39,1,39),(40,1,40),(41,1,41),(42,1,42),(43,1,43),(44,1,44),(45,1,45),(46,1,46),(47,1,47),(48,1,48),(49,1,49),(50,1,50),(51,1,51),(52,1,52),(57,2,25),(58,2,26),(59,2,28),(60,2,29),(61,2,30),(62,2,32),(63,2,33),(64,2,34),(65,2,36),(66,2,37),(67,2,38),(68,2,40),(69,2,41),(70,2,42),(71,2,44),(72,2,45),(73,2,46),(74,2,48),(75,2,49),(76,2,50),(77,2,52);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add employee',7,'add_employee'),(26,'Can change employee',7,'change_employee'),(27,'Can delete employee',7,'delete_employee'),(28,'Can view employee',7,'view_employee'),(29,'Can add passangers',8,'add_passangers'),(30,'Can change passangers',8,'change_passangers'),(31,'Can delete passangers',8,'delete_passangers'),(32,'Can view passangers',8,'view_passangers'),(33,'Can add passengers',8,'add_passengers'),(34,'Can change passengers',8,'change_passengers'),(35,'Can delete passengers',8,'delete_passengers'),(36,'Can view passengers',8,'view_passengers'),(37,'Can add passenger',8,'add_passenger'),(38,'Can change passenger',8,'change_passenger'),(39,'Can delete passenger',8,'delete_passenger'),(40,'Can view passenger',8,'view_passenger'),(41,'Can add courses',9,'add_courses'),(42,'Can change courses',9,'change_courses'),(43,'Can delete courses',9,'delete_courses'),(44,'Can view courses',9,'view_courses'),(45,'Can add students',10,'add_students'),(46,'Can change students',10,'change_students'),(47,'Can delete students',10,'delete_students'),(48,'Can view students',10,'view_students'),(49,'Can add sk us',11,'add_skus'),(50,'Can change sk us',11,'change_skus'),(51,'Can delete sk us',11,'delete_skus'),(52,'Can view sk us',11,'view_skus'),(53,'Can add project',12,'add_project'),(54,'Can change project',12,'change_project'),(55,'Can delete project',12,'delete_project'),(56,'Can view project',12,'view_project'),(57,'Can add contact phone',13,'add_contactphone'),(58,'Can change contact phone',13,'change_contactphone'),(59,'Can delete contact phone',13,'delete_contactphone'),(60,'Can view contact phone',13,'view_contactphone'),(61,'Can add identification',14,'add_identification'),(62,'Can change identification',14,'change_identification'),(63,'Can delete identification',14,'delete_identification'),(64,'Can view identification',14,'view_identification');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$jkE7dfo5Tu2e$dfZU61Owae5lnBz54W41nnjhfSYxRloNhxKw2g8epRs=','2021-02-01 23:20:37.434919',1,'nvaadmin','','','narmstrong@ohiochristian.edu',1,1,'2021-01-22 16:52:56.028541'),(2,'pbkdf2_sha256$216000$VPrfyUwCtVpt$7Su2CzGp4BNd9fm6ggKAN+6+wTobygVZUukt5QzgsXs=','2021-02-01 23:35:58.955350',0,'lesser','','','',1,1,'2021-02-01 21:54:50.000000'),(3,'pbkdf2_sha256$216000$MDjxA7GGDVhC$pKywTUdJmpVu6bd7PDIu+eaqOOYzDNLShHFTCJeWYkg=','2021-02-01 23:36:53.095761',0,'power','','','',0,1,'2021-02-01 23:01:36.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,2),(2,3,1);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-01-22 16:56:38.915808','1','Employee object (1)',1,'[{\"added\": {}}]',7,1),(2,'2021-01-22 16:56:51.158573','2','Employee object (2)',1,'[{\"added\": {}}]',7,1),(3,'2021-01-22 17:01:51.513740','1','Employee object (1)',2,'[{\"changed\": {\"fields\": [\"Salary\"]}}]',7,1),(4,'2021-01-22 18:48:13.235807','1','jj@apalachia.durf',1,'[{\"added\": {}}]',8,1),(5,'2021-01-22 18:48:24.266609','2','dj@apalacia.dorf',1,'[{\"added\": {}}]',8,1),(6,'2021-01-22 18:48:38.146162','3','bj@apalacia.dorf',1,'[{\"added\": {}}]',8,1),(7,'2021-01-22 18:49:20.115338','4','sigcal@gmail.com',1,'[{\"added\": {}}]',8,1),(8,'2021-01-22 18:49:43.212829','5','thegirl@apalachia.durf',1,'[{\"added\": {}}]',8,1),(9,'2021-01-22 18:49:54.609336','3','bj@apalacia.durf',2,'[{\"changed\": {\"fields\": [\"Email\"]}}]',8,1),(10,'2021-01-22 18:50:00.468607','2','dj@apalacia.durf',2,'[{\"changed\": {\"fields\": [\"Email\"]}}]',8,1),(11,'2021-01-22 18:50:11.482237','2','dj@apalachia.durf',2,'[{\"changed\": {\"fields\": [\"Email\"]}}]',8,1),(12,'2021-01-22 18:50:18.140751','3','bj@apalachia.durf',2,'[{\"changed\": {\"fields\": [\"Email\"]}}]',8,1),(13,'2021-01-26 03:18:26.998030','1','1 | Movies and how to watch them | Nathanael ---> This course teaches students h...',1,'[{\"added\": {}}]',9,1),(14,'2021-01-26 15:24:36.946327','1','Students object (1)',1,'[{\"added\": {}}]',10,1),(15,'2021-02-01 21:54:50.922358','2','test',1,'[{\"added\": {}}]',4,1),(16,'2021-02-01 22:22:33.413948','2','test',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(17,'2021-02-01 22:58:20.290626','1','poweruser',1,'[{\"added\": {}}]',3,1),(18,'2021-02-01 23:00:09.195607','2','lesseruser',1,'[{\"added\": {}}]',3,1),(19,'2021-02-01 23:00:48.700001','1','poweruser',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(20,'2021-02-01 23:01:03.366510','2','lesseruser',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,1),(21,'2021-02-01 23:01:17.175493','2','test',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(22,'2021-02-01 23:01:26.413646','2','leser',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,1),(23,'2021-02-01 23:01:36.783349','3','power',1,'[{\"added\": {}}]',4,1),(24,'2021-02-01 23:01:45.896207','3','power',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,1),(25,'2021-02-01 23:20:42.780286','2','lesser',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'mysql_cart','skus'),(9,'mysql_course','courses'),(10,'mysql_CVB','students'),(13,'mysql_hr','contactphone'),(7,'mysql_hr','employee'),(14,'mysql_hr','identification'),(8,'mysql_hr','passenger'),(12,'mysql_hr','project'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-01-22 16:26:21.308117'),(2,'auth','0001_initial','2021-01-22 16:26:21.538374'),(3,'admin','0001_initial','2021-01-22 16:26:21.872958'),(4,'admin','0002_logentry_remove_auto_add','2021-01-22 16:26:21.948955'),(5,'admin','0003_logentry_add_action_flag_choices','2021-01-22 16:26:21.964958'),(6,'contenttypes','0002_remove_content_type_name','2021-01-22 16:26:22.040863'),(7,'auth','0002_alter_permission_name_max_length','2021-01-22 16:26:22.084183'),(8,'auth','0003_alter_user_email_max_length','2021-01-22 16:26:22.133441'),(9,'auth','0004_alter_user_username_opts','2021-01-22 16:26:22.142444'),(10,'auth','0005_alter_user_last_login_null','2021-01-22 16:26:22.183452'),(11,'auth','0006_require_contenttypes_0002','2021-01-22 16:26:22.186453'),(12,'auth','0007_alter_validators_add_error_messages','2021-01-22 16:26:22.203472'),(13,'auth','0008_alter_user_username_max_length','2021-01-22 16:26:22.244973'),(14,'auth','0009_alter_user_last_name_max_length','2021-01-22 16:26:22.286743'),(15,'auth','0010_alter_group_name_max_length','2021-01-22 16:26:22.359777'),(16,'auth','0011_update_proxy_permissions','2021-01-22 16:26:22.369778'),(17,'auth','0012_alter_user_first_name_max_length','2021-01-22 16:26:22.423790'),(18,'mysql_hr','0001_initial','2021-01-22 16:26:22.468800'),(19,'sessions','0001_initial','2021-01-22 16:26:22.508650'),(20,'mysql_hr','0002_auto_20210122_1344','2021-01-22 18:44:14.682302'),(21,'mysql_hr','0003_auto_20210122_1346','2021-01-22 18:46:03.504092'),(22,'mysql_hr','0004_auto_20210122_1347','2021-01-22 18:47:22.089413'),(23,'mysql_hr','0005_auto_20210125_1315','2021-01-25 18:16:01.508935'),(24,'mysql_hr','0006_passenger_ssn','2021-01-25 18:19:29.994468'),(25,'mysql_course','0001_initial','2021-01-26 03:08:12.696251'),(26,'mysql_hr','0007_auto_20210125_2208','2021-01-26 03:08:12.704253'),(27,'mysql_course','0002_auto_20210125_2217','2021-01-26 03:17:13.805614'),(28,'mysql_CVB','0001_initial','2021-01-26 15:21:49.202999'),(29,'mysql_cart','0001_initial','2021-01-28 18:53:55.740815'),(30,'mysql_cart','0002_auto_20210129_1434','2021-01-29 19:35:03.648029'),(31,'mysql_hr','0008_project','2021-02-02 18:14:13.619489'),(32,'mysql_hr','0009_contactphone','2021-02-02 18:51:03.395076'),(33,'mysql_hr','0010_identification','2021-02-02 21:47:33.593325');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('k20kzukizdsklu660gtusepjuwoblzfd','.eJxVjEEOwiAQRe_C2hCYQgGX7j0DmWHAVg0kpV0Z765NutDtf-_9l4i4rVPcel7izOIstDj9boTpkesO-I711mRqdV1mkrsiD9rltXF-Xg7372DCPn3rkQyb4hQ58hgAbNEJRlAwDGQDB2sssUsuEQMHj57NmACLZsVlcCTeH941ODA:1l5WqF:XMkygE_PVA_opLwcSZakBoWRdOFMIOm9x0L6b3vHoOg','2021-02-12 16:41:51.935947'),('nnb3861m07s87luae207cqfmhjw5lkjn','.eJxVjDsOwjAQBe_iGlnerH-hpOcM1tpe4wBypDipEHeHSCmgfTPzXiLQttawdV7ClMVZoDj9bpHSg9sO8p3abZZpbusyRbkr8qBdXufMz8vh_h1U6vVbF5-jtQ7QWeOZvCWlYHRGAQMkBDSD4TFpMDp61M7lXKIvaAnTwM6L9we5RTbv:1l6ikX:Nkiluej1s4L0e2H1S9Df7papcdAjws5iMwsIoO4v_MI','2021-02-15 23:36:53.096608');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_cart_skus`
--

DROP TABLE IF EXISTS `mysql_cart_skus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_cart_skus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sku` varchar(30) NOT NULL,
  `mfg` varchar(50) NOT NULL,
  `name` varchar(200) NOT NULL,
  `desc` longtext NOT NULL,
  `price` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sku` (`sku`),
  UNIQUE KEY `mysql_cart_skus_sku_mfg_3a9a40de_uniq` (`sku`,`mfg`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_cart_skus`
--

LOCK TABLES `mysql_cart_skus` WRITE;
/*!40000 ALTER TABLE `mysql_cart_skus` DISABLE KEYS */;
INSERT INTO `mysql_cart_skus` VALUES (1,'LG-120','LG','LG 120 Phone','An ok phone that does general phone stuff.  Not Phoney - but not great either.  It\'s worth buying because it\'s an LG.',80),(2,'C-2100','Cobra','Cobra Walkie Talkie','This model of walkie talkies makes mothers extremely annoying.  But yea, you don\'t need to know all about this really.',20),(3,'CO-22','Cowin','Cowin Blue Tooth Noise Cancelling Headphones','A nice pair of noise cancelling headphones.  They almost never run out of batteries, so I\'m super impressed.',65),(4,'Dog-01','God','Slider, the Scared','This dog is - very MEH, I mean, he is not a BAD BAD dog, but also - I would like to get inside of his brain and re-work some of his dog-ness.  Mainly I\'d remove his anxiety.',755),(5,'Cat_01','God','The Cat','This cat is literally the best.  He\'s fun, he\'s active, he\'s a bit of a chonk.  He\'s neat and clean and he comes upstairs to pray with us at night.  BEST!  HIGHEST RATED!',900);
/*!40000 ALTER TABLE `mysql_cart_skus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_course_courses`
--

DROP TABLE IF EXISTS `mysql_course_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_course_courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  `instructor` varchar(100) NOT NULL,
  `rating` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_course_courses`
--

LOCK TABLES `mysql_course_courses` WRITE;
/*!40000 ALTER TABLE `mysql_course_courses` DISABLE KEYS */;
INSERT INTO `mysql_course_courses` VALUES (1,'Movies and how to watch them','This course teaches students how to watch movies.  Graduates will have a grasp of the following concepts: Do not talk during movies, do not ask questions, do not use your phone.','Nathanael',3),(3,'Get A Life','Learn how to assertively say Yes and No to others.  Throw off the hope crushing weight of performance guilt wrought from the unfulfilled dreams of your elders.','Kelly Bear McFreedom',5),(4,'You 2000 vs You 3000','In a post apocalyptical tri-centric nomenclature of the modern fantasy genre comic series: \"Time Capitulation\" learn to understand one\'s soul-composition by staring in the mirror.','Terrance of Parsec None',1),(7,'The Jack Daniel\'s Experience','Explore the acute loss of mindfulness while ingesting one of America\'s most prestigious beverages.','Capt. Jolly Rodger',5),(8,'FooBar PHP','Postscript Preprocessing of HTML is like a Foo fightin\' Bar fight of Foo\'n Fun','Gnome Won',1);
/*!40000 ALTER TABLE `mysql_course_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_cvb_students`
--

DROP TABLE IF EXISTS `mysql_cvb_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_cvb_students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first` varchar(30) NOT NULL,
  `last` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `grade` double NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_cvb_students`
--

LOCK TABLES `mysql_cvb_students` WRITE;
/*!40000 ALTER TABLE `mysql_cvb_students` DISABLE KEYS */;
INSERT INTO `mysql_cvb_students` VALUES (1,'Dark','Furrer','dferrer@darkdarkness.world',2),(4,'Another','Student','as@place.com',4),(5,'Jiggle','Smiggles','jsmiggles@bing.com',1.2),(6,'Nate','the Great','n8thegreat@gmail.com',4),(7,'Investigate','Prograstinate','ip@gmail.com',4),(8,'Jerry','Django','jd@westcoast.com',2.2);
/*!40000 ALTER TABLE `mysql_cvb_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_hr_contactphone`
--

DROP TABLE IF EXISTS `mysql_hr_contactphone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_hr_contactphone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `number` varchar(10) NOT NULL,
  `owner_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mysql_hr_contactphone_owner_id_ae7b40b9_fk_mysql_hr_employee_id` (`owner_id`),
  CONSTRAINT `mysql_hr_contactphone_owner_id_ae7b40b9_fk_mysql_hr_employee_id` FOREIGN KEY (`owner_id`) REFERENCES `mysql_hr_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_hr_contactphone`
--

LOCK TABLES `mysql_hr_contactphone` WRITE;
/*!40000 ALTER TABLE `mysql_hr_contactphone` DISABLE KEYS */;
INSERT INTO `mysql_hr_contactphone` VALUES (1,'home','7405459547',1),(2,'cell','7402073024',1),(3,'office','8007721254',2),(4,'office','8007721254',2);
/*!40000 ALTER TABLE `mysql_hr_contactphone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_hr_employee`
--

DROP TABLE IF EXISTS `mysql_hr_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_hr_employee` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(30) NOT NULL,
  `lastName` varchar(30) NOT NULL,
  `salary` double NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_hr_employee`
--

LOCK TABLES `mysql_hr_employee` WRITE;
/*!40000 ALTER TABLE `mysql_hr_employee` DISABLE KEYS */;
INSERT INTO `mysql_hr_employee` VALUES (1,'Nathanael','Armstrong',2000,'n8thanael@gmail.com'),(2,'Hayley','Armstrong',25000,'harmstrong9547@gmail.com');
/*!40000 ALTER TABLE `mysql_hr_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_hr_identification`
--

DROP TABLE IF EXISTS `mysql_hr_identification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_hr_identification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `number` varchar(10) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_id` (`employee_id`),
  CONSTRAINT `mysql_hr_identificat_employee_id_a8517865_fk_mysql_hr_` FOREIGN KEY (`employee_id`) REFERENCES `mysql_hr_employee` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_hr_identification`
--

LOCK TABLES `mysql_hr_identification` WRITE;
/*!40000 ALTER TABLE `mysql_hr_identification` DISABLE KEYS */;
INSERT INTO `mysql_hr_identification` VALUES (1,'state_lice','RP12345-01',1);
/*!40000 ALTER TABLE `mysql_hr_identification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_hr_passenger`
--

DROP TABLE IF EXISTS `mysql_hr_passenger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_hr_passenger` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first` varchar(30) NOT NULL,
  `last` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `points` double NOT NULL,
  `gender` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `ssn` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_hr_passenger`
--

LOCK TABLES `mysql_hr_passenger` WRITE;
/*!40000 ALTER TABLE `mysql_hr_passenger` DISABLE KEYS */;
INSERT INTO `mysql_hr_passenger` VALUES (1,'Jon','Jimmy','jj@apalachia.durf',20,'','',0),(2,'Dan','Jimmy','dj@westlafayette.com',35,'','',0),(3,'Bob','Jimmy','bj@apalachia.durf',44,'','',0),(4,'Sigfried','Calpershots','sigcal@gmail.com',980112,'','',0),(5,'Jill','Jimmy','thegirl@apalachia.durf',14,'','',0),(9,'Giz','Modo','gizmodo@gizmodo.com',50,'Unknown','123456QW',123456789),(11,'Joy','Singbob','joy.singbob@gmail.com',1234,'female','Abcdefghijklmnopqrs',123456789),(14,'Bob','Jones','bj@there.com',0,'male','asdf123',0),(15,'Willy','Carter','wcarter@woodburyoutfitters.com',50,'male','123456QA',123456789);
/*!40000 ALTER TABLE `mysql_hr_passenger` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_hr_project`
--

DROP TABLE IF EXISTS `mysql_hr_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_hr_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `projectName` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_hr_project`
--

LOCK TABLES `mysql_hr_project` WRITE;
/*!40000 ALTER TABLE `mysql_hr_project` DISABLE KEYS */;
INSERT INTO `mysql_hr_project` VALUES (1,'Trash Collection');
/*!40000 ALTER TABLE `mysql_hr_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mysql_hr_project_programmers`
--

DROP TABLE IF EXISTS `mysql_hr_project_programmers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mysql_hr_project_programmers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mysql_hr_project_program_project_id_employee_id_2a5d9e1e_uniq` (`project_id`,`employee_id`),
  KEY `mysql_hr_project_pro_employee_id_5563389c_fk_mysql_hr_` (`employee_id`),
  CONSTRAINT `mysql_hr_project_pro_employee_id_5563389c_fk_mysql_hr_` FOREIGN KEY (`employee_id`) REFERENCES `mysql_hr_employee` (`id`),
  CONSTRAINT `mysql_hr_project_pro_project_id_6c88a5f1_fk_mysql_hr_` FOREIGN KEY (`project_id`) REFERENCES `mysql_hr_project` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mysql_hr_project_programmers`
--

LOCK TABLES `mysql_hr_project_programmers` WRITE;
/*!40000 ALTER TABLE `mysql_hr_project_programmers` DISABLE KEYS */;
INSERT INTO `mysql_hr_project_programmers` VALUES (1,1,1),(2,1,2);
/*!40000 ALTER TABLE `mysql_hr_project_programmers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'python'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 15:14:51
