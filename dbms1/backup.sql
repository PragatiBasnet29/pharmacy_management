-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy
-- ------------------------------------------------------
-- Server version	8.0.33
/*!40101 SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci */;

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
-- Table structure for table contract
--

DROP TABLE IF EXISTS contract;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE contract (
  Contract_ID int NOT NULL,
  PharmaceuticalCo varchar(100) NOT NULL,
  Pharmacy_ID int NOT NULL,
  Start_Date date NOT NULL,
  End_Date date NOT NULL,
  Contract_Text text,
  Supervisor varchar(100) NOT NULL,
  PRIMARY KEY (Contract_ID),
  KEY PharmaceuticalCo (PharmaceuticalCo),
  KEY Pharmacy_ID (Pharmacy_ID),
  CONSTRAINT contract_ibfk_1 FOREIGN KEY (PharmaceuticalCo) REFERENCES pharmaceuticalco (CompanyName),
  CONSTRAINT contract_ibfk_2 FOREIGN KEY (Pharmacy_ID) REFERENCES pharmacy (Pharmacy_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci */;


--
-- Dumping data for table contract
--

LOCK TABLES contract WRITE;
/*!40000 ALTER TABLE contract DISABLE KEYS */;
/*!40000 ALTER TABLE contract ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table doctors
--

DROP TABLE IF EXISTS doctors;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE doctors (
  SSN varchar(20) NOT NULL,
  Name varchar(100) NOT NULL,
  Specialty varchar(100) NOT NULL,
  YearsOfExp int NOT NULL,
  PRIMARY KEY (SSN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table doctors
--

LOCK TABLES doctors WRITE;
/*!40000 ALTER TABLE doctors DISABLE KEYS */;
INSERT INTO doctors VALUES ('456789123','Dr. Sunita Singh','Pediatrician',10),('789123456','Dr. Deepak Acharya','Orthopedic Surgeon',20),('987654321','Dr. Rajesh Sharma','Cardiologist',15);
/*!40000 ALTER TABLE doctors ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table drug
--

DROP TABLE IF EXISTS drug;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE drug (
  Trade_Name varchar(100) NOT NULL,
  Formula varchar(200) NOT NULL,
  CompanyName varchar(100) NOT NULL,
  PRIMARY KEY (Trade_Name),
  KEY CompanyName (CompanyName),
  CONSTRAINT drug_ibfk_1 FOREIGN KEY (CompanyName) REFERENCES pharmaceuticalco (CompanyName)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table drug
--

LOCK TABLES drug WRITE;
/*!40000 ALTER TABLE drug DISABLE KEYS */;
/*!40000 ALTER TABLE drug ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table patients
--

DROP TABLE IF EXISTS patients;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE patients (
  SSN varchar(20) NOT NULL,
  Name varchar(100) NOT NULL,
  Address varchar(200) NOT NULL,
  Age int NOT NULL,
  PRIMARY KEY (SSN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table patients
--

LOCK TABLES patients WRITE;
/*!40000 ALTER TABLE patients DISABLE KEYS */;
INSERT INTO patients VALUES ('123456789','Hari Bahadur Thapa','Kathmandu, Nepal',42),('456789123','Gita Tamang','Biratnagar, Nepal',28),('987654321','Sita Shrestha','Pokhara, Nepal',35);
/*!40000 ALTER TABLE patients ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table pharmaceuticalco
--

DROP TABLE IF EXISTS pharmaceuticalco;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE pharmaceuticalco (
  CompanyName varchar(100) NOT NULL,
  Phone_Number varchar(20) NOT NULL,
  PRIMARY KEY (CompanyName)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table pharmaceuticalco
--

LOCK TABLES pharmaceuticalco WRITE;
/*!40000 ALTER TABLE pharmaceuticalco DISABLE KEYS */;
INSERT INTO pharmaceuticalco VALUES ('Everest Pharmaceuticals','+977-1-7778888'),('Himalayan Healthcare','+977-1-5556666'),('Nepal Pharma','+977-1-4445555');
/*!40000 ALTER TABLE pharmaceuticalco ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table pharmacy
--

DROP TABLE IF EXISTS pharmacy;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE pharmacy (
  Pharmacy_ID int NOT NULL,
  Name varchar(100) NOT NULL,
  Address varchar(200) NOT NULL,
  Phone_Number varchar(20) NOT NULL,
  PRIMARY KEY (Pharmacy_ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table pharmacy
--

LOCK TABLES pharmacy WRITE;
/*!40000 ALTER TABLE pharmacy DISABLE KEYS */;
/*!40000 ALTER TABLE pharmacy ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table prescription_history
--

DROP TABLE IF EXISTS prescription_history;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE prescription_history (
  Doctor_SSN varchar(20) NOT NULL,
  Patient_SSN varchar(20) NOT NULL,
  Drug_TradeName varchar(100) NOT NULL,
  Prescription_Date date NOT NULL,
  PRIMARY KEY (Doctor_SSN,`Patient_SSN`,`Drug_TradeName`),
  KEY Patient_SSN (Patient_SSN),
  KEY Drug_TradeName (Drug_TradeName),
  CONSTRAINT prescription_history_ibfk_1 FOREIGN KEY (Doctor_SSN) REFERENCES doctors (SSN),
  CONSTRAINT prescription_history_ibfk_2 FOREIGN KEY (Patient_SSN) REFERENCES patients (SSN),
  CONSTRAINT prescription_history_ibfk_3 FOREIGN KEY (Drug_TradeName) REFERENCES drug (Trade_Name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table prescription_history
--

LOCK TABLES prescription_history WRITE;
/*!40000 ALTER TABLE prescription_history DISABLE KEYS */;
/*!40000 ALTER TABLE prescription_history ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table prescriptions
--

DROP TABLE IF EXISTS prescriptions;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE prescriptions (
  Prescription_ID int NOT NULL,
  Doctor_SSN varchar(20) NOT NULL,
  Patient_SSN varchar(20) NOT NULL,
  Drug_TradeName varchar(100) NOT NULL,
  Date date NOT NULL,
  Quantity int NOT NULL,
  PRIMARY KEY (Prescription_ID),
  KEY Doctor_SSN (Doctor_SSN),
  KEY Patient_SSN (Patient_SSN),
  KEY Drug_TradeName (Drug_TradeName),
  CONSTRAINT prescriptions_ibfk_1 FOREIGN KEY (Doctor_SSN) REFERENCES doctors (SSN),
  CONSTRAINT prescriptions_ibfk_2 FOREIGN KEY (Patient_SSN) REFERENCES patients (SSN),
  CONSTRAINT prescriptions_ibfk_3 FOREIGN KEY (Drug_TradeName) REFERENCES drug (Trade_Name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table prescriptions
--

LOCK TABLES prescriptions WRITE;
/*!40000 ALTER TABLE prescriptions DISABLE KEYS */;
/*!40000 ALTER TABLE prescriptions ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-29 17:38:00