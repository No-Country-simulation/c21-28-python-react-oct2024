DROP TABLE IF EXISTS `Departaments`;
CREATE TABLE IF NOT EXISTS `Departaments` (
  `DepartamentId` int(11) NOT NULL,
  `CityId` int(11) NOT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`DepartamentId`),
  KEY `FK_Departaments_CityId` (`CityId`),
  CONSTRAINT `FK_Departaments_CityId` FOREIGN KEY (`CityId`) REFERENCES `Cities` (`CityId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
