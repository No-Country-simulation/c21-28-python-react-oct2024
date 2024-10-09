DROP TABLE IF EXISTS `PostalCodes`;
CREATE TABLE IF NOT EXISTS `PostalCodes` (
  `PostalCodeId` int(11) NOT NULL,
  `DepartamentId` int(11) NOT NULL,
  `Code` varchar(10) CHARACTER SET utf8 NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`PostalCodeId`),
  KEY `FK_PostalCodes_DepartamentId` (`DepartamentId`),
  CONSTRAINT `FK_PostalCodes_DepartamentId` FOREIGN KEY (`DepartamentId`) REFERENCES `Departaments` (`DepartamentId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
