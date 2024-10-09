DROP TABLE IF EXISTS `Items`;
CREATE TABLE IF NOT EXISTS `Items` (
  `ItemId` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyId` int(11) DEFAULT NULL,
  `ParentId` int(11) DEFAULT NULL,
  `ItemTypeId` int(11) DEFAULT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`ItemId`),
  KEY `FK_Items_CompanyId` (`CompanyId`),
  KEY `FK_Items_ParentId` (`ParentId`),
  KEY `FK_Items_ItemTypeId` (`ItemTypeId`),
  CONSTRAINT `FK_Items_CompanyId` FOREIGN KEY (`CompanyId`) REFERENCES `Companies` (`CompanyId`),
  CONSTRAINT `FK_Items_ItemTypeId` FOREIGN KEY (`ItemTypeId`) REFERENCES `ItemTypes` (`ItemTypeId`),
  CONSTRAINT `FK_Items_ParentId` FOREIGN KEY (`ParentId`) REFERENCES `Items` (`ItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
