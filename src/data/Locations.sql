DROP TABLE IF EXISTS `Locations`;
CREATE TABLE IF NOT EXISTS `Locations` (
  `LocationId` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyId` int(11) NOT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `CCode` varchar(5) CHARACTER SET utf8 NOT NULL,
  `NCode` smallint(6) NOT NULL,
  `IsRoot` smallint(6) NOT NULL DEFAULT '0',
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`LocationId`),
  UNIQUE KEY `IX_Locations_CCode` (`CCode`),
  UNIQUE KEY `IX_Locations_NCode` (`NCode`),
  KEY `FK_Locations_CompanyId` (`CompanyId`),
  KEY `FK_Locations_ParentId` (`ParentId`),
  CONSTRAINT `FK_Locations_CompanyId` FOREIGN KEY (`CompanyId`) REFERENCES `Companies` (`CompanyId`),
  CONSTRAINT `FK_Locations_ParentId` FOREIGN KEY (`ParentId`) REFERENCES `Locations` (`LocationId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
