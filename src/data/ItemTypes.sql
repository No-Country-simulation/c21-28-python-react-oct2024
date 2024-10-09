DROP TABLE IF EXISTS `ItemTypes`;
CREATE TABLE IF NOT EXISTS `ItemTypes` (
  `ItemTypeId` int(11) NOT NULL,
  `CompanyId` int(11) NOT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`ItemTypeId`),
  KEY `FK_ItemTypes_CompanyId` (`CompanyId`),
  KEY `FK_ItemTypes_ParentId` (`ParentId`),
  CONSTRAINT `FK_ItemTypes_CompanyId` FOREIGN KEY (`CompanyId`) REFERENCES `Companies` (`CompanyId`),
  CONSTRAINT `FK_ItemTypes_ParentId` FOREIGN KEY (`ParentId`) REFERENCES `ItemTypes` (`ItemTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
